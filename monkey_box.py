import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, KFold, GridSearchCV
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import RandomOverSampler
from keras.models import Sequential
from keras.layers import Dense, Input

# Load data
data = pd.read_csv('processed_data.txt')

# Split data into X and y
X = data.drop('MonkeyPox', axis=1)
y = data['MonkeyPox']

# Convert to int
X = X.astype('int')
y = y.astype('int')

# Over-sampling
ros = RandomOverSampler()
X_resampled, y_resampled = ros.fit_resample(X, y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

# Define the parameter grid
param_grid = {
    'alpha': [0.1, 0.5, 1.0, 2.0, 5.0],
    'fit_prior': [True, False],
}

# Perform grid search
grid_search = GridSearchCV(CategoricalNB(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Get the best model
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Backpropagation Neural Network and Feedforward Neural Network
model = Sequential()
model.add(Input(shape=(X_train.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=200, verbose=0, validation_data=(X_test, y_test))

y_pred_prob = model.predict(X_test)
y_pred_cnn = (y_pred_prob > 0.5).astype('int')

# Evaluate the model using cross-validation
kfold=KFold(n_splits=5, random_state=42, shuffle=True)
scores = cross_val_score(best_model, X_train, y_train, cv=kfold)
scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']

results = cross_validate(best_model, X_train, y_train, cv=kfold, scoring=scoring, return_train_score=False)

print("Accuracy for each fold:", results['test_accuracy'])
print("Precision for each fold:", results['test_precision_macro'])
print("Recall for each fold:", results['test_recall_macro'])
print("F1 Score for each fold:", results['test_f1_macro'])

y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred_cnn)
accuracy_nb = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(classification_report(y_test, y_pred_cnn))
print(classification_report(y_test, y_pred))

