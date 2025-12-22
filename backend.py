import pandas as pd
from textblob import TextBlob
from datetime import datetime
import os

class MoodAI:
    def __init__(self, filename='journal_data.csv'):
        self.filename = filename
        self.check_database()

    def check_database(self):
        # If the file doesn't exist, create it with headers
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=['Date', 'Entry', 'Mood_Score', 'Sentiment'])
            df.to_csv(self.filename, index=False)

    def analyze_entry(self, text):
        # AI Concept: Sentiment Analysis
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        
        # Simple logic to classify the number as a word
        if sentiment_score > 0.5:
            mood = "Happy 😄"
        elif sentiment_score > 0:
            mood = "Positive 🙂"
        elif sentiment_score == 0:
            mood = "Neutral 😐"
        else:
            mood = "Negative 😔"
            
        return sentiment_score, mood

    def save_entry(self, text, score, sentiment_label):
        # Save data to CSV (Simulating a database)
        new_entry = {
            'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Entry': text,
            'Mood_Score': score,
            'Sentiment': sentiment_label
        }
        df = pd.DataFrame([new_entry])
        # Append to the CSV file without rewriting headers
        df.to_csv(self.filename, mode='a', header=False, index=False)

    def load_data(self):
        # Load data for visualization
        return pd.read_csv(self.filename)