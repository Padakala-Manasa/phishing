import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import tldextract
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the training data
data = [
    ("https://movie-rulz.com", "Phishing"),
    ("https://www.disneyplus.com", "Phishing"),
    ("https://netflix.com", "Legitimate"),
    ("https://solarmovie.to", "Phishing"),
    ("https://google.com", "Legitimate"),
    ("https://facebook.com", "Legitimate"),
    ("https://twitter.com", "Legitimate"),
    ("https://instagram.com", "Legitimate"),
    ("https://youtube.com", "Legitimate"),
]

# Preprocess the data
urls, labels = zip(*data)
urls = [tldextract.extract(url).registered_domain for url in urls]
labels = [1 if label == "Phishing" else 0 for label in labels]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(urls, labels, test_size=0.2, random_state=42)

# Create a vectorizer and fit it to the training data
vectorizer = CountVectorizer(analyzer="char", ngram_range=(3, 5))
X_train_vectorized = vectorizer.fit_transform(X_train)

# Create a classifier and train it on the training data
model = RandomForestClassifier(random_state=42)
model.fit(X_train_vectorized, y_train)

# Evaluate the model on the testing data
X_test_vectorized = vectorizer.transform(X_test)
y_pred = model.predict(X_test_vectorized)
accuracy = model.score(X_test_vectorized, y_test)

# Log the accuracy
logging.info(f"Model accuracy: {accuracy:.2f}")

# Save the model and vectorizer to files
with open("./backend/models/model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
with open("./backend/models/vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

logging.info("Model and vectorizer saved successfully!")