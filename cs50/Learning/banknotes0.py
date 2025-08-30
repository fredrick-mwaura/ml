import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron #classification and regression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np


# CSV = pd.read_csv('banknotes.csv')

# df = CSV.head()
# print(df)

# model = Perceptron()
model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()

# Read data in from file
""" 
banknotes.csv file link:
https://drive.google.com/file/d/1E_fsyWYk9sRxDSkRVy0SlDMczs6XklO8/view?usp=sharing
"""
with open("banknotes.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    # print(next(reader))
    next(reader) #skip header row

    data = []
    for row in reader:
        # print(row)
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })

# Separate data into training and testing groups
holdout = int(0.50 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

# Train model on training set
X_training = [row["evidence"] for row in training]
y_training = [row["label"] for row in training]
model.fit(X_training, y_training)

# Make predictions on the testing set
X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)

# Compute how well we performed
correct = 0
incorrect = 0
total = 0
for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")
