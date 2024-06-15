# Trading-Algorithms
Designed a Streamlit app for Analyzing US stocks using yfinance library.
Stock Market Analyzer
Overview
The Stock Market Analyzer is a Streamlit web application that allows users to analyze stock market data for multiple companies. Users can enter company names, specify the date range, and view various stock metrics, including high/low prices, volume, and percentage gains/losses. The application also provides options to visualize closing prices using line or bar charts.

Features
Input multiple company names to analyze their stocks.
Convert company names to ticker symbols using Alpha Vantage API.
Specify the date range for stock data analysis.
Display high and low prices, trading volume, and percentage gain/loss.
Choose time intervals for data resampling (Daily, Weekly, Monthly).
Visualize closing prices with line or bar charts.
Libraries Required
To run this project, you need the following Python libraries:

streamlit: To create the web application interface.
pandas: For data manipulation and analysis.
yfinance: To fetch stock data from Yahoo Finance.
requests: To make API calls to Alpha Vantage.
Installation
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/stock-market-analyzer.git
cd stock-market-analyzer
Install Required Libraries:
Create a virtual environment and install the required libraries using pip:

sh
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
pip install streamlit pandas yfinance requests
Get Alpha Vantage API Key:
Sign up on Alpha Vantage to get a free API key. Replace YOUR_ALPHA_VANTAGE_API_KEY in the code with your actual API key.

Usage
Run the Application:
Execute the Streamlit application by running:

sh
Copy code
streamlit run stock_analyzer.py
Interact with the Application:

Enter the company names (comma-separated if multiple) in the sidebar.
Specify the start and end dates.
Choose additional features like showing high/low prices, volume, and resampling intervals.
Select the chart type for visualizing closing prices.
Click the "Analyze" button to view the results.
