import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns               

from sklearn.model_selection import train_test_split, cross_validate, KFold
from sklearn.naive_bayes import CategoricalNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load data
data = pd.read_csv('processed_data.txt')
data_present = data[data['MonkeyPox'] == 1]
data_absent = data[data['MonkeyPox'] == 0]

data_present_sampled = data_present.sample(n=60, random_state=42)
data_absent_sampled = data_absent.sample(n=60, random_state=42)

balanced_data = pd.concat([data_present_sampled, data_absent_sampled])
balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Split data into X and y
X = balanced_data.drop('MonkeyPox', axis=1)
y = balanced_data['MonkeyPox']

X = np.hstack((np.ones((X.shape[0], 1)), X))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logreg = LogisticRegression()
nb_model = CategoricalNB()

nb_model.fit(X_train, y_train)
logreg.fit(X_train, y_train)

# Evaluate the model using cross-validation
kfold=KFold(n_splits=5, random_state=42, shuffle=True)
scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
results = cross_validate(nb_model, X_train, y_train, cv=kfold, scoring=scoring, return_train_score=False)

print("Accuracy for each fold:", results['test_accuracy'])
print("Precision for each fold:", results['test_precision_macro'])
print("Recall for each fold:", results['test_recall_macro'])
print("F1 Score for each fold:", results['test_f1_macro'])

# Predictions
y_pred_nb = nb_model.predict(X_test)
y_pred_lr = logreg.predict(X_test)

accuracy_nb = accuracy_score(y_test, y_pred_nb)
accuracy_lr = accuracy_score(y_test, y_pred_lr)

confusion_matrix_lr = confusion_matrix(y_test, y_pred_lr)
confusion_matrix_nb = confusion_matrix(y_test, y_pred_nb)

# Deep Learning
print(f'Accuracy NB: {accuracy_nb}')
print(f'Accuracy LR: {accuracy_lr}')

# Classification report
print("Classification Report NB:")
print(classification_report(y_test, y_pred_nb))
print("Classification Report LR:")
print(classification_report(y_test, y_pred_lr))

# Plot confusion matrices side by side
fig, axes = plt.subplots(1, 2, figsize=(20, 7))

sns.heatmap(confusion_matrix_lr, annot=True, fmt='d', ax=axes[0], cmap='Blues')
axes[0].set_title('Confusion Matrix LR')
axes[0].set_xlabel('Predicted')
axes[0].set_ylabel('Actual')

sns.heatmap(confusion_matrix_nb, annot=True, fmt='d', ax=axes[1], cmap='Blues')
axes[1].set_title('Confusion Matrix NB')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')

plt.show()