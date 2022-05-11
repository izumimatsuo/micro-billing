import os
import tempfile
import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from main import app
from app.database import Base
from app.repositories import session


with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


def override_session():
    db_fd, db_path = tempfile.mkstemp()
    SQLALCHEMY_DATABASE_URL = "sqlite:///" + db_path

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    try:
        db = TestingSessionLocal()
        sql = ""
        for line in _data_sql:
            if not line.startswith("--") and line.strip("\n"):
                sql += line.strip("\n")
                if sql.endswith(";"):
                    try:
                        db.execute(sql)
                        db.commit()
                    except Exception as e:
                        print(e)
                    finally:
                        sql = ""
        yield db
    finally:
        db.close()
        os.close(db_fd)
        os.unlink(db_path)


@pytest.fixture
def client():
    app.dependency_overrides[session] = override_session
    return TestClient(app)
