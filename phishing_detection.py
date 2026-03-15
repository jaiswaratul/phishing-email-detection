import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("phishing_email.csv")

X = data["text_combined"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))


# Test with custom email
email = ["Verify your account immediately to avoid suspension"]

email_vector = vectorizer.transform(email)

prediction = model.predict(email_vector)

if prediction[0] == 1:
    print("This email is likely PHISHING")
else:
    print("This email is likely LEGITIMATE")

    # Test the model with a new email
email = ["support@microsoft.com"]

email_vector = vectorizer.transform(email)

prediction = model.predict(email_vector)

if prediction[0] == 1:
    print("Prediction: PHISHING EMAIL")
else:
    print("Prediction: LEGITIMATE EMAIL")

    Import text processing tool
    import re
    creating text cleaning function
    def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

cleaning to dataset
data["text_combined"] = data["text_combined"].apply(clean_text)