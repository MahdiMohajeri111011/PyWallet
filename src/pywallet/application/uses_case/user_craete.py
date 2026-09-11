from pywallet.domain.entities.user import User
from pywallet.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository


class CreateUser :

    def __init__(self , user_repository : SqlAlchemyUserRepository):
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
