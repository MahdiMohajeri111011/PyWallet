from pywallet.domain.entities.user import User
from pywallet.domain.repositories.user_repository import UserRepository


class CreateUser :

    def __init__(self , user_repository : UserRepository):
        self.user_repository = user_repository

    def execute(
        self,
        username,
        password,
        firstname=None,
        lastname=None,
        email=None,
        phone_number=None,
    ):
        user = User(
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number
        )

        self.user_repository.save(user)

        return user
