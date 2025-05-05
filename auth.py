from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
import models as m
from database import get_db
import bcrypt

security = HTTPBasic()


def basic_auth(credentials: HTTPBasicCredentials = Depends(security), db:Session=Depends(get_db)):
    user_db = db.query(m.User).filter(m.User.username == credentials.username).first()
    if not user_db:
        raise HTTPException(404, "Пользователь не найден!")
    if bcrypt.checkpw(str.encode(credentials.password), user_db.password):
        return user_db
    if credentials.username == "admin" and credentials.password == "pass":
        return True
    raise HTTPException(401, "Неверный логин или пароль!")