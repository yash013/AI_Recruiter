# AI Recruiter 📧

## Description
The AI Recruiter is a tool that enables users to compare their resume with a job description. It assesses the resume, rates it in relation to the job requirements, and provides structured feedback. This includes identifying matching qualifications, pointing out any missing qualifications, acknowledging extra qualifications, offering a numerical rating, and giving tailored suggestions for improvement.

## Usage
1. **Upload Candidate's CV**: Upload a PDF of the candidate's resume.
2. **Enter The Job Description**: Enter the job description.

## Getting Started
### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yash013/AI_Recruiter.git
   cd AI_Recruiter

2. **Environment Setup**:
   - Create .env file
   - Replace .env content with 
   ```
   HF_TOKEN=YOUR_HF_API_TOKEN
   ```
   - [How to get your hf token for free](https://huggingface.co/docs/hub/en/security-tokens)
      * Log in to [huggingface](https://huggingface.co/)
      * Go to Profie > then go to Setttings > then go to Access Tokens tab
      * [Access Tokens Page](https://huggingface.co/settings/tokens)
      * If there exists Access Token then copy it and paste it as HF_TOKEN in .env file of project
      * If Access Token does not exist then click on new token Write the "Name of Token" and Select the "Type of Token" (Read / Write) Access.
      * After creating copy the token and paste it as HF_TOKEN in .env file of project.

3. **Running the AI Recruiter**:
   - Create Virtual Enviornment & Install Dependencies
   * For windows ( git bash )
        ```sh
        python -m venv .venv
        source .venv/Scripts/activate
        pip install -r requirements.txt
        ```
    * For windows ( cmd )
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        pip install -r requirements.txt
        ```
    * For Linux & Mac
        ```sh
        python -m venv .venv
        souce .venv/bin/activate
        pip install -r requirements.txt
        ```
   - Run the Streamlit app:
     ```sh
     streamlit run app.py
     ```
   - Access the UI in your browser at `localhost:8501` (default Streamlit address).

### App Structure
* app.py: Contains the main Streamlit application.
* LLM.py: Module for performing inference on CV and Job Description.
* util.py: Utility functions for writing evaluation results.

## Future Enhancements

- **Customizable Rating Parameters**: Allow users to set their own criteria for what constitutes a strong match between a resume and a job description.
- **Resume Optimization Tips**: Based on the analysis, provide actionable tips to improve the resume for better alignment with job descriptions.
- **Historical Analysis**: Enable users to save and view past analyses to track improvements over time.
- **Multi-Language Support**: Offer resume and job description analysis in multiple languages to cater to a diverse user base.
- **Advanced Analytics Dashboard**: Provide an analytics dashboard with insights into industry trends, common missing qualifications, and more.