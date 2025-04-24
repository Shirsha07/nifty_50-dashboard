import pandas as pd
import ta

def calculate_indicators(df):
    # Make sure 'Close' is 1D before passing it to macd_diff
    close_data = df['Close'].squeeze()  # Ensures it's 1D
    
    # Calculate MACD
    df['MACD'] = ta.trend.macd_diff(close_data)
    
    # Add other indicators here
    return df

