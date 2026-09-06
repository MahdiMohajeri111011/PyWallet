from abc import ABC , abstractmethod
from pywallet.domain.entities.user import User

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

