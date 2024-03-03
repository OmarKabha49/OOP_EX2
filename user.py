from post import postFactory

class User:
    def __init__(self, username=str, password=str):
        self.username = username
        if self.isValidPassword(password):
            self.password = password

        self.following = set()         # Set to store users followed by this user
        self.followers = set()         # Set to store users who follow this user
        self.posts = []                # List to store posts made by this user
        self.notifications = []        # List to store notifications received by this user
        self.isOnline = False          # Flag to indicate if the user is currently online

    # Method to follow another user
    def follow(self, otherUser):
        if self != otherUser:
            if otherUser not in self.following:
                self.following.add(otherUser)
                otherUser.followers.add(self)
                print(f"{self.username} started following {otherUser.username}")

    # Method to unfollow another user
    def unfollow(self, otherUser):
        if self != otherUser:
            if otherUser in self.following:
                self.following.remove(otherUser)
                otherUser.followers.remove(self)
                print(f"{self.getName()} unfollowed {otherUser.getName()}")

    # Method to print notifications received by the user
    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.notifications:
            print(notification)

    # Method to receive a notification
    def receiveNotification(self, notification=str):
        self.notifications.append(notification)

    # Method to notify followers about a new post (part of Observer pattern)
    def notifyFollower(self, notification):
        for follower in self.followers:
            follower.receiveNotification(notification)  # Notify each follower about the new post

    # Method to return string representation of the user
    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}"

    # Method to validate password
    def isValidPassword(self, password):
        return 4 <= len(password) <= 8

    # Method to get user's name
    def getName(self):
        return self.username

    # Method to publish a new post
    def publish_post(self, post_type, *args):
        # Notify followers about the new post
        message = f"{self.getName()} has a new post"
        self.notifyFollower(message)  # Triggering the notification process for the Observer pattern

        # Create the post using the post factory
        post = postFactory.create_post(post_type, self, *args)
        if post:
            self.posts.append(post)   # Add the post to the user's list of posts
            print(post)               # Print the post
            return post
