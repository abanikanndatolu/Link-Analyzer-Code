## 📌 Project Overview
This **enhanced Link Analyzer** checks URLs for security risks, HTTP status codes, phishing threats, and provides a **Streamlit dashboard** for easy analysis.

## 🚀 Features
- ✅ Detects whether a URL uses **HTTPS** for security.
- ❌ Flags **potential phishing domains**.
- 🔄 Supports **batch link analysis**.
- 🌐 Interactive **Streamlit dashboard** for visualization.


## 🛠️ Installation & Usage
### **Prerequisites**
- Python 3.x installed.
- Install dependencies:
  ```bash
  pip install requests streamlit
  streamlit run analyzer.py


Enter a URL to analyze: https://example.com
🔍 Link Analysis Result:
URL: https://example.com
Security Status: ✅ Secure (HTTPS)
HTTP Status Code: 200
Phishing Status: ✅ Safe Domain
