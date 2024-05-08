# import os
# import torch
import streamlit as st
import time
import textwrap

def write_answer(Answer,language='en'):
    # spliting into paragraphs
    paragraphs=Answer.split('\n\n')
    TranslatedAnswer=''

    # writing each paragraph and translating if it is other than 'en'
    for paragraph in paragraphs:
        translated_paragraph=paragraph

        if language != 'en':
            translated_paragraph=translate(paragraph,'en',language)

        TranslatedAnswer+=translated_paragraph+'\n\n'

        # text wrap for screen
        wrapped_text = textwrap.fill(translated_paragraph)

        # streaming the text
        placeholder = st.empty()

        prev_text=''
        for char in wrapped_text:
            prev_text=prev_text+char
            placeholder.text(prev_text)
            time.sleep(0.001)  # Adjust the sleep duration as needed
        st.write('\n\n')
  

def display_footer():
    st.markdown(
        """
        <style>
            
            .footer {
                bottom:0
                background-color: #f8f9fa;
                padding: 20px 0;
                color: #495057;
                text-align: center;
                border-top: 1px solid #dee2e6;
            }
            .footer a {
                color: #007bff;
                text-decoration: none;
            }
            .footer a:hover {
                color: #0056b3;
                text-decoration: underline;
            }
        </style>
        <div class="content">
            <!-- Your main app content goes here -->
        </div>
        <div class="footer">
            <p class="mb-0">Made with 🙏 designed by Yash D Suthar</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
# def generate_context(search_results):
#     print("going to generate context")
#     Context=""
    
#     for link_url,data in search_results.items():
#         Context+="From "+link_url+" => "+data

#     return Context