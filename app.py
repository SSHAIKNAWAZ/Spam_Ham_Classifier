import streamlit as st
import nltk
from nltk.corpus import  stopwords
from  nltk.stem.porter import  PorterStemmer
import  string
import pickle
ps=PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)



tfidf=pickle.load(open('vectorizer.pkl', 'rb'))
model=pickle.load(open('model.pkl','rb'))

st.title('Email/Sms Spam Classifer')

input_text=st.text_area('Enter The Message')

if st.button('Predict'):

    # preprocess
    transformed_sms = transform_text(input_text)
    # vectorize
    vector_input = tfidf.transform([transformed_sms])
    # predict
    result= model.predict(vector_input)[0]
    # display
    if result==1:
        st.header('Spam')
    else:
        st.header('Not Spam')