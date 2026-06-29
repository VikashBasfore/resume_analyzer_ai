<div align="center">

# 📄🤖 Resume Analyzer AI

### Smart ATS Resume Screening & Job Match Analysis using Google Gemini AI

<img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
<img src="https://img.shields.io/badge/Streamlit-Web%20Application-FF4B4B?logo=streamlit">
<img src="https://img.shields.io/badge/Google-Gemini%202.5-blue">
<img src="https://img.shields.io/badge/LLM-AI%20Powered-success">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen">

---

### 🚀 Upload Resume → Paste Job Description → Get AI Career Insights in Seconds

</div>

---

# 💼 What is Resume Analyzer AI?

Resume Analyzer AI is an intelligent career assistant that evaluates resumes against job descriptions using **Google Gemini 2.5 Flash**.

Instead of simply extracting keywords, the application performs an AI-driven comparison between the candidate's resume and the target job description to generate professional recruitment insights similar to those used in Applicant Tracking Systems (ATS).

The application provides instant feedback on resume quality, job fit, ATS compatibility, improvement areas, and SWOT analysis through a simple and interactive Streamlit interface.

---

# 🎯 What Can It Do?

✅ Extract text automatically from PDF resumes

✅ Compare resumes with any Job Description

✅ Generate ATS Compatibility Score

✅ Predict Selection Probability

✅ Evaluate Job Fit

✅ Highlight Missing Skills

✅ Recommend Resume Improvements

✅ Generate Complete SWOT Analysis

---

# ⚡ Application Workflow

```text
                  Resume PDF
                      │
                      ▼
              PDF Text Extraction
                      │
                      ▼
             Job Description Input
                      │
                      ▼
             Google Gemini AI
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 ATS Score      Selection Chance    Job Fit
                      │
                      ▼
            SWOT Analysis Report
                      │
                      ▼
          Resume Improvement Tips
```

---

# 🧠 AI Analysis Modules

## 📊 ATS Score

The application estimates how well the uploaded resume aligns with the provided job description.

Outputs include:

* ATS Match Score (0–100)
* Resume Matching Analysis
* Keyword Relevance
* Missing Requirements

---

## 🎯 Selection Probability

AI estimates the likelihood of getting shortlisted for the position based on resume quality and job requirements.

Example:

```
Selection Probability

82%
```

---

## ✅ Job Fit Analysis

The AI evaluates whether the candidate is a good fit for the position.

It explains:

* Matching qualifications
* Missing technical skills
* Missing soft skills
* Suggested certifications
* Recommended improvements

---

## 📈 SWOT Analysis

A complete professional SWOT report is generated.

### Strengths

* Technical skills
* Relevant experience
* Education

### Weaknesses

* Skill gaps
* Missing tools
* Resume issues

### Opportunities

* Courses
* Certifications
* Career growth

### Threats

* Market competition
* Experience mismatch
* ATS limitations

---

# 🖥️ User Interface

The Streamlit dashboard provides:

* 📂 Resume PDF Upload
* 📝 Job Description Input
* ⚡ One-click AI Analysis
* 📊 Interactive Results
* 🤖 Google Gemini Responses
* 💬 User-friendly Interface

---

# 🛠️ Technologies Used

| Category       | Technologies            |
| -------------- | ----------------------- |
| Language       | Python                  |
| Web Framework  | Streamlit               |
| AI Model       | Google Gemini 2.5 Flash |
| PDF Processing | PyPDF                   |
| Environment    | Python-dotenv           |

---

# 📁 Project Structure

```text
Resume-Analyzer-AI
│
├── interface.py
├── analysis.py
├── pdf.py
├── requirements.txt
├── .env
├── README.md
└── sample_resume.pdf
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Resume-Analyzer-AI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_KEY_API=YOUR_GEMINI_API_KEY
```

Run the application

```bash
streamlit run interface.py
```

---

# 📖 How to Use

### Step 1

Upload your Resume (PDF)

⬇️

### Step 2

Paste the Job Description

⬇️

### Step 3

Click **Generate Score**

⬇️

### Step 4

View:

* ATS Score
* Selection Probability
* Job Fit Analysis
* SWOT Report
* Resume Improvement Suggestions

---

# 🌟 Why This Project?

Traditional ATS tools mainly focus on keyword matching.

Resume Analyzer AI goes a step further by leveraging Large Language Models to provide contextual resume evaluation, personalized career guidance, and actionable recommendations.

This makes the application useful for:

* Students
* Job Seekers
* Recruiters
* Career Coaches
* HR Professionals

---

# 🔮 Future Enhancements

* Resume Ranking System
* Multi-Resume Comparison
* AI Cover Letter Generator
* Resume Rewriter
* LinkedIn Profile Analysis
* Interview Question Generator
* PDF Report Export
* Resume Score History
* Multiple AI Model Support

---

# 📸 Screenshots

```
📁 images/

dashboard.png

upload_resume.png

ats_score.png

swot_analysis.png

job_fit.png
```

*(Add screenshots after deployment for a richer GitHub presentation.)*

---

# 👨‍💻 Developer

**Vikash Basfore**

Data Science • Machine Learning • Generative AI

---

# 🙏 Credits

This project was built using amazing open-source technologies and APIs.

Special thanks to:

* Google Gemini AI
* Streamlit
* PyPDF
* Python-dotenv
* Python Open Source Community

---

<div align="center">

### ⭐ If you like this project, don't forget to Star ⭐ the repository.

**Happy Coding! 🚀**

</div>
