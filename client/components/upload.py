import streamlit as st
from utils.api import upload_pdfs_api

def render_uploader():
    st.sidebar.header("📁 Upload Documents (.PDFs)")
    with st.sidebar.container():
        st.markdown(
            """
            <style>
            .stFileUploader > div > div {
                background: rgba(255,255,255,0.2) !important;
                border-radius: 10px !important;
                border: 1px solid rgba(255,255,255,0.3) !important;
                padding: 15px !important;
            }
            .stFileUploader label {
                color: white !important;
                font-weight: 500 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        uploaded_files = st.file_uploader(
            "Upload multiple PDFs",
            type="pdf",
            accept_multiple_files=True,
            help="Select documents in PDF format"
        )
        
        if st.button("📤 Upload to Database", key="upload_btn") and uploaded_files:
            with st.spinner("Processing documents..."):
                response = upload_pdfs_api(uploaded_files)
                if response.status_code == 200:
                    st.success("✅ Uploaded successfully")
                else:
                    st.error(f"❌ Error: {response.text}")