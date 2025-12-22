# 🧠 ZenJournal

**ZenJournal** is an AI-powered smart diary that helps track your mental health. It uses Natural Language Processing (NLP) to analyze daily journal entries and visualize mood trends over time.

## 🚀 Features

- **AI Sentiment Analysis** – Uses TextBlob to classify entries as Positive, Neutral, or Negative
- **Mood Visualization** – Interactive charts powered by Streamlit
- **Local Storage** – All data is stored securely on your local machine
- **Modern UI** – Clean interface with dark-mode support

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Frontend:** Streamlit  
- **AI / NLP:** TextBlob  
- **Data Handling:** Pandas  

## 💻 How to Run Locally

```bash
git clone https://github.com/rizinthehub/ZenJournal.git
cd ZenJournal

python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

pip install -r requirements.txt

streamlit run main.py
