import pandas as pd
import sqlalchemy as db
import getpass
import json

password = getpass.getpass("Insert your mysql root password: ")
engine = db.create_engine('mysql+pymysql://root:{}@localhost/project_api'.format(password))
print("Connected to server!")

def populatetable(jdaughter):
    query= "INSERT INTO {} VALUES {}"

    with engine.connect() as con:

        with open(jdaughter) as f:
            chats_json = json.load(f)
        
        users = list(set([(chats_json[i]['idUser'],chats_json[i]['userName']) for i in range(len(chats_json))]))
        chats = list(set([(chats_json[i]['idChat']) for i in range(len(chats_json))]))
        
        for user in users:
            q = query.format('users (userName)',"('{}')".format(user[1]),'users.idUser')
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
            q = query.format('messages(text, datetime, users_idUser, chats_idChat)','("{}","{}",{},{})'.format(message['text'],message['datetime'],message['idUser'],message['idChat'],),'messages.idMessage')
            print(q)
            try:
                con.execute(q)
                id = con.fetchone()[0]
                print(f"value inserted: {id}")
            except:
                print("At least I tried")
          
        return print('Done!')

populatetable('./INPUT/chats_bike.json')


