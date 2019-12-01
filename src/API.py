from bottle import route, run, template, get, post, request
import sqlalchemy as db
import getpass
import json
import pandas as pd
import requests

password = getpass.getpass("Insert your mysql root password: ")
engine = db.create_engine('mysql+pymysql://root:{}@localhost/project_api'.format(password))


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@get('/idUser/<number>')
def querita(number):
    query = """
        SELECT * FROM messages WHERE users_idUser={}
    """.format(number)
    print("Running query")
    print(query)
    df= pd.read_sql_query(query, engine)
    jdaughter = df.to_json(orient='records')
    return json.dumps(jdaughter)

@get('/mensajes/<number>')
def querito(number):
    query = """
        SELECT users.userName, COUNT(messages.idMessage) as TOTAL_MESSAGES
        from messages join
        users
        on messages.idUser = users.idUser
        WHERE messages.idUser = {}
        GROUP BY users.userName;
    """.format(number)
    df= pd.read_sql_query(query, engine)
    jdaughter = df.to_json(orient='records')
    return json.dumps(jdaughter)

@get('/chat/<chat_id>/list')
def queryMessages(chat_id):
    query = """
        SELECT text FROM messages WHERE chats_idChat='{}'
    """.format(chat_id)
    df = pd.read_sql_query(query, engine)
    jdaughter = df.to_json(orient='records')
    return json.dumps(jdaughter)

@get('/user/create')
def insertName():
    return '''<form method="POST" action="/user/create">
            Insert a new name: <input name="name"     type="text" />
            <input type="submit" />
              </form>'''

@post('/user/create')
def newUser():  
    name = str(request.forms.get('name'))
    with engine.connect() as conn: 
        query="""
            INSERT INTO project_api.users (userName) VALUES ('{}')  
        """.format(name)
        conn.execute(query) 
    with engine.connect() as conn:
        query2="""
            SELECT idUser FROM project_api.users WHERE users.userName = '{}'
        """.format(name)
        dfi= pd.read_sql_query(query2, engine)
        jdaughter = dfi.to_json(orient='records')
    return json.dumps(jdaughter)


@post('/create/chat')
def newChat():  
    with engine.connect() as conn:
        a=list(conn.execute("SELECT idChat FROM chats ORDER BY idChat DESC LIMIT 1"))
        new_chatId = a[0][0]+1
    with engine.connect() as conn:
        new_chatque ="""
            INSERT INTO chats (idChat) VALUES ({})  
        """.format(new_chatId)
        conn.execute(new_chatque) 
    return {
            f'{new_chatId}': "You've succesfully created this chat"
        }

@get('/chat/addmessage')
def insertChat():
    return '''<form method="POST" action="/chat/addmessage">
            Insert a new message: <input name="text"  type="text" />
            Insert an existing chat: <input name="chatid"  type="number" />
            Insert an existing user: <input name="userid"  type="number" />
            <input type="submit" />
              </form>'''

@post('/chat/addmessage')
def newMessage():
    text = str(request.forms.get('text'))
    print(text)
    chatid = request.forms.get('chatid')
    print(chatid)
    userid = request.forms.get('userid')
    print(userid)
    with engine.connect() as conn:
        query = """
        INSERT INTO messages (text, datetime, users_idUser, chats_idChat) 
        VALUES ('{}', CURRENT_TIMESTAMP, {}, {})
        """.format(text, userid, chatid)
        conn.execute(query) 
    with engine.connect() as conn:
        query2="""
            SELECT idMessage FROM project_api.messages WHERE messages.text = '{}'
        """.format(text)
        dfo= pd.read_sql_query(query2, engine)
        jdaughter = dfo.to_json(orient='records')
    return json.dumps(jdaughter)


run(host='localhost', port=8080)