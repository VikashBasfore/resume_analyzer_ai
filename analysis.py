import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai

# refer pdf.py
from pdf import extractpdf

key = os.getenv('GOOGLE_KEY_API')
genai.configure(api_key = key)

model = genai.GenerativeModel('gemini-2.5-flash')

def analyze_resume(pdf_doc, job_des):
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc) # class in pdf.py will run
        st.write('Extract Successfully ✅')
        
    else:
        st.warning('Error!! Drop file in PDF format ❌')
        return
        
    
    ats_score = model.generate_content(f'''Compare the resume {pdf_text} with given job description
                                       {job_des} and get ATS score in scale of 0 to 100.
                                       Genertae the result in bullet points (minimum 5 points)''')
    
    prod_score = model.generate_content(f'''Compare the resume {pdf_text} and the given job description
                                        {job_des} and give the probability in percent
                                        0 to 100 to get selected on the given job''')
    
    good_fit = model.generate_content(f'''Compare the resume {pdf_text} and the given job description
                                      {job_des} and say am i a good fit for the job or not.
                                      if not, highlight what am i lacking and 
                                      suggest the areas of improvement''')
    
    swot_analysis = model.generate_content(f'''Compare the resuma {pdf_text} and the given job description
                                           {job_des} and provide SWOT analysis.
                                           Generate minimum 3 points for each analysis''')
    
    return {st.write(ats_score.text),
            st.write(prod_score.text),
            st.write(good_fit.text),
            st.write(swot_analysis.text)}
    
        