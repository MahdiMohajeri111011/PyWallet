from pywallet.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from pywallet.infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher

class LoginUser :

    def __init__(self , user_repository : SqlAlchemyUserRepository):
        self.user_repository = user_repository

    def execute(
            self,
            username,
            password
    ):

        if "@" in username :
            user = self.user_repository.find_by_email(username)
        else :
            user = self.user_repository.find_by_username(username)

        if user is None :
            raise Exception("Invalid username or password")

        hasher = BcryptPasswordHasher()
        if not hasher.verify(password , user.password) :
            raise Exception("Invalid username or password")

        return user