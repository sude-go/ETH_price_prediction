import streamlit as st
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

st.set_page_config(page_title="Ethereum Price Predictor", layout="wide")

st.title("Ethereum (ETH) Price Predictor")
st.write("Predict future Ethereum prices using a simple machine learning model.")

# Sidebar for inputs
st.sidebar.header("Configure your prediction")

start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2025-01-01"))
predict_days = st.sidebar.slider("Days to Predict into the Future", 1, 60, 30)

# Button
if st.sidebar.button("Predict Now!"):
    st.subheader("Fetching data and training model...")

    # Download data
    eth = yf.download('ETH-USD', start=start_date, end=end_date)

    if eth.empty:
        st.error("No data found. Please adjust the date range.")
    else:
        # Prepare data
        eth['Date'] = eth.index
        eth['Days'] = (eth['Date'] - eth['Date'].min()).dt.days
        X = eth['Days'].values.reshape(-1, 1)
        y = eth['Close'].values

        # Train model
        model = LinearRegression()
        model.fit(X, y)

        # Cross-validation
        cv_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
        mean_cv_score = np.mean(cv_scores)
        st.write(f"Cross-validation MSE: {-mean_cv_score:.2f}")

        # R-squared error
        y_pred = model.predict(X)
        r2 = r2_score(y, y_pred)
        st.write(f"R-squared: {r2:.4f}")

        # Predict future
        last_day = X[-1][0]
        future_days = np.array(range(last_day + 1, last_day + predict_days + 1)).reshape(-1, 1)
        future_prices = model.predict(future_days)

        # Prepare future dates
        future_dates = pd.date_range(eth['Date'].iloc[-1] + pd.Timedelta(days=1), periods=predict_days)

        # Ensure future_prices and future_dates are 1D arrays
        future_prices = future_prices.flatten()  # Reshape to 1D
        future_dates = future_dates.to_list()  # Convert to list to ensure 1D

        # Plot
        st.subheader("📈 Prediction Graph")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(eth['Date'], y, label='Historical Prices')
        ax.plot(future_dates, future_prices, label='Predicted Prices', linestyle='--')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (USD)')
        ax.set_title('Ethereum (ETH) Price Prediction')
        ax.legend()
        st.pyplot(fig)

        st.subheader("📊 Data Overview")
        col1, col2 = st.columns(2)

        # Show Historical Data
        with col1:
            st.subheader("🗃 Historical Data")
            st.dataframe(eth[['Close']])

        # Show Predicted Future Prices
        with col2:
            st.subheader("🔮 Predicted Future Prices")
            prediction_df = pd.DataFrame({
                'Date': future_dates,
                'Predicted Close Price (USD)': future_prices
            })
            st.dataframe(prediction_df)

else:
    st.info("👈 Adjust the settings and click 'Predict Now!' to see predictions.")
