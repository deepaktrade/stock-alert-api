from fastapi import FastAPI
from services.market_data import MarketData
from services.indicator_service import IndicatorService

app = FastAPI()

market = MarketData()
indicator = IndicatorService()


@app.get("/")
def home():
    return {"message": "Deepak AI Trader Running 🚀"}


@app.get("/stock/{symbol}")
def stock(symbol: str):
    return market.get_stock_price(symbol + ".NS")


@app.get("/signal/{symbol}")
def signal(symbol: str):

    symbol = symbol.upper() + ".NS"

    df = market.get_history(symbol)

    if df.empty:
        return {"error": "No data found"}

    ema20 = indicator.ema(df, 20).iloc[-1]
    ema50 = indicator.ema(df, 50).iloc[-1]
    rsi = indicator.rsi(df).iloc[-1]

    price = float(df["Close"].iloc[-1])

    if price > ema20 and ema20 > ema50 and rsi > 60:
        signal = "BUY"

    elif price < ema20 and ema20 < ema50 and rsi < 40:
        signal = "SELL"

    else:
        signal = "HOLD"

    return {
        "symbol": symbol,
        "price": round(price, 2),
        "ema20": round(float(ema20), 2),
        "ema50": round(float(ema50), 2),
        "rsi": round(float(rsi), 2),
        "signal": signal
    }