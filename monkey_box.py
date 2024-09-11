import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_validate, KFold
from sklearn.naive_bayes import CategoricalNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score

# Load data
data = pd.read_csv('processed_data.txt')
data_present = data[data['MonkeyPox'] == 1]
data_absent = data[data['MonkeyPox'] == 0]

# Define different sizes of training records
record_sizes = [120, 500, 1200]
accuracies_lr = []
accuracies_nb = []

for size in record_sizes:
    # Sample data
    data_present_sampled = data_present.sample(n=size//2, random_state=42)
    data_absent_sampled = data_absent.sample(n=size//2, random_state=42)

    balanced_data = pd.concat([data_present_sampled, data_absent_sampled])
    balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

    # Split data into X and y
    X = balanced_data.drop('MonkeyPox', axis=1)
    y = balanced_data['MonkeyPox']

    X = np.hstack((np.ones((X.shape[0], 1)), X))

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train logistic regression model
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)
    y_pred_lr = logreg.predict(X_test)
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    accuracies_lr.append(accuracy_lr)

    # Train Naive Bayes model
    nb_model = CategoricalNB()
    nb_model.fit(X_train, y_train)
    y_pred_nb = nb_model.predict(X_test)
    accuracy_nb = accuracy_score(y_test, y_pred_nb)
    accuracies_nb.append(accuracy_nb)

# Plot the accuracies for different record sizes
plt.figure(figsize=(10, 6))
plt.plot(record_sizes, accuracies_lr, marker='o', label='Logistic Regression')
plt.plot(record_sizes, accuracies_nb, marker='o', label='Naive Bayes')
plt.title('Accuracy vs. Number of Training Records')
plt.xlabel('Number of Training Records')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()

# Use the dataset with 120 records for confusion matrix, classification report, and ROC AUC
size = 120
data_present_sampled = data_present.sample(n=size//2, random_state=42)
data_absent_sampled = data_absent.sample(n=size//2, random_state=42)

balanced_data = pd.concat([data_present_sampled, data_absent_sampled])
balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Split data into X and y
X = balanced_data.drop('MonkeyPox', axis=1)
y = balanced_data['MonkeyPox']

X = np.hstack((np.ones((X.shape[0], 1)), X))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
logreg = LogisticRegression(max_iter=1000)
nb_model = CategoricalNB()

logreg.fit(X_train, y_train)
nb_model.fit(X_train, y_train)

# Predictions
y_pred_lr = logreg.predict(X_test)
y_pred_nb = nb_model.predict(X_test)

# Confusion matrices
confusion_matrix_lr = confusion_matrix(y_test, y_pred_lr)
confusion_matrix_nb = confusion_matrix(y_test, y_pred_nb)

# Calculate accuracy for the dataset with 120 records
accuracy_lr_120 = accuracy_score(y_test, y_pred_lr)
accuracy_nb_120 = accuracy_score(y_test, y_pred_nb)

# Print accuracy
print(f'Accuracy LR (120 records): {accuracy_lr_120}')
print(f'Accuracy NB (120 records): {accuracy_nb_120}')

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

# Calculate ROC AUC for both models
y_prob_lr = logreg.predict_proba(X_test)[:, 1]
y_prob_nb = nb_model.predict_proba(X_test)[:, 1]

fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
fpr_nb, tpr_nb, _ = roc_curve(y_test, y_prob_nb)

roc_auc_lr = roc_auc_score(y_test, y_prob_lr)
roc_auc_nb = roc_auc_score(y_test, y_prob_nb)

# Plot ROC curves
plt.figure(figsize=(10, 6))
plt.plot(fpr_lr, tpr_lr, label=f'Logistic Regression (AUC = {roc_auc_lr:.2f})')
plt.plot(fpr_nb, tpr_nb, label=f'Naive Bayes (AUC = {roc_auc_nb:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()