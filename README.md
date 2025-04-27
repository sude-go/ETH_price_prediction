# Ethereum Price Predictor

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="Ethereum-icon-purple.svg.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">ETH Price Prediction With Linear Regression</h3>
<a href="https://ethpriceprediction.streamlit.app/">Link to Project</a>
</div>


<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)

## About The Project

The Ethereum Price Predictor is a simple machine learning application built to predict future Ethereum (ETH) prices
using historical data. The model is based on linear regression and allows users to predict future Ethereum prices for a
specified range of dates. This project leverages Yahoo Finance's API to fetch historical Ethereum data, and the
predictions are visualized in an interactive plot using Streamlit.

## Built With

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-blue)](https://streamlit.io/)
[![yfinance](https://img.shields.io/badge/yfinance-0.1%2B-green)](https://pypi.org/project/yfinance/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24%2B-yellow)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4%2B-orange)](https://matplotlib.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-lightgreen)](https://pandas.pydata.org/)

## Getting Started

To get started with this project, follow the steps below to set up the project locally.

### Prerequisites

You will need to have Python 3.7 or later installed on your system. It is also recommended to use a virtual environment
to manage dependencies.

- **Python**: 3.7 or later
- **pip**: Package installer for Python

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ethereum-price-predictor.git
    cd ethereum-price-predictor
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # For Linux/MacOS
    .\venv\Scripts\activate    # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the app.

3. Use the sidebar to configure the prediction:
    - Set the **Start Date** and **End Date** for the historical data.
    - Adjust the **Days to Predict into the Future** slider to predict future Ethereum prices.
    - Click the **Predict Now!** button to generate the predictions.

4. You will see a graph showing the historical Ethereum prices and the predicted future prices along with a table of the
   predicted data.

---

[KBD]:https://ethpriceprediction.streamlit.app/




