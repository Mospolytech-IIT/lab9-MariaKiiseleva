""" Лабораторная работа 9 """

from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

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

Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

user1 = User(username="username1", email="email1", password="pass1")
user2 = User(username="username2", email="email2", password="pass2")
user3 = User(username="username3", email="email3", password="pass3")

# db.add(user1)
db.add_all([user1, user2, user3])
db.commit()

post1 = Post(title="post1", content="content1", user_id=1)
post2 = Post(title="post2", content="content2", user_id=2)
post3 = Post(title="post3", content="content3", user_id=3)
post4 = Post(title="post4", content="content4", user_id=1)

db.add_all([post1, post2, post3, post4])
db.commit()

users = db.query(User).all()
for user in users:
    print(f"{user.id} {user.username} {user.email} {user.password}")

results = db.query(Post, User).join(User, User.id == Post.user_id).all()
for post, user in results:
    print(f"{post.id} {post.title} {post.content} {post.user_id} {user.id} {user.username} {user.email}")

posts = db.query(Post).where(Post.user_id == 1).all()
for post in posts:
    print(f"{post.id} {post.title} {post.content}")

target_user = db.query(User).filter(User.id == 3).first()
target_user.email = "email3"
db.commit()
print(target_user.email)
target_user.email = "email99"
db.commit()
target_user = db.query(User).filter(User.id == 3).first()
print(target_user.email)

target_post = db.query(Post).filter(Post.user_id == 2).first()
target_post.content = "content2"
db.commit()
print(target_post.content)
target_post.content = "content992419"
db.commit()
target_post = db.query(Post).filter(Post.user_id == 2).first()
print(target_post.content)

del_post = db.query(Post).filter(Post.id == 3).first()
db.delete(del_post)
db.commit()

del_user = db.query(User).filter(User.username == "username1").first()
posts = del_user.posts
for post in posts:
    db.delete(post)
db.delete(del_user)
db.commit()


app = FastAPI()
