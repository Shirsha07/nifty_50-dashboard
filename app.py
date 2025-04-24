import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from utils.indicators import calculate_indicators

# Title
st.title("📈 Nifty50 Interactive Stock Market Dashboard")

# Sidebar
st.sidebar.header("Settings")
selected_stock = st.sidebar.selectbox("Choose a stock", pd.read_csv("data/nifty50.csv")['Symbol'])
timeframe = st.sidebar.selectbox("Timeframe", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y"])
interval = st.sidebar.selectbox("Interval", ["1m", "5m", "15m", "1h", "1d"])

# Fetch data
df = yf.download(selected_stock, period=timeframe, interval=interval)
df.dropna(inplace=True)
df = calculate_indicators(df)

# Show latest indicators
st.metric("Current Price", round(df['Close'].iloc[-1], 2))
st.metric("MACD", round(df['MACD'].iloc[-1], 2))
st.metric("RSI", round(df['RSI'].iloc[-1], 2))

# Candlestick chart
fig = go.Figure(data=[
    go.Candlestick(x=df.index,
                   open=df['Open'], high=df['High'],
                   low=df['Low'], close=df['Close'],
                   name='Candlestick'),
    go.Scatter(x=df.index, y=df['EMA20'], line=dict(color='blue'), name="EMA 20"),
    go.Scatter(x=df.index, y=df['BB_upper'], line=dict(color='green', dash='dot'), name='Upper BB'),
    go.Scatter(x=df.index, y=df['BB_lower'], line=dict(color='red', dash='dot'), name='Lower BB')
])
fig.update_layout(title=f"{selected_stock} Candlestick Chart", xaxis_title="Date", yaxis_title="Price")
st.plotly_chart(fig)

# Show Data
with st.expander("See Raw Data"):
    st.dataframe(df.tail())
