import yfinance as yf

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")  # Fetch past 1 month of data
        info = stock.info  # Get stock metadata
        
        if not data.empty:
            return {
                "name": info.get("longName", "N/A"),
                "symbol": ticker.upper(),
                "price": info.get("regularMarketPrice", "N/A"),
                "market_cap": info.get("marketCap", "N/A"),
                "pe_ratio": info.get("trailingPE", "N/A"),
                "dividend_yield": info.get("dividendYield", "N/A"),
                "history": data["Close"].to_dict()
            }
        else:
            return {"error": "Invalid Ticker or No Data Available"}
    
    except Exception as e:
        return {"error": f"Error fetching stock data: {str(e)}"}

if __name__ == "__main__":
    user_ticker = input("Enter stock ticker symbol (e.g., AAPL, TSLA, MSFT): ").strip().upper()
    print(get_stock_data(user_ticker))
