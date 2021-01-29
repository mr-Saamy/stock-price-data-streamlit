import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date
st.write("""
# Simple Stock Price Checker App

## Shown are the stock price and volume of Microsoft since 2010

""")
# select a ticker symbol for the company that
# you wamnt to check the stock prices... in this
# case... Microsoft
ticker_symbol = 'MSFT'

# get the stocks data
ticker_data = yf.Ticker(ticker_symbol)

# filter out the required timeframe
ticker_of = ticker_data.history(
    start='2010-1-31', end=str(date.today().strftime("%Y-%m-%d")))

# plot the data
st.line_chart(ticker_of.Close)
st.line_chart(ticker_of.Volume)
