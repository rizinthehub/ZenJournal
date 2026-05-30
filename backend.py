import pandas as pd
from textblob import TextBlob
from datetime import datetime
import os

class MoodAI:
    def __init__(self, filename='journal_data.csv'):
        self.filename = filename
        self.check_database()

    def check_database(self):
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=['Date', 'Entry', 'Mood_Score', 'Sentiment'])
            df.to_csv(self.filename, index=False)

    def analyze_entry(self, text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        
        if sentiment_score > 0.1:
            mood = "positive"
        elif sentiment_score < -0.1:
            mood = "negative"
        else:
            mood = "neutral"
            
        return sentiment_score, mood

    def save_entry(self, text, score, sentiment_label):
        new_entry = {
            'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Entry': text,
            'Mood_Score': score,
            'Sentiment': sentiment_label
        }
        df = pd.DataFrame([new_entry])
        df.to_csv(self.filename, mode='a', header=False, index=False)

    def load_data(self):
        return pd.read_csv(self.filename)