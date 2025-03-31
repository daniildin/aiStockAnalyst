import requests
from transformers import pipeline

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def get_stock_news(stock_symbol):
    """
    Fetch stock-related news articles.
    Replace with an actual news API for real data.
    """
    return [
        f"Breaking: {stock_symbol} surges after earnings report!",
        f"{stock_symbol} faces challenges as market volatility increases.",
        f"Experts say {stock_symbol} is a strong buy right now!"
    ]

def analyze_sentiment(news_articles):
    """
    Analyze sentiment of stock-related news articles and return structured data.
    """
    sentiments = []
    for article in news_articles:
        try:
            result = sentiment_pipeline(article)[0]
            sentiments.append({"article": article, "label": result["label"], "score": round(result["score"], 4)})
        except Exception as e:
            sentiments.append({"article": article, "label": "Unknown", "score": 0, "error": str(e)})
    
    return sentiments
