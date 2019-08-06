import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import os

LABEL_MAP = {'体育': 0, '女性': 1, '文学': 2, '校园': 3}
#Load Stop_words
with open('./text_classification-master/text_classification/stop/stopword.txt', 'r', encoding='utf-8') as f:
    Stop_words = [line.strip() for line in f.readlines()]

#Load data
def load_data(base_path):
    documents = []
    labels = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            label = root.split('/')[-1]
            labels.append(LABEL_MAP[label])
            filename = os.path.join(root, file)
            with open(filename, 'rb') as f:
                content = f.read()
                word_list = list(jieba.cut(content))
                words = [wl for wl in word_list]
                documents.append(''.join(words))
    return documents, labels

def train_fun(traind, trainl, testd, testl):
    traint = TfidfVectorizer(stop_words = Stop_words, max_df=0.5)
    trainf = traint.fit_transform(traind)
    clf = MultinomialNB(alpha=0.001).fit(trainf, trainl)
    test_tf = TfidfVectorizer(stop_words=Stop_words, max_df=0.5, vocabulary=traint.vocabulary_)
    test_features = test_tf.fit_transform(testd)
    predicted_labels = clf.predict(test_features)
    x = metrics.accuracy_score(testl, predicted_labels)
    return x


train_documents, train_labels = load_data('./text_classification-master/text_classification/train')
test_documents, test_labels = load_data('./text_classification-master/text_classification/test')
y = train_fun(train_documents, train_labels, test_documents, test_labels)
print(y)
