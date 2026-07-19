import yfinance as yf


class MarketData:
    def get_stock_price(self, symbol: str):
        ticker = yf.Ticker(symbol)

        data = ticker.history(period="1d")

        if data.empty:
            return {"error": "No data found"}

        latest = data.iloc[-1]

        return {
            "symbol": symbol,
            "open": float(latest["Open"]),
            "high": float(latest["High"]),
            "low": float(latest["Low"]),
            "close": float(latest["Close"]),
            "volume": int(latest["Volume"])
        }