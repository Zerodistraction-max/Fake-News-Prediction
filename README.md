# Fake-News-Prediction
The Fake News Prediction project uses machine learning to classify news as real or fake. It includes data preprocessing, TF-IDF vectorization, and model training with Logistic Regression. A web app is also implemented using Streamlit, allowing users to input news text and get instant authenticity predictions. 


The Fake News Prediction project is a machine learning-based solution designed to classify news articles as either real or fake. In today's digital age, misinformation spreads rapidly, and detecting fake news has become a crucial challenge. This project aims to address that issue by using Natural Language Processing (NLP) and classification algorithms to build an automated detection system.

The process begins with collecting and preprocessing a labeled dataset containing both fake and real news articles. Preprocessing steps include cleaning the text data by removing punctuation, converting all characters to lowercase, eliminating stop words, and performing stemming or lemmatization to standardize the text. These steps help prepare the raw news content for meaningful analysis.

Next, the cleaned data is transformed into numerical format using **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization. This technique assigns weights to words based on their frequency in a document relative to their frequency across all documents, allowing the model to focus on terms that are more informative.

For classification, the project utilizes **Logistic Regression**, a reliable and interpretable algorithm suited for binary classification tasks. The model is trained on the vectorized data and evaluated using metrics like accuracy, precision, recall, F1-score, and confusion matrix to assess its performance and ensure robustness.

To make the system interactive and user-friendly, a **Streamlit web application** has been implemented. This web interface allows users to input any news article or headline, and with a single click, receive a real-time prediction on whether the news is real or fake. The integration of Streamlit not only enhances accessibility but also showcases the practical application of machine learning in a real-world scenario.

Overall, the Fake News Prediction project combines data science, NLP, and web deployment to deliver a complete end-to-end solution. It provides users with an easy-to-use tool that promotes awareness, helps verify news credibility, and encourages responsible information sharing. The project can be extended further using deep learning models or larger datasets to improve accuracy and handle more complex linguistic patterns.
