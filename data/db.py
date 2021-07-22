HOST = 'enter your host here'
DATABASE = 'enter database here'
USER = 'enter user here'
PASSWORD = 'enter password here'

from sentiment import sentiment
import pandas as pd
import numpy as np
# !pip install mysql-connector-python
import mysql.connector as mysql

db_connection = mysql.connect(host=HOST,database = DATABASE, user = USER, password=PASSWORD)
print('Connected to:',db_connection.get_server_info())

cursor = db_connection.cursor(buffered=True)
d = dict()
cursor.execute('SELECT * FROM product;')
for i,data in enumerate(cursor):
    d[i] = data
product = pd.DataFrame(d).transpose()
product.columns = ['id','name','category','dom','doe']
product.to_csv('product.csv')
del product

d = dict()
cursor.execute('SELECT * FROM validation;')
for i,data in enumerate(cursor):
    d[i] = data
validation = pd.DataFrame(d).transpose()
validation.columns = ['id','lat','long','time']
validation.to_csv('validation.csv')
del validation

d = dict()
cursor.execute('SELECT * FROM feedback;')
for i,data in enumerate(cursor):
    d[i] = data
feedback = pd.DataFrame(d).transpose()
feedback.columns = ['id','feedback','lat','long','score','time']

temp = []
for i in feedback['feedback']:
    temp.append(sentiment(i))
feedback = pd.DataFrame(temp,columns=['sentiment','confidence']).join(feedback)
feedback['sent_value'] = np.where(feedback['sentiment'] == 'pos',1,-1)
feedback.to_csv('feedback.csv')
del feedback

d = dict()
cursor.execute('SELECT * FROM complain;')
for i,data in enumerate(cursor):
    d[i] = data
complain = pd.DataFrame(d).transpose()
complain.columns = ['id','complain','n_revalid','lat','long','time']
temp = []
for i in complain['complain']:
    temp.append(sentiment(i))

complain = pd.DataFrame(temp,columns=['sentiment','confidence']).join(complain)
complain['confidence'] = complain['confidence']*100
complain['sent_value'] = np.where(complain['sentiment'] == 'pos',1,-1)
complain.to_csv('complain.csv')
del complain


db_connection.commit()
cursor.close()
db_connection.close()