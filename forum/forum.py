__author__ = 'arobres'

from bottle import run, template, Bottle, request, response, auth_basic, redirect, static_file, TEMPLATE_PATH
from constants import THEME, SUBJECT, MESSAGES
from collections import defaultdict
import ujson
from sys import argv
import os

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))



app = Bottle()
user_list = []
USER_ATTRIBUTES = {'name', 'username', 'password', 'role', 'email'}
FORUM_ATTRIBUTES = {'theme', 'subject', 'message'}
ROLES = ['QA', 'DEVELOPER', 'MANAGER']
THEMES = ['Security', 'Development', 'Automation', 'Testing']
user_messages_dict = defaultdict(list)
forum_messages_dict = defaultdict(list)


def check_username(username, password):
    for user in user_list:
        if user['username'] == username:
            if user['password'] == password:
                return True
    return False




@app.get("/v1.0")
@app.get("/v1.0/")
def im_alive():

    output = template('welcome', first_time=True)
    return output


@app.get("/v1.0/reset")
@app.get("/v1.0/reset/")
def reset_data():
    del user_list[:]
    user_messages_dict.clear()
    forum_messages_dict.clear()


@app.post("/v1.0/users")
@app.post("/v1.0/users/")
def create_user():

    if request.POST.get('save','').strip():

        name = request.POST.get('name', '').strip()
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        role = request.POST.get('role', '').strip()
        email = request.POST.get('email', '').strip()

        if name == '' or username == '' or password == '' or role == '' or email == '':
            response.status = 400
            return {"message": "some parameter is not correct"}
        if role not in ROLES:
            response.status = 400
            return {"message": "Role not valid"}
        if find_user(username):
            response.status = 409
            return {"message": "User exist!"}
        else:
            body = create_body(name, username, password, role, email)
            user_list.append(body)
            redirect("/v1.0/users")


@app.get("/v1.0/users")
@app.get("/v1.0/users/")
def list_users():
    if len(user_list) == 0:
        return "No users created"
    else:
        output = template('user_list', rows=user_list)
        return output


@app.post("/v1.0/users/inbox/<username>")
@app.post("/v1.0/users/inbox/<username>/")
def create_user_message(username):

    body = "".join(request.body)
    try:
        body = ujson.loads(body)
    except:
        response.status = 400
        return {"message": "The JSON format is not correct"}

    user_exist = find_user(username=username)

    if not user_exist:
        response.status = 404
        return {"message": "The user not exists"}

    receiver_list = user_messages_dict[username]
    receiver_list.append(body)
    response.status = 200
    return 'message saved'


@app.get("/v1.0/users/inbox/<username>")
@app.get("/v1.0/users/inbox/<username>/")
@auth_basic(check_username)
def get_user_messages(username):

    receiver_list = user_messages_dict[username]
    return {"username": username, "messages": receiver_list}

@app.delete("/v1.0/users/inbox/<username>")
@app.delete("/v1.0/users/inbox/<username>/")
@auth_basic(check_username)
def delete_messages_from_user(username):

    del(user_messages_dict[username])
    return 'messages deleted'


@app.get("/v1.0/forum/new")
@app.get("/v1.0/forum/new/")
def publish_to_forum_html():
    return template('new_forum_message.tpl')


@app.get("/v1.0/users/new")
@app.get("/v1.0/users/new/")
def publish_to_forum_html():
    return template('new_user.tpl')



@app.post("/v1.0/forum")
@app.post("/v1.0/forum/")
def publish_to_forum():

    if request.POST.get('save','').strip():

        theme = request.POST.get('theme', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if theme == '' or subject == '' or message == '' :
            response.status = 400
            return {"message": "some parameter is not correct"}
        if theme not in THEMES:
            response.status = 400
            return {"message": "Theme not valid"}
        else:
            body = {THEME: theme, SUBJECT: subject, MESSAGES: message}
            forum_list = forum_messages_dict[body['theme']]
            forum_list.append(body)
            redirect('/v1.0/forum')


@app.get("/v1.0/forum")
@app.get("/v1.0/forum/")
def get_messages():

    theme_to_filter = request.query.getall('theme')

    if len(theme_to_filter) == 0:
        output = template('forum_messages_list', rows=forum_messages_dict)
        return output

    if len(theme_to_filter) == 1:

        message_list = forum_messages_dict[theme_to_filter[0]]
        output = template('forum_messages_list', rows={theme_to_filter[0]: message_list})
        return output


def find_user(username):

    for user in user_list:
        if user['username'] == username:
            return True

    return False


def check_user_body(body):
    count = 0
    for attribute in USER_ATTRIBUTES:

        if attribute not in body:
            return False
        else:
            count += 1
    if count != 5:
        return False
    else:
        return True


def check_forum_body(body):
    count = 0
    for attribute in FORUM_ATTRIBUTES:

        if attribute not in body:
            return False
        else:
            count +=1
    if count != 3:
        return False
    else:
        return True


def create_body(name=None, username=None, pwd=None, role=None, email=None):

        body = {}
        if name is not None:
            body['name'] = name
        if username is not None:
            body['username'] = username
        if pwd is not None:
            body['password'] = pwd
        if role is not None:
            body['role'] = role
        if email is not None:
            body['email'] = email

        return body


@app.route('/static/css/<filename>')
def cssget(filename):
    return static_file(filename, root="./static/css")


@app.route('/static/fonts/<filename>')
def fontsget(filename):
    return static_file(filename, root="./static/fonts")


run(app, host='0.0.0.0', port=argv[1], reloader=True)
