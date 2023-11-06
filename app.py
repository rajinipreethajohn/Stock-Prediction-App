import streamlit as st
from datetime import date
import yfinance as yf
import prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from prophet import Prophet



START = "2013-11-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

stocks = ("AAPL", "GOOG", "MSFT", "TSLA")

selected_stock = st.selectbox("Select dataset for prediction", stocks)

n_years = st.slider("Years of prediction: ", 1, 10)

period = n_years * 365

@st.cache_data
def load_data(ticker):
  data= yf.download(ticker, START, TODAY)
  data.reset_index(inplace=True)
  return data

data_load_sate = st.text("Loading....")
data = load_data(selected_stock)

data_load_sate.text("Loading DONE!")

st.subheader("Raw data")
st.write(data.tail())

def plot_raw_data():
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=data['Date'], y=data["Open"], name= "stock_open",line=dict(color='red')))
  fig.add_trace(go.Scatter(x=data['Date'], y=data["Close"], name= "stock_close",line=dict(color='blue')))
  fig.layout.update(title_text= "Time Series Data", xaxis_rangeslider_visible=True)

  st.plotly_chart(fig)

plot_raw_data()

#Forecasting

df_train = data[["Date", "Close"]]

#renaming column as fbprohept expects it a certain way
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

#Instantiate the model
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecast data")
st.write(forecast.tail())

st.write("Forecast data")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)






