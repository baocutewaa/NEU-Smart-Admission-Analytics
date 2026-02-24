from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Format: mysql+pymysql://user:password@host/db_name
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:NHẬP_PASS_VÀO_ĐÂY@localhost/NHẬP_TÊN_DB_VÀO_ĐÂY")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency để inject vào Router
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
