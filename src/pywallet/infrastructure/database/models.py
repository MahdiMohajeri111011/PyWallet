from sqlalchemy import String , Integer
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column

class ModelBase(DeclarativeBase) :
    pass

class UserModel(ModelBase) :

    __tablename__ = "users"

    id : Mapped[int] = mapped_column(Integer , primary_key=True , autoincrement=True)
    username : Mapped[str] = mapped_column(String(20) , unique=True)
    password : Mapped[str] = mapped_column(String(30))
    first_name : Mapped[str] = mapped_column(String , nullable=True)
    last_name : Mapped[str] = mapped_column(String , nullable=True)
    email : Mapped[str] = mapped_column(String , nullable=True)
    phone_number : Mapped[str] = mapped_column(String , nullable=True)
