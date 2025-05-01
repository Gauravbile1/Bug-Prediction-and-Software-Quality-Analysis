import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Load the preprocessed data
data = pd.read_csv(r"C:\Users\Gaurav Bile\Videos\1Study\SKY internship\Bug Prediction and Software Quality Analysis\synthetic_bug_prediction_data.csv")


# Check if the dataset is empty
if data.empty:
    print("The dataset is empty. Please check the preprocessing step.")
else:
    print(f"Dataset shape: {data.shape}")
    print("First few rows of the dataset:")
    print(data.head())

    # Handle missing values by filling NaN with empty strings
    data['title'] = data['title'].fillna('')
    data['body'] = data['body'].fillna('')
    data['message'] = data['message'].fillna('')

    # Combine text columns ('title', 'body', 'message') into a single feature
    data['text'] = data['title'] + ' ' + data['body'] + ' ' + data['message']

    # Drop original text columns as we now have the combined text column
    X = data['text']  # Features
    y = data['label']  # Target
  # Target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize the TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')

    # Fit and transform the training data, and transform the test data
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Initialize and train the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_tfidf, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test_tfidf)

    # Evaluate the model
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # Save the trained model and vectorizer for future use
# Save the model
with open(r"C:\Users\Gaurav Bile\Videos\1Study\SKY internship\Bug Prediction and Software Quality Analysis\bug_prediction_model.pkl", 'wb') as f:
    pickle.dump(model, f)

# Save the vectorizer
with open(r"C:\Users\Gaurav Bile\Videos\1Study\SKY internship\Bug Prediction and Software Quality Analysis\vectorizer.pkl", 'wb') as f:
    pickle.dump(vectorizer, f)


    print("Model and vectorizer saved to bug_prediction_model.pkl and vectorizer.pkl")
