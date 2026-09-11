from pywallet.domain.repositories.user_repository import UserRepository
from pywallet.domain.entities.user import User
from pywallet.infrastructure.database.models import UserModel
from pywallet.infrastructure.database.sessions import session1

class SqlAlchemyUserRepository(UserRepository) :

    def save(self , user : User):
        model = UserModel(
            username = user.username,
            password = user.show_hashed,
            first_name = user.firstname,
            last_name = user.lastname,
            email = user.email,
            phone_number = user.phone_number,
            created_at = user.created_at,
            updated_at = user.updated_at,
            is_active = user.is_active,
        )
        session1.add(model)
        session1.commit()
        session1.refresh(model)
        return model
    def find_by_id(self , user_id):
        pass

    def find_by_username(self , username):
        pass