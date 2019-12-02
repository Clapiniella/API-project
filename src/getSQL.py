import sqlalchemy as db
import getpass
import json
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

#https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91

url= os.getenv('PASSWORD')
engine = db.create_engine(url)
connection = engine.raw_connection()
cursor = connection.cursor()


def getChatIdUser(number):
    query = """
        SELECT * FROM messages WHERE users_idUser={}
    """.format(number)
    print("Running query")
    print(query)
    df= pd.read_sql_query(query, engine)
    return df.to_json(orient='records')

def whoIdUser(number):
    query = """
        SELECT users.userName, COUNT(messages.idMessage) as TOTAL_MESSAGES
        from messages join
        users
        on messages.users_idUser = users.idUser
        WHERE messages.users_idUser = {}
        GROUP BY users.userName;
    """.format(number)
    df= pd.read_sql_query(query, engine)
    return df.to_json(orient='records')

def getMessages(chat_id):
    query = """
        SELECT text FROM messages WHERE chats_idChat='{}'
    """.format(chat_id)
    cursor.execute(query)
    return cursor.fetchall()

def newUser(name):
    query="""
        INSERT INTO project_api.users (userName) VALUES ('{}')
    """.format(name)
    cursor.execute(query) 
    query2="""
        SELECT idUser FROM project_api.users WHERE users.userName = '{}'
    """.format(name)
    cursor.execute(query2)
    return cursor.fetchall()

    

def newChat():
    with engine.connect() as conn:
        a=list(conn.execute("SELECT idChat FROM chats ORDER BY idChat DESC LIMIT 1"))
        new_chatId = a[0][0]+1
        print(new_chatId)
    new_chatque ="""
        INSERT INTO chats (idChat) VALUES ({})  
    """.format(new_chatId)
    cursor.execute(new_chatque)
    return {
            f'{new_chatId}': "You've succesfully created this chat"
        }

def newMessage(text,userid,chatid):
    query = """
        INSERT INTO messages (text, datetime, users_idUser, chats_idChat) 
        VALUES ('{}', CURRENT_TIMESTAMP, {}, {})
    """.format(text, userid, chatid)
    cursor.execute(query) 
    query2="""
        SELECT idMessage FROM project_api.messages WHERE messages.text = '{}'
    """.format(text)
    cursor.execute(query2)
    return cursor.fetchall()