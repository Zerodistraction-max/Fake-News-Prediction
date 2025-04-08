# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 02:37:42 2025
@author: Asus
"""

import numpy as np
import pickle

# Load the trained model and vectorizer
model = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Fake news Prediction project/trained_model.sav', 'rb'))
vectorizer = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Fake news Prediction project/vectoriser.sav', 'rb'))

# Example news input (you can replace this with user input or test data)
news_text = "Breaking: Government confirms increase in minimum wage starting next month."

# Transform the text input using the loaded vectorizer
X_new = vectorizer.transform([news_text])

# Predict using the trained model
prediction = model.predict(X_new)
print(prediction)

# Output result
if prediction[0] == 0:
    print('The news is Real')
else:
    print('The news is Fake')
