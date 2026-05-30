<img src="https://raw.githubusercontent.com/rizinthehub/ZenJournal/main/assets/favicon.svg" width="40" align="left" style="margin-right: 12px;" />

# ZenJournal

**ZenJournal** is an AI-powered journaling app built for calm, reflective writing. It uses Natural Language Processing to analyze your daily entries, visualize mood trends, and surface recurring themes from your own words.

Designed with editorial typography, a sage-green palette, and a dark/light theme system — built to feel like a quiet room, not a dashboard.

## ✦ Features

- **AI Sentiment Analysis** – Real-time mood detection on every entry using TextBlob
- **Mood Timeline** – Smooth gradient area chart of your emotional trends (Altair)
- **Theme Discovery** – Auto-generated pill cloud of recurring words from your journal
- **Entry Timeline** – Clean, journal-style list of recent entries with sentiment indicators
- **Dark / Light Mode** – One-click theme toggle with a calming sage accent
- **Time-Aware Greeting** – Personalized opening that adapts to morning, afternoon, or evening
- **Local-First** – All entries stay on your machine in a private CSV
- **Editorial Design** – Custom typography (Instrument Serif + Inter) and motion design

## 🛠️ Tech Stack

- **Language:** Python 3
- **Frontend:** Streamlit + custom CSS
- **AI / NLP:** TextBlob (sentiment analysis)
- **Visualization:** Altair (gradient area charts)
- **Data:** Pandas + CSV
- **Typography:** Instrument Serif, Inter, JetBrains Mono (via Google Fonts)

## 🗂️ Project Structure

```
ZenJournal/
├── app.py           # Main journal application
├── backend.py       # MoodAI class — sentiment logic + data persistence
├── theme.py         # Dark/light theme tokens + toggle state
├── styles.py        # Theme-aware CSS generator
├── components.py    # Reusable UI components (animated logo)
├── landing.py       # Marketing landing page
├── assets/
│   └── favicon.svg
└── requirements.txt
```

## 💻 Run Locally

```bash
git clone https://github.com/rizinthehub/ZenJournal.git
cd ZenJournal

python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

To preview the marketing landing page:

```bash
streamlit run landing.py
```

## 🎨 Design Philosophy

> *"Calm intelligence."*

ZenJournal is inspired by apps like **Linear, Notion, Things 3, and Day One** — favoring editorial typography, generous whitespace, and a single intentional accent color over the typical "AI app" aesthetic.

## 📌 Roadmap

- [ ] Streak counter
- [ ] Weekly AI summaries
- [ ] Keyboard shortcut to save (⌘ + Enter)
- [ ] Calendar heatmap view
- [ ] Export to PDF / Markdown

---

*Built as a personal project to explore NLP, design systems, and full-stack UI engineering in Python.*
