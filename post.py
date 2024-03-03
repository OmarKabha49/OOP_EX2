from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define a base class for all types of posts
class Post:
    def __init__(self, user, text=str):
        self.user = user
        self.text = text

    # Method to like a post
    def like(self, Liker):
        if self.user.getName() != Liker.getName():
            message = f"{Liker.getName()} liked your post"
            self.user.receiveNotification(message)
            print(f"notification to {self.user.getName()}: {message}")

    # Method to comment on a post
    def comment(self, Commenter, text=str):
        message = f"{Commenter.getName()} commented on your post"
        self.user.receiveNotification(message)
        print(f"notification to {self.user.getName()}: {message}: {text}")

    @abstractmethod
    def display(self):
        pass

# Define a subclass for text posts
class TextPost(Post):
    def __init__(self, user, text=str):
        super().__init__(user, text)

    # Method to display text post
    def display(self):
        print(f"{self.user.getName()} published a post:")
        print(f'"{self.text}"')
        print()

    # Override __str__ method for string representation
    def __str__(self):
        print(f"{self.user.getName()} published a post:")
        return f'"{self.text}"\n'

# Define a subclass for image posts
class ImagePost(Post):
    def __init__(self, user, text=str):
        super().__init__(user, text)

    # Method to display image post
    def display(self):
        print("Shows picture")
        try:
            image = plt.imread(self.text)
            plt.imshow(image)
            plt.axis('off')  # Turn off axis
            plt.show()
        except FileNotFoundError:
            pass

    # Override __str__ method for string representation
    def __str__(self):
        return f"{self.user.getName()} posted a picture\n"

# Define a subclass for sale posts
class SalePost(Post):
    def __init__(self, user, text=str, price=float, location=str):
        super().__init__(user, text)
        self.price = price
        self.location = location
        self.isAvailable = True

    # Method to mark the sale of a product
    def sold(self, password=str):
        self.isAvailable = False
        print(f"{self.user.getName()}'s product is sold")

    # Method to apply discount to the product
    def discount(self, percent=int, password=str):
        self.price -= self.price * percent / 100
        print(f"Discount on {self.user.getName()} product! the new price is: {self.price}")

    # Method to display sale post
    def display(self):
        print(f"{self.user.getName()} posted a product for sale:")
        print(f"For sale! {self.text}, price: {self.price}, pickup from: {self.location}")
        print()

    # Override __str__ method for string representation
    def __str__(self):
        print(f"{self.user.getName()} posted a product for sale:")
        status = "For sale" if self.isAvailable else "Sold"
        return f"{status}! {self.text}, price: {self.price}, pickup from: {self.location}\n"

# Factory class to create posts
class postFactory:
    def create_post(self, user, *args):

        # Determine the type of post to create
        if self == "Text":
            return TextPost(user, *args)

        elif self == "Image":
            return ImagePost(user, *args)

        elif self == "Sale":
            return SalePost(user, *args)

        else:
            return None
