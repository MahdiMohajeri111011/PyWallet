from datetime import datetime
import json
import re
from pywallet.infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher

class User :

    bcrypt_hasher = BcryptPasswordHasher()
    EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    PHONE_NUMBER_PATTERN = r'09[0-9]{9}$'
    USERNAME_PATTERN = r'^[0-9A-Za-z_]{9,20}$'

    def __init__(
            self,
            username : str,
            password : str,
            firstname : str = None,
            lastname : str = None,
            email : str = None,
            phone_number : str = None,
    ):

        User.username_validator(username)
        if email :
            User.email_validator(email)
        if phone_number :
            User.phone_number_validator(phone_number)


        self.username = username
        self.__hashed_password = self.hash_password(password)
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_active = True
        self.check_password(password)


    def hash_password(self , input_password):
        result = User.bcrypt_hasher.hash(password=input_password)
        self.__hashed_password = result
        return result

    def check_password(self, input_password):
        return User.bcrypt_hasher.verify(input_password , self.__hashed_password)

    @property
    def show_hashed(self):
        return self.__hashed_password

    @staticmethod
    def email_validator(input_email):
        if re.match(User.EMAIL_PATTERN , input_email) is None :
            raise ValueError()
        return True
        
    @staticmethod
    def phone_number_validator(input_phone_number):
        if re.match(User.PHONE_NUMBER_PATTERN , input_phone_number) is None:
            raise ValueError()
        return True

    @staticmethod
    def username_validator(input_username):
        if re.match(User.USERNAME_PATTERN , input_username) is None :
            raise ValueError()
        return True

    def change_phone_number(self , new_phone_number):
        valid = self.phone_number_validator(new_phone_number)
        if valid :
            self.phone_number = new_phone_number

    def change_email(self , new_email):
        valid = self.email_validator(new_email)
        if valid :
            self.email = new_email

    def change_username(self , new_username):
        self.username = new_username

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def status(self):
        return self.is_active

    def to_json(self):
        return json.dumps({
            'username' : self.username,
        },indent=2)

    def  __str__(self) :
        return self.username


user1 = User(
    username='Mahdi',
    password='sibzamini8145'
)
print(user1.to_json())
