import streamlit as st
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Set Streamlit page config
st.set_page_config(page_title="Bug Prediction App", layout="wide")

# Load model and vectorizer
model_path = "C:/Users/Gaurav Bile/Videos/1Study/SKY internship/Bug Prediction and Software Quality Analysis/bug_prediction_model.pkl"
vectorizer_path = "C:/Users/Gaurav Bile/Videos/1Study/SKY internship/Bug Prediction and Software Quality Analysis/vectorizer.pkl"

try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    with open(vectorizer_path, 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)

    model_loaded = True
except FileNotFoundError:
    st.error("❌ Model or vectorizer file not found!")
    model_loaded = False

# Page Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🛠️ Bug Prediction and Software Quality Analysis</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.header("📊 Model Info")
st.sidebar.success("✅ Accuracy: 100% (on current dataset)")

st.sidebar.markdown("---")
st.sidebar.header("ℹ️ About This Project")
st.sidebar.markdown("""
This project helps developers identify whether a commit message or issue report is likely to be a **bug** or **not**.

**Input Format:**
- 📝 Title: Short summary of the issue/commit
- 📄 Body: Description/details
- 💬 Message: Actual commit or bug message

The model uses Natural Language Processing to analyze the input and predicts if it's likely to be a bug.

---

### 🔎 Examples:
- **Example 1 (Bug)**  
  - Title: `Fix null pointer exception in login module`  
  - Body: `App crashes when username field is left empty.`  
  - Message: `[BUGFIX] Handle null values in login.`  
  - ✅ Prediction: **Bug**

- **Example 2 (Not a Bug)**  
  - Title: `Add dark mode toggle`  
  - Body: `Implemented feature to toggle between light and dark theme.`  
  - Message: `[FEATURE] Added user preference for dark mode.`  
  - ✅ Prediction: **Not a Bug**
""")

# Main App
if model_loaded:
    st.subheader("🔍 Predict if your input relates to a Bug")
    col1, col2 = st.columns(2)

    with col1:
        title = st.text_input("Enter Title", "")
        body = st.text_area("Enter Body", height=150)
        message = st.text_area("Enter Commit/Bug Message", height=150)

        if st.button("Predict"):
            combined_text = title + " " + body + " " + message
            vectorized_input = vectorizer.transform([combined_text])
            prediction = model.predict(vectorized_input)[0]

            if prediction == 1:
                st.error("🪲 This is likely a **BUG** 🐞")
            else:
                st.success("✅ This is **NOT a Bug**")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2210/2210153.png", width=300)
        st.caption("Bug Detection powered by ML and NLP 🧠")

