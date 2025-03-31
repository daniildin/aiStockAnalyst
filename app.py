import os
import yfinance as yf
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from sentiment_analysis import get_stock_news, analyze_sentiment

# Load API key from .env
load_dotenv('config.env')
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def format_number(value):
    """Format large numbers to 4 significant figures"""
    if isinstance(value, (int, float)):
        return f"{value:.4g}"
    return "N/A"

def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.info  # Use 'info' instead of 'fast_info' for better reliability

        price = stock_info.get("regularMarketPrice", "N/A")

        # Fetch stock history (last 1 month)
        history_data = stock.history(period="1mo")
        history = {str(date.date()): round(price, 2) for date, price in history_data["Close"].items()} if not history_data.empty else {}

        stock_data = {
            "symbol": ticker.upper(),
            "name": stock_info.get("shortName", "N/A"),
            "price": round(price, 2) if isinstance(price, (int, float)) else "N/A",
            "market_cap": format_number(stock_info.get("marketCap")),
            "pe_ratio": format_number(stock_info.get("trailingPE")),
            "dividend_yield": format_number(stock_info.get("dividendYield")),
            "history": history
        }

        return stock_data

    except Exception as e:
        return {"error": f"Error fetching stock data: {str(e)}"}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/get_stock", methods=["POST"])
def fetch_stock_data():
    data = request.get_json()  # Use JSON parsing
    ticker = data.get("ticker", "").strip().upper()

    if not ticker:
        return jsonify({"error": "Invalid ticker symbol"}), 400

    try:
        stock = get_stock_info(ticker)
        if "error" in stock:
            return jsonify(stock), 500

        news_articles = get_stock_news(ticker)
        sentiment_results = analyze_sentiment(news_articles)

        news_sentiments = [
            {
                "article": result["article"],
                "label": result["label"],
                "score": result["score"]
            }
            for result in sentiment_results
        ]

        return jsonify({"stock": stock, "news_sentiment": news_sentiments})

    except Exception as e:
        return jsonify({"error": f"Error fetching stock data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
