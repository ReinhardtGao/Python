from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
from sklearn.datasets import load_digits

#Prepare datasets
digits = load_digits()

#Got target datasets and labels
features = digits.data
labels = digits.target

#Select 20% of datasets to be the test sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=0)

#Create CART Tree
clf = DecisionTreeClassifier(criterion='gini')
clf = clf.fit(train_features, train_labels)

#Graphviz
dot_data = export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('Digits')

#Predict
test_predict = clf.predict(test_features)

#Compare train and test
score = accuracy_score(test_labels, test_predict)
print("CART accuracy_score is %.4lf" % score)
