# -*- coding: utf-8 -*-
"""
Created on Thu May  7 01:27:00 2020

@author: rrite
"""
#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the dataset
dataset = pd.read_csv('iris.data', header = None)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

#Encoding Categorial Data
from sklearn.preprocessing import LabelEncoder
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

#Splitting the data set into Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#Applying knn algorithm to the problem of Iris flower Classification
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
print(Y_pred)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))