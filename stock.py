import streamlit as st
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_datareader as web

# Title
st.title('Stock Portfolio')


tickers = []
amounts = []
prices = []
total = []

bool_v = True

# Sidebar section
st.sidebar.header("Please add some stocks")

if (bool_v):
    ticker = st.sidebar.selectbox("What stock to add?", ['AAPL', 'TSLA', 'FB', 'MSFT', 'AMZN', 'GOOG', 'NVDA', 'ABNB', 'ALL', 'CMG', 'BAC', 'JPM', 'GME', 'HD'],key="new")
    amount = st.sidebar.number_input("How many shares?",1,100,2)
    tickers.append(ticker)
    amounts.append(amount)
    ticker2 = st.sidebar.selectbox("What stock to add?", ['AAPL', 'TSLA', 'FB', 'MSFT', 'AMZN', 'GOOG', 'NVDA', 'ABNB', 'ALL', 'CMG', 'BAC', 'JPM', 'GME', 'HD'],key="new3")
    amount2 = st.sidebar.number_input("How many shares?",1,100,4, key="new2")
    tickers.append(ticker2)
    amounts.append(amount2)
    ticker3 = st.sidebar.selectbox("What stock to add?", ['AAPL', 'TSLA', 'FB', 'MSFT', 'AMZN', 'GOOG', 'NVDA', 'ABNB', 'ALL', 'CMG', 'BAC', 'JPM', 'GME', 'HD'],key="new2")
    amount3 = st.sidebar.number_input("How many shares?",1,100,4, key="new4")
    tickers.append(ticker3)
    amounts.append(amount3)
    ticker4 = st.sidebar.selectbox("What stock to add?", ['AAPL', 'TSLA', 'FB', 'MSFT', 'AMZN', 'GOOG', 'NVDA', 'ABNB', 'ALL', 'CMG', 'BAC', 'JPM', 'GME', 'HD'],key="new5")
    amount4 = st.sidebar.number_input("How many shares?",1,100,4, key="new6")
    tickers.append(ticker4)
    amounts.append(amount4)
    ticker5 = st.sidebar.selectbox("What stock to add?", ['AAPL', 'TSLA', 'FB', 'MSFT', 'AMZN', 'GOOG', 'NVDA', 'ABNB', 'ALL', 'CMG', 'BAC', 'JPM', 'GME', 'HD'],key="new7")
    amount5 = st.sidebar.number_input("How many shares?",1,100,4, key="new8")
    tickers.append(ticker5)
    amounts.append(amount5)
    ticker6 = st.sidebar.selectbox("What stock to add?", ['AAPL', 'TSLA', 'FB', 'MSFT', 'AMZN', 'GOOG', 'NVDA', 'ABNB', 'ALL', 'CMG', 'BAC', 'JPM', 'GME', 'HD'],key="new9")
    amount6 = st.sidebar.number_input("How many shares?",1,100,4, key="new10")
    tickers.append(ticker6)
    amounts.append(amount6)


for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', dt.datetime(2019,8,1), dt.datetime.now())
    price = df[-1:]['Close'][0]
    prices.append(price)
    index = tickers.index(ticker)
    total.append(price * amounts[index])

fig, ax = plt.subplots(figsize=(14,7))

ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')

ax.tick_params(axis='x', color='white')
ax.tick_params(axis='y', color='white')

ax.set_title('Stock Portfolio Visualizer', color="#EF6C35", fontsize=20)

_, texts, _ = ax.pie(total, labels=tickers, autopct='%1.1f%%', pctdistance=0.8)

my_circle = plt.Circle((0,0), 0.60, color='white')
plt.gca().add_artist(my_circle)

ax.text(-2, 1, 'PORTFOLIO OVERVIEW', fontsize=14, color='black', verticalalignment='center', horizontalalignment='center')
ax.text(-2, 0.85, f'Total USD Amount: {sum(total):.2f} $', fontsize=12, color='black', verticalalignment='center', horizontalalignment='center')
counter = 0.15
for ticker in tickers:
    ax.text(-2, 0.85 - counter, f'{ticker}: {total[tickers.index(ticker)]:.2f} $', fontsize=12, color='black', verticalalignment='center', horizontalalignment='center')
    counter += 0.15

st.pyplot(fig)
