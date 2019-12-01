import sqlalchemy as db
import getpass
import json
import pandas as pd

#https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91

password = getpass.getpass("Insert your mysql root password: ")
engine = db.create_engine('mysql+pymysql://root:{}@localhost/api-project'.format(password))
print("Connected to server!")

def querita(number):
    query = """
        SELECT * FROM messages WHERE idUser={}
    """.format(number)
    print("Running query")
    print(query)
    df= pd.read_sql_query(query, engine)
    jdaughter = df.to_json(orient='records')
    return json.loads(jdaughter)
    
querita(8)


'''
password = getpass.getpass("Insert your mysql root password: ")
engine = db.create_engine('mysql+pymysql://root:{}@localhost/api-project'.format(password))
connection = engine.connect()
metadata = db.MetaData()
chat = db.Table('messages', metadata, autoload=True, autoload_with=engine)
query = db.select([chat])

ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()

print(ResultSet[:3],indent=4)


@post('/user/create')
def createUser():
    name = str(request.forms.get('name'))
    query=INSERT INTO project_api.users (userName) VALUES ({});
            SELECT idUser FROM project_api.users
            WHERE users.userName = {};
            .format(name,name)
    return query

'''