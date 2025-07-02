# 📝 AI Grammar Correction App

This is a lightweight, cloud-deployable grammar correction app built using:
- Python 🐍
- HuggingFace Transformers 🤗
- Streamlit 🧼
- Hosted on Streamlit Cloud ☁️

## 🚀 Features

- Accepts full sentences or paragraphs
- Uses a pre-trained NLP model for grammar correction
- Fast, responsive web interface (Streamlit)
- One-click deployment on Streamlit Cloud

---

## 🧠 Model Used

[📚 `prithivida/grammar_error_correcter_v1`](https://huggingface.co/prithivida/grammar_error_correcter_v1)

Fine-tuned T5 model specifically for grammar correction.

---

## 📁 Project Structure

AI-Grammar-Checker-App/
├── app/ # Streamlit UI logic
│ └── streamlit_app.py
├── model/ # Grammar model loader
│ └── grammar_model.py
├── requirements.txt # All dependencies
├── .gitignore # Ignores venv and cache files
├── README.md # 📄 You're reading it!
└── deploy/
└── azure_deploy_instructions.md (optional)


---

## 💻 How to Run Locally

### 🔧 Step 1: Clone and set up

```bash
git clone https://github.com/yourusername/AI-Grammar-Checker-App.git
cd AI-Grammar-Checker-App
python -m venv .venv
.venv\Scripts\activate         # On Windows
# OR
source .venv/bin/activate      # On Mac/Linux
pip install -r requirements.txt
```
### ▶️ Step 2: Run the app
```bash
streamlit run app/streamlit_app.py
```
Open your browser at http://localhost:8501

☁️ One-Click Deployment on Streamlit Cloud
🌐 Host it Free at: https://streamlit.io/cloud
Steps:
1.Push your project to GitHub

2.Go to streamlit.io/cloud

3.Connect GitHub and select your repo

4.Set the app entry point to:
```bash
app/streamlit_app.py
```
5.Click Deploy 🚀

Your app will be live in minutes!

## 🧪 Example
Input:
He go to university every weekends.

Output:
He goes to university every weekend.

## ✅ Requirements
```bash
transformers
torch
streamlit
scikit-learn
```
Install with:
```bash
pip install -r requirements.txt
```