import sys
import os

# Add parent directory to Python path so 'model' module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.grammar_model import correct_grammar
import streamlit as st

# Page configuration
st.set_page_config(page_title="Grammar Correction App", layout="centered")

# App title
st.title("📝 Grammar Correction App")
st.write("This app corrects the grammar of your input using a pre-trained NLP model from Hugging Face.")

# Input text box
text_input = st.text_area("✍️ Enter your sentence or paragraph below:")

# Button to trigger correction
if st.button("🔍 Correct Grammar"):
    if text_input.strip():
        with st.spinner("Correcting grammar..."):
            corrected = correct_grammar(text_input)
            st.success("✅ Corrected Text:")
            st.write(corrected)
    else:
        st.warning("⚠️ Please enter some text above before clicking the button.")
