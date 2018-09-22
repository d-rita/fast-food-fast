class User(object):
    """This class defines the instance of a User"""

    def __init__(self, userId, username, email, password, user_state):
        self.userId=userId
        self.username=username
        self.email=email
        self.password=password
        self.user_state=user_state

    def sign_up(self):
        pass

    def log_in(self):
        pass

    