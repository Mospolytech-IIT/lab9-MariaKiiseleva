""" Модели базы данных """

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import  Column, Integer, String, Text, ForeignKey

from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase): pass

class User(Base):
    """ Модель пользователя """

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    posts = relationship('Post', back_populates='author')

class Post(Base):
    """ Модель поста """

    __tablename__ = "Posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("Users.id"))

    author = relationship('User', back_populates='posts')


class UserModel(BaseModel):
    """ Модель пользователя для создания нового """

    username: str
    email: str
    password: str

class UserUpdateModel(BaseModel):
    """ Модель пользователя для обновление существующего """

    id: int
    username: str
    email: str
    password: str

class UserDeleteModel(BaseModel):
    """ Модель пользователя для удаления """

    id: int

class PostModel(BaseModel):
    """ Модель поста для создания нового """

    title: str
    content: str
    user_id: int

class PostUpdateModel(BaseModel):
    """ Модель поста для обновления """
    id: int
    title: str
    content: str
    user_id: int

class PostDeleteModel(BaseModel):
    """ Модель поста для удаления """
    id: int

SessionLocal = sessionmaker(autoflush=False, bind=engine)
