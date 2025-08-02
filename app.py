import streamlit as st
import joblib
import numpy as np
import re

# -------------------------
# Feature Extraction Function
# -------------------------
def extract_features(url):
    features = {
        "url_length": len(url),
        "has_https": int("https" in url),
        "count_dots": url.count('.'),
        "has_at_symbol": int("@" in url),
        "contains_ip": int(bool(re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', url))),
        "has_prefix_suffix": int('-' in url),
        "count_digits": sum(c.isdigit() for c in url),
    }
    return features

# -------------------------
# Load the Model
# -------------------------
model = joblib.load("phishing_detector.pkl")

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="Phishing Detection Tool", page_icon="🛡️", layout="centered")
st.title("🛡️ Phishing URL Detection Tool")
st.markdown("Enter a URL below and find out if it's **Phishing** or **Legitimate**.")

# -------------------------
# URL Input
# -------------------------
url_input = st.text_input("🔗 Enter a URL", placeholder="https://example.com")

if url_input:
    # Extract features
    features = extract_features(url_input)
    input_vector = np.array(list(features.values())).reshape(1, -1)

    # Predict
    prediction = model.predict(input_vector)[0]

    # Result
    if prediction == 1:
        st.error("🚨 This URL is likely **PHISHING**.")
    else:
        st.success("✅ This URL appears **LEGITIMATE**.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Cyber Security Project")
