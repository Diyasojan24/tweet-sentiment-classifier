import streamlit as st
import joblib

@st.cache_resource
def load_model():
    return joblib.load(r"E:\projects\tweet-sentiment-classifier\models\tweet_sentiment_nb_model.joblib")

model = load_model()

def predict_sentiment(text):
    if isinstance(text, str):
        return model.predict([text])[0]
    else:
        return model.predict(text)

st.title("Tweet Sentiment Classifier")

st.write("Type a tweet and get a predicted sentiment (negative, neutral, positive).")

user_input = st.text_area("Enter tweet text here:", "")

if st.button("Predict sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        pred = predict_sentiment(user_input)
        st.success(f"Predicted sentiment: **{pred}**")
