import json
import yfinance as yf

WATCHLIST_PATH = "watchlist.json"

def load_watchlist():
    with open(WATCHLIST_PATH, "r") as f:
        return json.load(f)

def save_watchlist(watchlist):
    with open(WATCHLIST_PATH, "w") as f:
        json.dump(watchlist, f)

def add_to_watchlist(ticker):
    watchlist = load_watchlist()
    ticker = ticker.upper()
    if ticker not in watchlist:
        watchlist.append(ticker)
        save_watchlist(watchlist)
        return f"{ticker} added to watchlist."
    return f"{ticker} is already in your watchlist."

def remove_from_watchlist(ticket):
    watchlist = load_watchlist()
    ticker = ticker.upper()
    if ticker in watchlist:
        watchlist.remove(ticker)
        save_watchlist(watchlist)
        return f"{ticker} has been removed from your watchlist"
    
    return f"{ticker} is not in your watchlist"

def get_stock_data(symbols):
    stock_data = []

    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="2d")

        if len(data) < 2:
            continue

        today = data["Close"].iloc[-1]
        yesterday = data["Close"].iloc[-2]
        diff = today - yesterday
        pct = (diff / yesterday) * 100

        stock_data.append({
            "symbol": symbol,
            "price": today,
            "change": diff,
            "percent": pct
        })

    return stock_data

def display_stock_data(stocks):
    print(f"{'Symbol':<8} {'Price':<10} {'Change':<10} {'%Change':<10}")
    print("-" * 40)
    for s in stocks:
        print(f"{s['symbol']:<8} ${s['price']:<10.2f} {s['change']:<10.2f} {s['percent']:<10.2f}")