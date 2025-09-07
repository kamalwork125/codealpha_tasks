# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER (run only once)
nltk.download('vader_lexicon')

# Load Dataset
df = pd.read_csv("amazon_reviews.csv")   # Apna dataset file ka naam yaha do
print(df.head())

# Create Sentiment Column from Ratings
def get_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

df['Sentiment'] = df['Rating'].apply(get_sentiment)

print(df['Sentiment'].value_counts())

# -------------------------
# Step 3: Sentiment Analysis with VADER
# -------------------------
sid = SentimentIntensityAnalyzer()
df['VADER_Score'] = df['ReviewText'].apply(lambda x: sid.polarity_scores(str(x))['compound'])

# Convert score into sentiment
def vader_sentiment(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df['VADER_Result'] = df['VADER_Score'].apply(vader_sentiment)

# -------------------------
# Step 4: Visualization
# -------------------------

# Countplot
plt.figure(figsize=(6,4))
sns.countplot(x='Sentiment', data=df, palette='viridis')
plt.title("Sentiment Distribution (Based on Ratings)")
plt.show()

# WordCloud for Positive Reviews
positive_text = " ".join(df[df['Sentiment']=='Positive']['ReviewText'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud - Positive Reviews")
plt.show()

# WordCloud for Negative Reviews
negative_text = " ".join(df[df['Sentiment']=='Negative']['ReviewText'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='black', colormap="Reds").generate(negative_text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud - Negative Reviews")
plt.show()

# -------------------------
# Step 5: Insights
# -------------------------
print("📌 Insights:")
print("Most reviews are:", df['Sentiment'].mode()[0])
print("Positive Reviews:", len(df[df['Sentiment']=='Positive']))
print("Negative Reviews:", len(df[df['Sentiment']=='Negative']))
print("Neutral Reviews:", len(df[df['Sentiment']=='Neutral']))
