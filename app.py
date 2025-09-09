
# 📦 Imports
import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import google.generativeai as genai

# 🔐 Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure API 
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in env.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

#Loading Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')

#Function to query Gemini
def get_gemini_response(system_prompt, image_parts, user_query):
    try:
        response = model.generate_content([system_prompt, image_parts[0], user_query])
        return response.text
    except Exception as e:
        return f"Error while generating response: {e}"

#Converting uploaded image to format Gemini expects
def prepare_image_data(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No image uploaded.")

#Streamlit UI
st.set_page_config(page_title="Multilanguage Invoice Extractor")
st.title("Multilanguage Invoice Extractor")

#User input prompt
user_query = st.text_input("Ask about the invoice (e.g. What is the total amount?):", key="user_input")

#File uploader
uploaded_file = st.file_uploader("Upload an invoice image", type=["jpg", "jpeg", "png"])

# Show preview of uploaded image
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

#Fixed system prompt for Gemini
system_prompt = """
You are a grand master in understanding invoices. An image of an invoice will be uploaded,
and you must answer questions based on the content of the image.
"""
# system_prompt = """
# Extract key invoice fields and return them in JSON format:
# - Vendor Name
# - Invoice Date
# - Invoice Number
# - Total Amount
# - Tax Amount
# - Due Date (if any)
# """
#Run on button click
if st.button("Tell me about the invoice"):
    if uploaded_file and user_query:
        try:
            image_data = prepare_image_data(uploaded_file)
            response = get_gemini_response(system_prompt, image_data, user_query)
            st.subheader("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload an invoice and enter your question.")

