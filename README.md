# 🛡️ Phishing URL Detection Tool

A lightweight machine learning project to detect phishing URLs using handcrafted features and a Random Forest classifier. This tool includes a training script, a command-line interface (CLI) for quick testing, and a clean Streamlit-based web application for real-time URL checking.


## ✅ Overview

This project focuses on detecting phishing URLs by analyzing key characteristics of a URL string (like length, presence of IPs, number of dots, etc.) and classifying them using a supervised learning approach.

Phishing websites often use deceptive URLs to trick users into providing sensitive data. This tool helps identify such malicious links before they can cause harm.

---

## 🧱 System Architecture

```plaintext
+-------------------+       +------------------------+       +------------------+
|   Raw URL Input   | --->  |   Feature Extraction   | --->  |  ML Classifier   |
+-------------------+       +------------------------+       +------------------+
                                   |                                    |
                                   |                                    v
                          +------------------+                 +--------------------+
                          |  Numeric Feature |                 | Prediction Result  |
                          |    Vector (X)    |                 | (Phishing/Legit)   |
                          +------------------+                 +--------------------+

```


---

## 🧰 Tech Stack

| Component       | Technology               |
|----------------|--------------------------|
| Language        | Python 3.x               |
| ML Model        | Random Forest Classifier |
| Data Handling   | Pandas, NumPy            |
| Model Storage   | Joblib                   |
| Web App         | Streamlit                |
| Regex Parsing   | re (Regular Expressions) |

---

## 🚀 Features

- ✅ CLI-based URL phishing checker (via terminal)  
- 🌐 Real-time web app with Streamlit interface  
- 🧠 Feature extraction from URLs:  
  - URL length  
  - Use of HTTPS  
  - Number of dots  
  - Presence of IP addresses  
  - Use of special symbols (`@`, `-`)  
  - Digit count  
- 📦 Trained and saved ML model (`.pkl`)  
- 🎯 Clean and intuitive UI for end users  

---

## 🧩 Installation

### Step 1: Clone the repository
```
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
```
### Step 2: Create a virtual environment (optional but recommended)
```
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Linux/Mac:
source venv/bin/activate

```

### Step 3: Install dependencies
```
pip install -r requirements.txt

```

## ▶️ How to Use
🔧 Model Training (Optional)
Use this step only if you want to retrain the model with your own dataset.
```
python phishing_detection_tool.py
```
🌐 Run Web App (Streamlit)
```
streamlit run app.py
```
🖥️ CLI Prediction (Optional)
```
python phishing_detection_tool.py
```
Then input a URL when prompted to check its legitimacy.

## 📁 Project Structure
```
phishing-url-detector/
│
├── app.py / phy.py               # Streamlit UI for real-time prediction
├── phishing_detection_tool.py    # Model training + CLI interface
├── phishing_detector.pkl         # Saved ML model
├── phishing_site_urls.csv        # Dataset (URLs with labels)
├── requirements.txt              # Dependencies
└── README.md                     # Project Documentation
```
## Dataset
The model is trained on a dataset (phishing_site_urls.csv) containing URLs labeled as:

1 → Phishing

0 → Legitimate

Each URL undergoes custom feature extraction before being used to train a Random Forest classifier.

📌 If you're using a private dataset, please mention that users must supply their own.

## Future Improvements
Here are some ways to enhance the project:

### 🔍 Advanced Feature Extraction
Add lexical analysis, WHOIS data, domain age, SSL certificate status, etc.

### 🔬 Deep Learning Approaches
Experiment with LSTM or CNN models on raw URL data.

### 🌍 Live Threat Intelligence APIs
Integrate with APIs like VirusTotal, Google Safe Browsing, or PhishTank.

### 🧩 Browser Extension
Build a Chrome or Firefox extension using the backend model.

### 📊 Logging & Analytics Dashboard
Track predictions and visualize phishing attempts over time.

### ☁️ Cloud Deployment
Deploy the model and web app using Heroku, Streamlit Cloud, or AWS Lambda.

---

🙌 Credits
Made with ❤️ by Faheem
Cybersecurity Enthusiast | Python Developer

✅ You can copy and paste this entire block directly into your `README.md` file.
```

Let me know if you'd like me to create the corresponding `LICENSE` file or `requirements.txt` too.

```
