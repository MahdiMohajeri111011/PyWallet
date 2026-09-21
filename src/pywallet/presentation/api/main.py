from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pywallet.presentation.api.routes.users import router as user_router
from pywallet.presentation.api.routes.admins import router as admin_router
app = FastAPI(
    title="PyWallet",
    version="1.0.0"
)

#-----------routers------------
app.include_router(user_router)
app.include_router(admin_router)

#-----------config static files----------

app.mount("/admin/static" , StaticFiles(directory="pywallet/gui/admin_panel/login_page"))


