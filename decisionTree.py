from sklearn import tree
import graphviz
import numpy as np

data = np.array([[1,1],[1,0],[0,1],[0,0]])
target = np.array([1,1,0,0])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data,target)

dot_data = tree.export_graphviz(clf,out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")
