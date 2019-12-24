from sklearn import svm
import pandas as pd

#Load Data
data = pd.read_csv("/Users/jgao-mdp/PycharmProjects/Python/breast_cancer_data-master/data.csv")
pd.set_option('display.max_columns', None)
print(data.columns)
print(data.head(5))
print(data.describe())

##Data Clean##
#Split features into 3 groups
features_mean = list(data.columns[2:12])
features_se = list(data.columns[12:22])
features_worst = list(data.columns[22:32])
data.drop("id",axis=1,inplace=True)
data['diagnosis']=data['diagnosis']
