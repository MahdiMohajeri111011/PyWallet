from pywallet.infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher
from datetime import datetime

class Wallet :

    bcrypt_hasher = BcryptPasswordHasher()

    def __init__(
            self,
            wallet_id,
            name,
            password,
            descriptions = None
    ):

        self.wallet_id = wallet_id
        self.name = name
        self.__hashed_password = self.hash_password(password)
        self.descriptions = descriptions
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_active = True
        self.balance = 0


    def hash_password(self , password):
        hashed = Wallet.bcrypt_hasher.hash(password)
        result = (Wallet.bcrypt_hasher.verify(password , self.__hashed_password))
        if result :
            return hashed
        raise ValueError

    def deposit(self , amount):
        self.balance += amount

    def withdraw(self , amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True



