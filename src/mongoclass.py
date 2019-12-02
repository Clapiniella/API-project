'''
def userRecommend(user_id):
    data = selectTables("users")
    print(data)
    docs = dict()
    for u in data:
        print(u[0])
        messages = userMessages(u[0])
        mestring = ' '.join([data for ele in messages for data in ele])
        docs.update({u[1]:mestring})
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(docs.values())
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, columns=count_vectorizer.get_feature_names(), index=docs.keys())
    similarity_matrix = distance(df, df)
    sim_df = pd.DataFrame(similarity_matrix, columns=docs.keys(), index=docs.keys())
    np.fill_diagonal(sim_df.values, 0) # Remove diagonal max values and set those to 0
    res = {'recommended_users': [e for e in list(sim_df[name].sort_values(ascending=False)[0:3].index)]}
    return res
    
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

@get('/chat/<chat_id>/list')
def queryMessages(chat_id):
    query = """
        SELECT text FROM messages WHERE chats_idChat='{}'
    """.format(chat_id)
    df = pd.read_sql_query(query, engine)
    jdaughter = df.to_json(orient='records')
    return json.dumps(jdaughter)
last="""
    SELECT idChat FROM chats ORDER BY idChat DESC LIMIT 1
    """
    cursor.execute(last)
    last_chatId = cursor.fetchall()
    new_chatId = last_chatId+1
    new_chatque ="""
        INSERT INTO chats (idChat) VALUES ({})  
    """.format(new_chatId)
    cursor.execute(new_chatque) 
    return cursor.fetchall()




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
'''