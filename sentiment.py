#Part 2 - use the trained algos and generated data directly
import nltk,random,pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers = classifiers
    
    def classify(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    #how much % of algos are confident | 4/5 = 80% of algos are confident
    def confidence(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

documents_ = open('data/models/documents.pickle','rb')
documents = pickle.load(documents_)
documents_.close()

word_features_ = open('data/models/word_features5k.pickle','rb')
word_features = pickle.load(word_features_)
word_features_.close()

def find_features(document):
    words = word_tokenize(document)  
    features = {}
    for w in word_features:
        features[w] = (w in words)
    
    return features

classifier_ = open('data/models/classifier.pickle','rb')
classifier = pickle.load(classifier_)
classifier_.close()

MultinomialNB_classifier_ = open('data/models/MultinomialNB_classifier.pickle','rb')
MultinomialNB_classifier = pickle.load(MultinomialNB_classifier_)
MultinomialNB_classifier_.close()

BernoulliNB_classifier_ = open('data/models/BernoulliNB_classifier.pickle','rb')
BernoulliNB_classifier = pickle.load(BernoulliNB_classifier_)
BernoulliNB_classifier_.close()

LogisticRegression_classifier_ = open('data/models/LogisticRegression_classifier.pickle','rb')
LogisticRegression_classifier = pickle.load(LogisticRegression_classifier_)
LogisticRegression_classifier_.close()

SGDClassifier_classifier_ = open('data/models/SGDClassifier_classifier.pickle','rb')
SGDClassifier_classifier = pickle.load(SGDClassifier_classifier_)
SGDClassifier_classifier_.close()

LinearSVC_classifier_ = open('data/models/LinearSVC_classifier.pickle','rb')
LinearSVC_classifier = pickle.load(LinearSVC_classifier_)
LinearSVC_classifier_.close()


voted_classifier = VoteClassifier(classifier,
                                  MultinomialNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  SGDClassifier_classifier,
                                #   SVC_classifier,
                                  LinearSVC_classifier)

def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
