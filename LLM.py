import os
from dotenv import load_dotenv


def format_prompt_1(CandidateCV,JobDescription):
    prompt = f"""
    Assume you are a recruiter,

    Providing you with the Candidate's CV and the Job Description below:

    You are required to provide the following details succinctly:
    1. Matching Qualifications: Enumerate, point by point and in a formatted manner (note: each point on a new line), the qualifications and experiences in the candidate's CV that align with the job description.
    2. Missing Qualifications: List, in a similar formatted manner, the qualifications and experiences that the job description requires but are absent in the candidate's CV.
    3. Additional Qualifications: Detail any extra qualifications and experiences the candidate possesses that, while not required, could be advantageous for the job role.
    4. Candidate Rating: Rate the Candidate out of 10 based on the rules given below. Show the calculations.
    5. Suggestions: Provid few suggestions to improve that score.

    Rating Evaluation Rules:
    - Start with a base score of 5, which assumes the candidate meets the minimum job requirements.
    - For each qualification or experience that matches the job description, add 0.5 to the score.
    - For each missing qualification or experience required by the job description, subtract 0.5 from the score.
    - For each additional qualification or experience the candidate has that could benefit the role, add 0.25 to the score.
    - The final score should be rounded to the nearest whole number, with a maximum possible score of 10.

    Candidate's CV : "{CandidateCV}"

    Job Description : "{JobDescription}"
    
    Total Rating : "/10"
  

    """
    
    return prompt


 
# loading env varaibles
load_dotenv()
# REPLACE WITH YOUR HUGGING FACE ACCOUNT TOKEN ( Go to settings and get access token from hugging face)
hf_token=os.getenv('HF_TOKEN')

# querying
def query(payload):
    
    import requests

    # Replace API URL with your LLM API URL ( from hugging face. i.e. )
    # for example HF_LLM_INFERENCE_CHECKPOINT='https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2'
    # API_URL='https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2'
    API_URL="https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    # API_URL = os.getenv('HF_LLM_INFERENCE_CHECKPOINT')

    headers = {"Authorization": "Bearer "+hf_token}
    
    # retriving response
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def prompt_format_2(CandidateCV,JobDescription):
  formatted_prompt=format_prompt_1(CandidateCV,JobDescription)
  prompt='<s>[INST] '+formatted_prompt+'\n [/INST] Model answer</s>'
  return prompt

def infer(CandidateCV,JobDescription):
  try:
      print("going to infer")

      prompt=prompt_format_2(CandidateCV,JobDescription)
      
      # print("generated prompt",prompt)
      output = query({
          "inputs": prompt,
          "parameters": 
        {
          "contentType": "application/json",
          "max_tokens": 30000,
          "max_new_tokens": 5000,
          "return_full_text": False
        }
      })

      return output[0]['generated_text']
  except Exception as e:
        print(f"An error occurred: {e}")
        return f"could not generate answer Due to Error, please try after some time ,{e} "  