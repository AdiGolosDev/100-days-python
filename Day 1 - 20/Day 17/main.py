class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
        print("A new user is being created") # runs every time a User object is created

    def follow(self, user):
        user.followers += 1
        self.following += 1
    

user1 = User("222", "klokan")

print(user1.username)

user2 = User("22", "TheFool")

user1.follow(user2)

print(user1.following)