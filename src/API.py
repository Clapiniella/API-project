from bottle import route, run, template, get, post, request
import sqlalchemy as db
import getpass
import json
import pandas as pd
import requests
import mysql.connector
import getSQL as sql
import sentiment as sen

'''
password = getpass.getpass("Insert your mysql root password: ")
engine = db.create_engine('mysql+pymysql://root:{}@localhost/project_api'.format(password))
connection = engine.raw_connection()
cursor = connection.cursor()
'''
   
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@get('/idUser/<number>')
def querita(number):
    chats_idUser= sql.getChatIdUser(number)
    return json.dumps(chats_idUser)


@get('/mensajes/<number>')
def querito(number):
    whothe= sql.whoIdUser(number)
    return json.dumps(whothe)

@get('/chat/<chat_id>/list')
def queryMessages(chat_id):
    re_rows=sql.getMessages(chat_id)
    return json.dumps(re_rows)


@get('/chat/<chat_id>/sentiment')
def querySenti(chat_id):
    sentimi = sen.chatSentiment(chat_id)
    return json.dumps(sentimi)

@get('/user/create')
def insertName():
    return '''<form method="POST" action="/user/create">
            Insert a new name: <input name="name"     type="text" />
            <input type="submit" />
              </form>'''

@post('/user/create')
def createUser():  
    name = str(request.forms.get('name'))
    newUs = sql.newUser(name)
    return json.dumps(newUs)


@post('/create/chat')
def createChat():  
    chatid = sql.newChat()
    return json.dumps(chatid)


@get('/chat/addmessage')
def insertChat():
    return '''<form method="POST" action="/chat/addmessage">
            Insert a new message: <input name="text"  type="text" />
            Insert an existing chat: <input name="chatid"  type="number" />
            Insert an existing user: <input name="userid"  type="number" />
            <input type="submit" />
              </form>'''

@post('/chat/addmessage')
def createMessage():
    text = str(request.forms.get('text'))
    chatid = request.forms.get('chatid')
    userid = request.forms.get('userid')
    newMes= sql.newMessage(text, chatid, userid)
    return json.dumps(newMes)
  


run(host='localhost', port=8080)