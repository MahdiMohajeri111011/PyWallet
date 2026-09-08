from sqlalchemy import String , Integer , TIMESTAMP , Boolean
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column
from datetime import datetime

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
    created_at : Mapped[datetime] = mapped_column(TIMESTAMP , default = datetime.now)
    updated_at : Mapped[datetime] = mapped_column(TIMESTAMP , default= datetime.now , onupdate=datetime.now)
    is_active : Mapped[bool] = mapped_column(Boolean , default=True)