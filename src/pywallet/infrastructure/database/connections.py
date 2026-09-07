import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()

class Singleton :
    instance = None

    def __new__(cls, *args , **kwargs):
        if not cls.instance :
            cls.instance = super().__new__(cls , *args , **kwargs)
        return cls.instance

class PostgresHandler(Singleton) :
    def __init__(
            self,
            name,
            user,
            host,
            password,
            port,
    ):
        self.name = name
        self.user = user
        self.host = host
        self.password = password
        self.port = port

db_1 = PostgresHandler(

    name = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    host = os.getenv("DB_HOST"),
    password = os.getenv("DB_PASSWORD"),
    port = os.getenv("DB_PORT")

)

DATABASE_URL = f"postgresql+psycopg://{db_1.user}:{db_1.password}@{db_1.host}:{db_1.port}/{db_1.name}"
engine = create_engine(DATABASE_URL, echo=True)