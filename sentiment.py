import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import getSQL as sql

sid = SentimentIntensityAnalyzer()


def getSent(chats):
    analiza = ' '.join([word for frase in chats for word in frase])
    return sid.polarity_scores(analiza)

def chatSentiment(chat_id):
    chat=sql.getMessagesChat(chat_id)
    return getSent(chat)

def userSentiment(user_id):
    user=sql.getMessagesUser(user_id)
    return getSent(user)