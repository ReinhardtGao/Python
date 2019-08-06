import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import export_graphviz
import graphviz
#Load Data
train_data = pd.read_csv('./Titanic_Data/train.csv')
test_data = pd.read_csv('./Titanic_Data/test.csv')
#Go thru Data
print(train_data.info())
print('-'*30)
print(train_data.describe())
print('-'*30)
#print(train_data.describe(include=['0']))
#print('-'*30)
print(train_data.head())
print('-'*30)
print(train_data.tail())
#Fill in NaN
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)
#Select features
features = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
#Build up ID3 tree
clf = DecisionTreeClassifier(criterion='entropy')
#Train
clf.fit(train_features, train_labels)
#Test and estimate
test_features = dvec.transform(test_features.to_dict(orient='record'))
#Predict
pred_labels = clf.predict(test_features)
#Accuracy
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'Score Accuracy is %.4lf' % acc_decision_tree)
#K-Cross Verification
print(u'Score Accuracy is %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))
#Visualization
dot_data = export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('TitanicData')
