
import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat

st.set_page_config(page_title="ZenSight: Mental Health Support", layout="wide")


st.markdown(
    """
    <style>
    /* Base styling */
    body, .stApp {
        background: linear-gradient(135deg, #1e5799 0%, #2989d8 100%);
        background-attachment: fixed;
        color: #ffffff;
    }
    
    /* Papyrus heading */
    h1 {
        font-family: 'Papyrus', fantasy;
        text-align: center;
        font-size: 3.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }
    
    /* Palatino body text */
    body, .stMarkdown, .stText, .stButton, .stTextInput {
        font-family: 'Palatino', 'Palatino Linotype', 'Book Antiqua', serif;
    }
    
    /* Hero section */
    .hero {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    /* Feature cards */
    .feature-card {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.15);
        transition: all 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.2);
    }
    
    /* CTA button */
    .stButton>button {
        background: linear-gradient(135deg, #ffffff 0%, #e6f0ff 100%) !important;
        color: #1e5799 !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 12px 30px !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        transition: all 0.3s ease !important;
        display: block;
        margin: 2rem auto;
        width: 250px;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2) !important;
    }
    
    /* Testimonial styling */
    .testimonial {
        font-style: italic;
        border-left: 3px solid rgba(255,255,255,0.5);
        padding-left: 1rem;
        margin: 1.5rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="hero">
        <h1>🧠 ZenSight</h1>
        <h2 style="font-size: 2rem; margin-bottom: 1.5rem;">
            The only chat that lowers your stress instead of raising it ⬇️😌
        </h2>
        <p style="font-size: 1.5rem; max-width: 800px; margin: 0 auto;">
            "Your thoughts are not facts. Let's untangle them together" 🧠✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🌅 24/7 Support</h3>
            <p>Instant help whenever you need it - no appointments needed</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🔒 Judgment-Free Zone</h3>
            <p>Share freely without fear - your secrets are safe here</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🌱 Personalized Growth</h3>
            <p>Evidence-based techniques tailored to your needs</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if st.button("Begin Healing Conversation Now ➡️", key="main_cta"):
    st.session_state.show_chat = True


if st.session_state.get("show_chat"):
    render_uploader()
    render_chat()
    render_history_download()

