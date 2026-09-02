from pywallet.infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher


class Wallet :

    password_hasher = BcryptPasswordHasher()

    def __init__(
        self,
        wallet_id,
        password,
        balance,
        name,
            ):

        self.wallet_id = wallet_id
        self.__password = password
        self.balance = balance
        self.name = name

    @classmethod
    def hash_password(cls , password):
        return cls.password_hasher.hash(password)

    @classmethod
    def check_password(cls , password):
        cls.password_hasher.verify(password)

    def change_name(self , new_name):
        self.name = new_name
        return new_name



