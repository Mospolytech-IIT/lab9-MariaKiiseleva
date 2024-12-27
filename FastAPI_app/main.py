""" Сервер """

# uvicorn main:app --reload

from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    """ Зависимость для БД """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/users")
def get_users(db: Session = Depends(get_db)):
    """ Получение всех пользователей """
    return db.query(User).all()


@app.post("/api/user/add")
def add_user(data: UserModel, db: Session = Depends(get_db)):
    """ Добавление пользователя """
    user = User(username=data.username, email=data.email, password=data.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return "Пользователь добавлен"


@app.put("/api/user/update")
def update_user(data: UserUpdateModel, db: Session = Depends(get_db)):
    """ Обновление пользователя """
    user = db.query(User).filter(User.id == data.id).first()
    user.username = data.username
    user.email = data.email
    user.password = data.password
    db.commit()
    db.refresh(user)
    return "Пользователь изменен"


@app.delete("/api/user/delete")
def delete_user(data: UserDeleteModel, db: Session = Depends(get_db)):
    """ Удаление пользователя """
    user = db.query(User).filter(User.id == data.id).first()
    db.delete(user)
    db.commit()
    return "Пользователь удалён"


@app.get("/api/posts")
def get_posts(db: Session = Depends(get_db)):
    """ Получение всех постов """
    return db.query(Post).all()


@app.post("/api/post/add")
def add_posts(data: PostModel, db: Session = Depends(get_db)):
    """ Создание поста """
    post = Post(title=data.title, content=data.content, user_id=data.user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return "Пост добавлен"


@app.put("/api/post/update")
def update_posts(data: PostUpdateModel, db: Session = Depends(get_db)):
    """ Обновление постов """
    post = db.query(Post).filter(Post.id == data.id).first()
    post.title = data.title
    post.content = data.content
    post.user_id = data.user_id
    db.commit()
    db.refresh(post)
    return "Пост изменён"


@app.delete("/api/post/delete")
def delete_posts(data: UserDeleteModel, db: Session = Depends(get_db)):
    """ Удаление поста """
    post = db.query(Post).filter(Post.id == data.id).first()
    db.delete(post)
    db.commit()
    return "Пост удалён"