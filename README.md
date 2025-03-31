#  AI Stock Analyst

##  Overview
AI Stock Analyst is a web-based application that provides **real-time stock market data**, **historical prices**, and **sentiment analysis** of financial news. The app leverages **Yahoo Finance (`yfinance`)** for stock data, **OpenAI's GPT model** for chatbot interactions, and **transformers** for sentiment analysis.

## 🛠 Features
-  **Fetch real-time stock price & market data**
-  **View historical stock prices (Last 1 Month)**
-  **Sentiment Analysis of Stock-related News**
-  **AI Chatbot for stock-related queries**
-  **Simple & responsive UI**

##  Project Structure
```
├── app.py                 # Main Flask app
├── templates
│   ├── index.html         # Frontend UI template
├── static
│   ├── style.css          # CSS styling
│   ├── script.js          # Frontend JS logic
├── sentiment_analysis.py  # News scraping & sentiment analysis
├── requirements.txt       # Dependencies list
├── README.md              # Project documentation
├── config.env             # API keys (DO NOT SHARE!)
```

##  Installation & Setup

###  Clone the Repository
```sh
git clone https://github.com/yourusername/ai-stock-analyst.git
cd ai-stock-analyst
```

###  Install Dependencies
```sh
pip install -r requirements.txt
```

###  Set Up API Keys
Create a **config.env** file and add your API keys:
```sh
OPENAI_API_KEY=your_openai_api_key
```

###  Run the Application
```sh
python app.py
```
Then, open **http://127.0.0.1:5000/** in your browser.

##  Usage
1. **Enter a stock ticker (e.g., AAPL, TSLA)** in the input field.
2. Click **"Get Stock Info"** to fetch data.
3. View **stock price, market cap, P/E ratio, and news sentiment**.
4. Chat with the AI chatbot for **stock insights**.

##  Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: Yahoo Finance (`yfinance`), OpenAI, Transformers (Hugging Face)

## License
This project is licensed under the **MIT License**.

---
 **Developed by Daniil Nasadiuk**
