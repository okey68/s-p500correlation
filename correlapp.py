import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Stock Correlation App')
st.header('Enter two stock tickers to find their correlation')

stock1 = st.text_input("ticker", 'AAPL')
stock2 = st.text_input("ticker", 'KO') 

# data as of 12/2020. will need to update
df = pd.read_csv('sp500_joined_closes.csv')

##df['AAPL'].plot()
##plt.show()

df_corr = df.corr()
##print(df_corr.head())

correl = df_corr.loc[stock1,stock2]
#print("Correlation of",stock1,"&", stock2, "is:",correl)

st.beta_container(3)

st.write("The correlation between",stock1,"&", stock2, "is:",correl)


