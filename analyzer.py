import requests
import streamlit as st
from urllib.parse import urlparse

# Known phishing domains (Can be expanded or integrated with external APIs)
PHISHING_DOMAINS = ["malicious-site.com", "fake-bank-login.net", "phishing-example.org"]

# Function to analyze link security
def analyze_link(url):
    parsed_url = urlparse(url)
    
    # Security check
    security_status = "✅ Secure (HTTPS)" if parsed_url.scheme == "https" else "⚠️ Not Secure (HTTP)"
    
    # Phishing detection
    domain = parsed_url.netloc
    phishing_warning = "❌ Potential Phishing Site!" if domain in PHISHING_DOMAINS else "✅ Safe Domain"
    
    # Check HTTP status
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
    except requests.exceptions.RequestException:
        status_code = "🚫 Unable to reach URL"

    return {
        "URL": url,
        "Security Status": security_status,
        "HTTP Status Code": status_code,
        "Phishing Status": phishing_warning
    }

# Streamlit Dashboard Setup
st.title("🔗 Link Analyzer")
st.write("Check URLs for security status, HTTP codes, and phishing risks.")

# Input for batch link checking
urls = st.text_area("Enter URLs (one per line)", "").split("\n")
if st.button("Analyze Links"):
    if urls:
        results = [analyze_link(url.strip()) for url in urls if url.strip()]
        for result in results:
            st.write(result)
    else:
        st.warning("Please enter at least one valid URL.")
