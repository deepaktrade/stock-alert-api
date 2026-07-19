import yfinance as yf


class MarketData:

    def get_history(self, symbol):
        """
        Download 6 months of historical data
        """
        ticker = yf.Ticker(symbol)
        return ticker.history(period="6mo")

    def get_stock_price(self, symbol):
        """
        Get today's latest price
        """
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