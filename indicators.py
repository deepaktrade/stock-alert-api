import pandas as pd


class IndicatorService:

    def ema(self, df, period):
        return df["Close"].ewm(span=period, adjust=False).mean()

    def rsi(self, df, period=14):

        delta = df["Close"].diff()

        gain = delta.where(delta > 0, 0)

        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi