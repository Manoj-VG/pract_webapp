import yfinance as yf
import streamlit as st
import datetime


title = st.text_input("Company Name","TSLA")

ticker_data = yf.Ticker(title)
st.header("Stock Market Analyser")

col1, col2 = st.columns(2)

start_date = col1.date_input("Enter start date", datetime.date(year=2020, month=1, day=1))
end_date = col2.date_input("Enter end date", datetime.date.today())

ticker_df = ticker_data.history( start = start_date, end = end_date)

st.dataframe(ticker_df)
st.line_chart(ticker_df["Close"])