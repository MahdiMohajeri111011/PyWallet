from fastapi import APIRouter
from pywallet.presentation.api.schema.user import LoginUserRequest
from pywallet.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
router = APIRouter()

@router.get("/admin/login")
def admin_login() :
    return f'Login page will be here'

@router.post("/admin/login/auth")
def admin_login_auth(request : LoginUserRequest):
    sql_alchemy_repo = SqlAlchemyUserRepository()
    user = sql_alchemy_repo.find_by_username(request.username)

    if user.is_super_user == True :
        return {
            "message" : "Login successful",
            "username" : user.username
        }
