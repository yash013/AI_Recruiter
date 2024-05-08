import streamlit as st
# import streamlit.components.v1 as components
from pdfminer.high_level import extract_text
from io import BytesIO
from LLM import infer
from util import write_answer
# from trans import speak

def read_pdf(file):
    file_like = BytesIO(file.getvalue())
    text = extract_text(file_like)
    return text

def main():
    
    st.set_page_config(
        page_title="AI Recruiter",
        page_icon="📧",
        # layout="wide",
    )
    
if __name__ == "__main__":
    main()

st.title("AI Recruiter")

st.write("Let The AI analyse your CV for the job and rate it!")

st.markdown("#### Step 1 : Upload The CV")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
resume = ""
if uploaded_file is not None:
    # To read file as bytes:
    text = read_pdf(uploaded_file)
    # Display the extracted text in a code block with a copy button
    with st.container():
        resume = st.text_area("Extracted Text", text, height=100)
# components.html(
#     """
#     <iframe
#         # src="https://merve-llava-next.hf.space"
#         frameborder="0"
#         width="100%"
#         height="80%"
#     ></iframe>
#     """
# )
st.markdown("#### Step 2 : Enter Job Description")
job_description = st.text_area("Enter Job Description here")


if st.button('Examine Result', key='submit_button', help='Click to submit your input.'):
    placeholder = st.empty()
    placeholder.image("examine.gif")
    Evaluation=infer(resume,job_description)
    placeholder.empty()

    write_answer(Evaluation)

# display_footer()

    # speak(Evaluation)
