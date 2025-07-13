import streamlit as st
from crew.crew_setup import setup_crew
import os

st.title("💡 Product Idea Validator")
product_idea = st.text_area("Describe your product idea", value="AI personal assistant...")

if st.button("Generate Report"):
    crew = setup_crew(product_idea)
    with st.spinner("Generating..."):
        result = crew.kickoff()
        st.session_state['report'] = result

if 'report' in st.session_state:
    st.markdown("## 📄 Final Market Research Report")
    st.markdown(st.session_state['report'])
    
st.markdown(
    """
    <hr style="margin-top: 2rem;">
    <div style='text-align: center;'>
        Made with ❤️ by <a href='https://github.com/kethan52' target='_blank'>Kethan Pothula</a>
    </div>
    """,
    unsafe_allow_html=True
)

