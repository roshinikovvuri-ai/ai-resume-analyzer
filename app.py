import streamlit as st
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

resume_text = st.text_area("Paste Your Resume")

if st.button("Analyze Resume"):

    if resume_text:

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(resume_text)

            st.write(result)

    else:
        st.warning("Please paste your resume.")