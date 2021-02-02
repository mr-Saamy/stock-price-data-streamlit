import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date
st.write("""
# Simple Stock Price Checker App

## Shown are the stock price and volume of your desired company since 2000

""")

# select a ticker symbol for the company that
# you wamnt to check the stock prices... in this
# case... Defaults to Google
st.write("""
### Enter Ticker Symbol Of Desired Company: 
""")

ticker_symbol = st.text_input("", 'GOOGL')

# get the stocks data
ticker_data = yf.Ticker(ticker_symbol)

# filter out the required timeframe
ticker_of = ticker_data.history(
    start='2000-1-31', end=str(date.today().strftime("%Y-%m-%d")))

# plot the data
st.line_chart(ticker_of.Close)
st.line_chart(ticker_of.Volume)
