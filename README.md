# API-project

The goal of this project is to analyze the conversations of my team to ensure they are happy 😃

**Main goal**: Analyze the conversations coming from a chat like `slack`

# How ?

- (L1🧐) Writing an API in bottle just to store chat messages in mysql

x-special/nautilus-clipboard
copy
file:///home/clara/Desktop/Ironhack/Projects/instrucciones-API/remote_dbs/Screenshot%20from%202019-11-29%2009-22-44.png


- (L2🥳) Extracting sentiment from chat messages and perform a report over a whole conversation

- (L4🤭) Recommending friends to a user based on the contents from chat `documents` using a recommender system with `NLP` analysis

- (L3😎) Creating an image of the API with docker

# API endpoints

  #### @route('/hello/<name>')
    
    - Gives you the chance to say hello to your own self, very useful if you are just testing the API works 
 
  #### @get('/idUser/user')
    
    - Returns every user in DB, UserId and their names
  
  #### @get('/idUser/<number>')
    
    - Returns every message a user has sent, given an UserId
  
  #### @get('/mensajes/<number>')
    
    - Returns the user name and how many messages has ever sent, given an UserId
  
  #### @get('/chat/<chat_id>/list')
  
    - Returns a list of all the messages in a chat, given an ChatId
 
  #### @post('/user/create')
  
    - Create a user and save into DB
    - Returns the UserId
    
   **Params:** `UserName` 
  
  #### @post('/create/chat')
  
    - Create a conversation in the DB, to load messages
    - Returns the ChatId
  
  #### @post('/chat/addmessage')
  
    - Add a message to an existing conversation into DB
    - Returns the MessageId
    
   **Params:** `Text`, `ChatId` and `UserId`
  
  #### @get('/user/<user_id>/sentiment')
  
    - Returns a JSON array with the results of analyzing all messages from a User, given a UserId
    
   `{'neg': 0.1, 'neu': 0.776, 'pos': 0.125, 'compound': 0.501}` used `nltk` for this task
  
  
  #### @get('/chat/<chat_id>/sentiment')
    
    - Returns a JSON array with the results of analyzing all messages from a Chat, given a ChatId
    
   `{'neg': 0.209, 'neu': 0.69, 'pos': 0.101, 'compound': -0.834}` used `nltk` for this task
  
  #### @get('/findafriend/<name>')
  
    - Given a UserName, it recommends you a friend based on similarities with other Chat's users
   
   Used `Sklearn` for this task
  
 
  
  ## Links - API dev in python

- [https://bottlepy.org/docs/dev/]

- [https://www.getpostman.com/]


  ## Links - NLP & Text Sentiment Analysis

- [https://www.nltk.org/]

- [https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]

- [https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]


  # Links - Heroku & Docker & Cloud Databases

- [https://docs.docker.com/engine/reference/builder/]

- [https://runnable.com/docker/python/dockerize-your-python-application]

- [https://devcenter.heroku.com/articles/container-registry-and-runtime]

- [https://devcenter.heroku.com/categories/deploying-with-docker]

- MySQL ClearDB [https://devcenter.heroku.com/articles/cleardb]
