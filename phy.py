# phishing_detection_tool.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import re

# -------------------------
# 1. Feature Extraction
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
# 2. Load Dataset
# -------------------------
print("[+] Loading dataset...")
# Replace with your dataset path
df = pd.read_csv("phishing_site_urls.csv")

# Normalize column names (force to lowercase & remove spaces)
df.columns = df.columns.str.strip().str.lower()
print("CSV columns:", df.columns)
feature_list = []
# Now use lowercase names
for url in df["url"]:
    feature_list.append(extract_features(url)) # type: ignore

features_df = pd.DataFrame(feature_list) # type: ignore
features_df['label'] = df['label']  # 1 = Phishing, 0 = Legitimate

# -------------------------
# 3. Train/Test Split
# -------------------------
X = features_df.drop("label", axis=1)
y = features_df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------
# 4. Train Model
# -------------------------
print("[+] Training model...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# -------------------------
# 5. Evaluate Model
# -------------------------
print("[+] Evaluating model...")
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -------------------------
# 6. Save Model
# -------------------------
joblib.dump(model, "phishing_detector.pkl")
print("[+] Model saved as phishing_detector.pkl")

# -------------------------
# 7. Predict from User Input
# -------------------------
while True:
    print("\n🔗 Enter a URL to check if it's phishing (or type 'exit' to quit):")
    user_url = input("URL: ")

    if user_url.lower() == 'exit':
        break

    user_features = extract_features(user_url)
    input_features = np.array(list(user_features.values())).reshape(1, -1)
    prediction = model.predict(input_features)[0]

    if prediction == 1:
        print("🚨 This URL is likely **PHISHING**.")
    else:
        print("✅ This URL appears **LEGITIMATE**.")
