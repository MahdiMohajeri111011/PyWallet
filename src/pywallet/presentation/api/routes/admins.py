from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path
from pywallet.presentation.api.schema.user import LoginUserRequest
from pywallet.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from pywallet.application.uses_case.user_login import LoginUser
BASE_PATH = Path(__file__).resolve().parents[3]
login_page_path = BASE_PATH / "gui" / "admin_panel" / "login_page" / "login.html"
home_page_path = BASE_PATH / "gui" / "admin_panel" / "home_page" / "home.html"
router = APIRouter()


@router.get("/admin/login")
def admin_login() :
    return FileResponse(login_page_path)

@router.post("/admin/login/auth")
def admin_login_auth(request : LoginUserRequest):
    sql_alchemy_repo = SqlAlchemyUserRepository()
    login_checker = LoginUser(sql_alchemy_repo)
    user = login_checker.execute(
        username = request.username,
        password = request.password
    )

    if user.is_super_user == True :
        return {
            "message": "Login successful"
        }


    return f'permission denied'

@router.get("/admin/home")
def admin_home() :
    return FileResponse(home_page_path)
