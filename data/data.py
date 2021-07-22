# from sentiment import sentiment
import pandas as pd
import nltk
# nltk.download('punkt')
# print(sentiment('trash'))

def product():
    product = pd.read_csv('product.csv')
    del product['Unnamed: 0']
    return product
def validation():
    validation = pd.read_csv('product.csv')
    del validation['Unnamed: 0']
    return validation
def feedback():
    feedback = pd.read_csv('product.csv')
    del feedback['Unnamed: 0']
    return feedback
def complain():
    complain = pd.read_csv('product.csv')
    del complain['Unnamed: 0']
    return complain

