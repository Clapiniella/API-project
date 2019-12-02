import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
import seaborn as sns
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import getSQL as sql

def getPhrase(chats):
    analiza = ' '.join([word for frase in chats for word in frase])
    return analiza


def makeDict():
    users= list(sql.getUsers())
    usernames=[]
    for u in users:
        usernames.append(u[1])
    usersid=[]
    for u in users:
        usersid.append(u[0])
    whattheysaid=[]
    for i in usersid:
        whattheysaid.append(sql.getChatIdUser(i))
    otherlist=[]
    for e in whattheysaid:
        otherlist.append(getPhrase(e))
    docs={}
    for i,nombre in enumerate(usernames): 
        docs[nombre]= otherlist[i]
    return docs


def recommendator(name):
    count_vectorizer = CountVectorizer(stop_words='english')
    sparse_matrix = count_vectorizer.fit_transform(makeDict().values())
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, columns=count_vectorizer.get_feature_names(), index=makeDict().keys())
    similarity_matrix = distance(df, df)
    sim_df = pd.DataFrame(similarity_matrix, columns=makeDict().keys(), index=makeDict().keys())
    np.fill_diagonal(sim_df.values, 0) 
    pepe = sim_df.idxmax()
    dict45825121={}
    dict45825121[name]= 'Your best friend should be {}'.format(pepe.loc[name])
    return dict45825121
