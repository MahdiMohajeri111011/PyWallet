from pydantic import BaseModel

class CreateUserRequest(BaseModel) :
    username : str
    password : str
    first_name : str | None
    last_name : str | None
    email : str | None
    phone_number : str | None