from fastapi import FastAPI, HTTPException, Response, Request, Form, status, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional
from collections import defaultdict
import uvicorn
from enum import Enum
import os


# Models
class Role(str, Enum):
    QA = "QA"
    DEVELOPER = "DEVELOPER"
    MANAGER = "MANAGER"


class Theme(str, Enum):
    SECURITY = "Security"
    DEVELOPMENT = "Development"
    AUTOMATION = "Automation"
    TESTING = "Testing"


class User(BaseModel):
    name: str
    username: str
    password: str
    role: Role
    email: EmailStr


class Message(BaseModel):
    content: dict


class ForumMessage(BaseModel):
    theme: Theme
    subject: str
    message: str


# App initialization
app = FastAPI(title="Forum API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "forum"))
templates.env.file_extension = '.tpl'


# Configuración de archivos estáticos
app.mount("/static", StaticFiles(directory="forum/static"), name="static")

# Storage (in memory)
user_list: List[Dict] = []
user_messages_dict: Dict = defaultdict(list)
forum_messages_dict: Dict = defaultdict(list)


# Helper functions
def check_username(username: str, password: str) -> bool:
    return any(
        user["username"] == username and user["password"] == password
        for user in user_list
    )


def find_user(username: str) -> bool:
    return any(user["username"] == username for user in user_list)


# Routes
@app.get("/v1.0", response_class=HTMLResponse)
@app.get("/v1.0/", response_class=HTMLResponse)
async def im_alive(request: Request):
    return templates.TemplateResponse(
        "welcome.tpl",
        {"request": request, "first_time": True}
    )


@app.get("/v1.0/reset")
async def reset_data():
    user_list.clear()
    user_messages_dict.clear()
    forum_messages_dict.clear()
    return {"message": "Data reset successful"}


@app.post("/v1.0/users", status_code=status.HTTP_201_CREATED)
async def create_user(
        name: str = Form(...),
        username: str = Form(...),
        password: str = Form(...),
        role: Role = Form(...),
        email: EmailStr = Form(...)
):
    if find_user(username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

    user = {
        "name": name,
        "username": username,
        "password": password,
        "role": role,
        "email": email
    }
    user_list.append(user)
    return RedirectResponse(
        url="/v1.0/users",
        status_code=status.HTTP_303_SEE_OTHER
    )


@app.get("/v1.0/users", response_class=HTMLResponse)
async def list_users(request: Request):
    return templates.TemplateResponse(
        "user_list.tpl",
        {"request": request, "rows": user_list}
    )


@app.post("/v1.0/users/inbox/{username}")
async def create_user_message(username: str, message: Message):
    if not find_user(username):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user_messages_dict[username].append(message.content)
    return {"message": "Message saved"}


@app.get("/v1.0/users/inbox/{username}")
async def get_user_messages(
        username: str,
        user_cookie: Optional[str] = Cookie(None)
):
    if not user_cookie:
        return RedirectResponse(
            url="/v1.0/login",
            status_code=status.HTTP_303_SEE_OTHER
        )

    if not check_username(username, user_cookie[::-1]):
        return RedirectResponse(
            url="/v1.0/login",
            status_code=status.HTTP_303_SEE_OTHER
        )

    return {
        "username": username,
        "messages": user_messages_dict[username]
    }


@app.delete("/v1.0/users/inbox/{username}")
async def delete_messages_from_user(username: str):
    if username in user_messages_dict:
        del user_messages_dict[username]
    return {"message": "Messages deleted"}


@app.get("/v1.0/forum/new", response_class=HTMLResponse)
async def publish_to_forum_html(request: Request):
    return templates.TemplateResponse(
        "new_forum_message.tpl",
        {"request": request}
    )


@app.get("/v1.0/users/new", response_class=HTMLResponse)
async def new_user_form(request: Request):
    return templates.TemplateResponse(
        "new_user.tpl",
        {"request": request}
    )


@app.post("/v1.0/forum")
async def publish_to_forum(forum_message: ForumMessage):
    forum_messages_dict[forum_message.theme].append(forum_message.dict())
    return RedirectResponse(
        url="/v1.0/forum",
        status_code=status.HTTP_303_SEE_OTHER
    )


@app.get("/v1.0/forum", response_class=HTMLResponse)
async def get_messages(
        request: Request,
        theme: Optional[Theme] = None
):
    if not forum_messages_dict:
        return "No forum messages"

    messages = (
        {theme: forum_messages_dict[theme]}
        if theme
        else forum_messages_dict
    )

    return templates.TemplateResponse(
        "forum_messages_list.tpl",
        {"request": request, "rows": messages}
    )


@app.get("/v1.0/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.tpl",
        {"request": request}
    )


@app.post("/v1.0/login")
async def user_login(
        response: Response,
        username: str = Form(...),
        password: str = Form(...)
):
    if not check_username(username, password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid username or password"
        )

    response.set_cookie(key="username", value=username[::-1])
    return RedirectResponse(
        url=f"/v1.0/users/inbox/{username}",
        status_code=status.HTTP_303_SEE_OTHER
    )

@app.get("/v1.0/demo", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "demoweb.tpl",
        {"request": request}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)