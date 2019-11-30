from bottle import route, run, template, get, post
import sqlalchemy as db
import getpass
import json
import pandas as pd

password = getpass.getpass("Insert your mysql root password: ")
engine = db.create_engine('mysql+pymysql://root:{}@localhost/api-project'.format(password))

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@get('idUser/<number>')
def querita(number):
    query = """
        SELECT * FROM messages WHERE idUser={}
    """.format(number)
    print("Running query")
    print(query)
    df= pd.read_sql_query(query, engine)
    jdaughter = df.to_json(orient='records')
    return json.dumps(jdaughter)

@post('/add/<jdaughter>')
def populatetable(jdaughter):
    query= "INSERT INTO {} VALUES {}"

    with engine.connect() as con:

        with open(jdaughter) as f:
            chats_json = json.load(f)
        
        users = list(set([(chats_json[i]['idUser'],chats_json[i]['userName']) for i in range(len(chats_json))]))
        chats = list(set([(chats_json[i]['idChat']) for i in range(len(chats_json))]))
        
        for user in users:
            q = query.format('users (idUser, userName)',"({}, '{}')".format(user[0],user[1]),'users.idUser')
            print(q)
            try:
                con.execute(q)
                #Get Response
                id = con.fetchone()[0]
                print(f"value inserted: {id}")
            except:
                print("At least I tried")

        for chat in chats:
            q = query.format('chats(idChat)',"({})".format(chat),'chats.idChat')
            print(q)
            try:
                con.execute(q)
                #Get Response
                id = con.fetchone()[0]
                print(f"value inserted: {id}")
            except:
                print("At least I tried")

        for message in chats_json:
            q = query.format('messages(idMessage, text, datetime, idUser, idChat)','({},"{}","{}",{},{})'.format(message['idMessage'],message['text'],message['datetime'],message['idUser'],message['idChat'],),'messages.idMessage')
            print(q)
            try:
                con.execute(q)
                #Get Response
                id = con.fetchone()[0]
                print(f"value inserted: {id}")
            except:
                print("At least I tried")
            
        return print('Done!')


run(host='localhost', port=8080)


