import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("phishing_email.csv")

X = data["text_combined"]
y = data["label"]

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

st.title("Phishing Email Detection Tool")

email_text = st.text_area("Paste email text here")

if st.button("Check Email"):
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        st.error("⚠️ This email looks like PHISHING")
    else:
        st.success("✅ This email looks LEGITIMATE")
        domain = email_text.split("@")[-1]
    if "rnicrosoft" in email_text or "paypa1" in email_text:
     st.error("⚠️ Suspicious domain detected")