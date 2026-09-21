from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path
from pywallet.presentation.api.schema.user import LoginUserRequest
from pywallet.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from pywallet.application.uses_case.user_login import LoginUser
BASE_PATH = Path(__file__).resolve().parents[3]
login_page_path = BASE_PATH / "gui" / "admin_panel" / "login_page" / "login.html"
router = APIRouter()


@router.get("/admin/login")
def admin_login() :
    return FileResponse(login_page_path)

@router.post("/admin/login/auth")
def admin_login_auth(request : LoginUserRequest):
    sql_alchemy_repo = SqlAlchemyUserRepository()
    user = login_check = LoginUser(sql_alchemy_repo)
    login_check.execute(
        username = request.username,
        password = request.password
    )

    if user.is_super_user == True :

        return {
            "message" : "Login successful",
            "username" : user.username
        }
    return f'permission denied'
