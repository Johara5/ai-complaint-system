import streamlit as st
import google.generativeai as genai
import json

# Setup Gemini using Streamlit Secrets
genai.configure(api_key=st.secrets["AIzaSyDeksmMB5Q176tKR49Nfw8Jv65VPNb1Pg"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🛡️ AI Complaint Intelligence")

# Text input for the complaint
complaint_text = st.text_area("Paste the customer complaint here:", height=200)

if st.button("Analyze Complaint", type="primary"):
    if complaint_text:
        with st.spinner("Gemini is analyzing..."):
            prompt = f"""
            Analyze this complaint and return a JSON object with:
            Category, Priority (Critical/High/Medium/Low), Sentiment, Root_Cause, Recommended_Action, SLA.
            Text: {complaint_text}
            """
            response = model.generate_content(prompt)
            # Display results
            st.json(response.text)
    else:
        st.warning("Please paste a complaint first.")