from user import *

class UserManager():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_accounts = {}

    def load_users():
        pass

    def save_users():
        pass

    def validate_username():
        pass

    def validate_password():
        pass

    def register():
        while True:
            try:
                username = input ("Enter your desired Username (Must be 4 characters): ")
                if not username:
                    return
                elif username < 4:
                    print ("Username must be 4 characters long")
                else: 
                    password = input ("Enter your desired Password (Must be 8 characters): ")
                    if not password:
                        return
                    elif password < 8:
                        print ("Password must be 8 characters long")
                    else:
                        self.username.User(username, password)
            except ValueError as e:
                print (f"An error occures: {e}")
                        
                        

    def login():
        pass