import numpy as np
import pickle
import streamlit as st
# Load the trained model and vectorizer
model = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Fake news Prediction project/trained_model.sav', 'rb'))
vectorizer = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Fake news Prediction project/vectoriser.sav', 'rb'))
#creating a function for prediction
def fake_news_prediction(news_text):
        # Transform the text input using the loaded vectorizer
    X_new = vectorizer.transform([news_text])

    # Predict using the trained model
    prediction = model.predict(X_new)
    print(prediction)

    # Output result
    if prediction[0] == 0:
        return 'The news is Real'
    else:
        return 'The news is Fake'
def main():
    st.title('Fake news predictor')
    news_text= st.text_input('Enter the text')
    
    diagnosis=''
    if st.button('show result'):
        diagnosis= fake_news_prediction(news_text)
    
    st.success(diagnosis)
if __name__=='__main__':
    main()        

