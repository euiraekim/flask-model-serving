from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

iris = datasets.load_iris()
x = iris.data
y = iris.target
print(x,y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

pipeline = Pipeline([('std', StandardScaler()), ('lr', LogisticRegression())])
pipeline.fit(x_train, y_train)

pred = pipeline.predict(x_test)

print(f'Accuracy : {accuracy_score(y_test, pred)}')

file_name = 'model.pkl'
joblib.dump(pipeline, file_name)
print('Model saved.')