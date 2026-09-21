from fastapi import APIRouter
from pywallet.application.uses_case.user_craete import CreateUser
from pywallet.application.uses_case.user_login import LoginUser
from pywallet.presentation.api.schema.user import CreateUserRequest, LoginUserRequest
from pywallet.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from pywallet.infrastructure.security.jwt_handler import create_access_token , create_refresh_token

router = APIRouter()


@router.post("/user")
def create_user(request : CreateUserRequest) :

    sqlalchemy_repo = SqlAlchemyUserRepository()
    user_creator = CreateUser(sqlalchemy_repo)
    user = user_creator.execute(
        username=request.username,
        password=request.password,
        firstname=request.first_name,
        lastname=request.last_name,
        email=request.email,
        phone_number=request.phone_number,
    )

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return {
        "message" : "User created",
        "access token" : access_token,
        "refresh token" : refresh_token,
        "username" : request.username
    }

@router.post("/login")
def login_user(request : LoginUserRequest) :
    sqlalchemy_repo = SqlAlchemyUserRepository()
    login_check = LoginUser(sqlalchemy_repo)
    user = login_check.execute(
        username = request.username,
        password = request.password
    )

    access_token = create_access_token(user.username)
    refresh_token = create_refresh_token(user.username)

    return {

        "message" : "login was successful",
        "username" : request.username,
        "access token" : access_token,
        "refresh token": refresh_token,

    }

@router.get("/user_create")
def test_user_create() :
    return {"kir" : "kir"}