from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  # 75 % training, 25% testing
from sklearn.tree import DecisionTreeClassifier
import numpy as np

if __name__ == '__main__':
    iris_dataset = load_iris()
    print(type(iris_dataset.values()))
    # Random Dataset 75% training
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset.items(), iris_dataset.values(), random_state=0)
    print(type(y_test))
