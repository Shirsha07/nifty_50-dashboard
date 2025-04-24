import pandas as pd
import ta

def calculate_indicators(df):
    df['MACD'] = ta.trend.macd_diff(df['Close'])
    df['RSI'] = ta.momentum.rsi(df['Close'])
    bb = ta.volatility.BollingerBands(df['Close'])
    df['BB_upper'] = bb.bollinger_hband()
    df['BB_lower'] = bb.bollinger_lband()
    df['EMA20'] = ta.trend.ema_indicator(df['Close'], window=20)
    return df
