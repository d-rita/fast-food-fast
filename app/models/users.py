class User(object):
    """This class defines a User model"""

    def __init__(self, userId, username, email, password, user_state):
        """Initialises user attributes"""
        self.userId=userId
        self.username=username
        self.email=email
        self.password=password
        self.user_state=user_state

    
    