from fastapi import APIRouter
from pywallet.application.uses_case.user_craete import CreateUser
from pywallet.presentation.api.schema.user import CreateUserRequest
from pywallet.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository

router = APIRouter()
@router.post("/user")
def create_user(request : CreateUserRequest) :

    sqlalchemy_repo = SqlAlchemyUserRepository()
    user_creator = CreateUser(sqlalchemy_repo)
    user_creator.execute(
        username=request.username,
        password=request.password,
        firstname=request.first_name,
        lastname=request.last_name,
        email=request.email,
        phone_number=request.phone_number
    )

    return {
        "message" : "request was successful",
        "username" : request.username
    }
