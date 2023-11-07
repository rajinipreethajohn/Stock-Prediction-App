# Stock Prediction Web App using Prophet and Streamlit

[![Visit Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stock-prediction-app-2023.streamlit.app/)

This is a web application built with Streamlit, a popular Python library for creating web apps, to predict stock prices using the Prophet forecasting model. Users can select a stock (AAPL, GOOG, MSFT, TSLA) and specify the number of years for the prediction. The app displays the historical stock data, predicts future stock prices, and visualizes the forecasted data and components.
<img width="952" alt="StockPrediction" src="https://github.com/rajinipreethajohn/Stock-Prediction-App/assets/72058664/e1ed8a4f-5ecc-4330-8a7c-5ddd91bfb73f">

<img width="804" alt="stock1" src="https://github.com/rajinipreethajohn/Stock-Prediction-App/assets/72058664/98625ab0-93d4-402d-ae8b-515aa611d2a7">


## Getting Started

### Prerequisites

Make sure you have the following libraries installed:

- Streamlit
- yfinance
- prophet
- plotly

You can install them using `pip`:

```bash
pip install streamlit yfinance prophet plotly
```

### Running the App (Click the OPEN IN STREAMLIT icon on the top of this page to be re-directed to the Streamlit app)

To run the web application, execute the following command in your terminal:

```bash
streamlit run app.py
```

Replace `app.py` with the name of your Python script if it's different.

## Usage

1. When you run the app, it will open in your web browser.
2. Select a stock from the dropdown menu (AAPL, GOOG, MSFT, TSLA).
3. Use the slider to choose the number of years for the prediction.
4. The app will display the raw historical data for the selected stock.
5. It will also show a plot with the stock's open and close prices over time.
6. The app will predict the future stock prices and display the forecasted data and components using interactive Plotly charts.

## Built With

- [Streamlit](https://streamlit.io/) - The web framework used for building the app.
- [yfinance](https://pypi.org/project/yfinance/) - Python module to fetch historical market data from Yahoo Finance.
- [Prophet](https://facebook.github.io/prophet/) - Forecasting tool open-sourced by Facebook Research.
- [Plotly](https://plotly.com/python/) - Interactive graphing library for Python.

## Authors

- Rajini Preetha JOHN (RPJ)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

