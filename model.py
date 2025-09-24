<<<<<<< HEAD

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
data = pd.read_csv('Crop_recommendation.csv')
X = data.iloc[:, :-1]
y = data.iloc[:, -1] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
pickle.dump(model, open("model.pkl", "wb"))
# Evaluate the model
# accuracy = model.score(X_test, y_test)
# print("Accuracy:", accuracy)

# Example usage: Predict crop for a new set of features
# new_features = [[117 ,32,34,26.2724184,52.12739421,6.758792552,127.1752928,]]
# predicted_crop = model.predict(new_features)
# print("Predicted crop:", predicted_crop)
=======

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
data = pd.read_csv('Crop_recommendation.csv')
X = data.iloc[:, :-1]
y = data.iloc[:, -1] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
pickle.dump(model, open("model.pkl", "wb"))
# Evaluate the model
# accuracy = model.score(X_test, y_test)
# print("Accuracy:", accuracy)

# Example usage: Predict crop for a new set of features
# new_features = [[117 ,32,34,26.2724184,52.12739421,6.758792552,127.1752928,]]
# predicted_crop = model.predict(new_features)
# print("Predicted crop:", predicted_crop)
>>>>>>> 2412f8fdbbeb80352994ecb1c9f6016f3ba4fc3d
