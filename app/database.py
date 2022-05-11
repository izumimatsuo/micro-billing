import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

INSTANCE_PATH = os.path.join(os.getcwd(), "instance")
SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(INSTANCE_PATH, "billing.sqlite")

try:
    os.makedirs(INSTANCE_PATH)
except OSError:
    pass

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
