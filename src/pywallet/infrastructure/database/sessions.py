from sqlalchemy.orm import sessionmaker
from pywallet.infrastructure.database.connections import engine

SessionLocal = sessionmaker(bind=engine)
session1 = SessionLocal()
