from abc import ABC , abstractmethod
from pywallet.domain.entities.user import User
from pywallet.infrastructure.database.models import UserModel
from pywallet.infrastructure.database.sessions import session1


class UserRepository(ABC) :

    @abstractmethod
    def find_by_username(self , username):
        pass

    @abstractmethod
    def find_by_id(self , user_id):
        pass

    @abstractmethod
    def save(self , user : User):
        pass

    



