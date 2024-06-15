# # import streamlit as st 
# # import pandas as pd
# # import yfinance as yf
# # import numpy as np
# # import matplotlib.pyplot as plt


# # st.title("Stock Market Analyzer")
# # st.subheader("Analyze Any Stock")
# # # st.header("Hi! I am Header")
# # st.text("Hi! I am Stock Analyst")
# # # st.markdown("This is Good 😄")

# # # sidebar

# # month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
# #               'November', 'December']

# # list_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
# #             30, 31]


# # st.sidebar.header("Stock Analysis")
# # st.sidebar.subheader("Start Info")
# # month_s = st.sidebar.selectbox('Month Start',month_list)
# # day_s = st.sidebar.selectbox("Day Start",list_day)
# # year_s  = st.sidebar.text_input("Enter the Start Year")

# # st.sidebar.subheader("End Info")

# # month_e = st.sidebar.selectbox('Month End',month_list)
# # day_e = st.sidebar.selectbox("Day End",list_day)
# # year_e = st.sidebar.text_input("Enter the Ending Year")




# # # st.sidebar.subheader("Stock Section")

# # # stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock")


# # tickers = ["KO","MSFT","GOOGL","NVDA","INTC"]
# # stocks = yf.download(tickers,start="1993-1-1",end = "2022-1-1")
# # # stocks = yf.download(tickers, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")

# # if(st.sidebar.button('Analyze')):
# #  inf = ["Close","Open"]
# #  close = stocks.loc[:,"Close"]
# #  dataframe = stocks.loc[:,inf]
# #  st.dataframe(dataframe)
# #  plt.style.use("seaborn")
# #  st.line_chart(close)


# # import streamlit as st 
# # import pandas as pd
# # import yfinance as yf

# # st.title("Stock Market Analyzer")
# # st.subheader("Analyze Any Stock")
# # st.text("Hi! I am Stock Analyst")

# # # sidebar
# # month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
# #               'November', 'December']

# # list_day = list(range(1, 32))

# # st.sidebar.header("Stock Analysis")
# # st.sidebar.subheader("Start Info")
# # month_s = st.sidebar.selectbox('Month Start', month_list)
# # day_s = st.sidebar.selectbox("Day Start", list_day)
# # year_s = st.sidebar.text_input("Enter the Start Year")

# # st.sidebar.subheader("End Info")
# # month_e = st.sidebar.selectbox('Month End', month_list)
# # day_e = st.sidebar.selectbox("Day End", list_day)
# # year_e = st.sidebar.text_input("Enter the Ending Year")

# # st.sidebar.subheader("Stock Section")
# # stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock")

# # if st.sidebar.button('Analyze'):
# #     stocks = yf.download(stock_to_for_info, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")
    
# #     if not stocks.empty:
# #         inf = ["Close","Open"]
# #         close = stocks.loc[:,"Close"]
# #         dataframe = stocks[inf]
# #         st.dataframe(dataframe)
# #         st.line_chart(close)
# #     else:
# #         st.write("No data available for the specified stock symbol and date range.")


# # import streamlit as st 
# # import pandas as pd
# # import yfinance as yf

# # st.title("Stock Market Analyzer")
# # st.subheader("Analyze Any Stock")
# # st.text("Hi! I am Stock Analyst")

# # # sidebar
# # month_list = list(range(1,13))

# # list_day = list(range(1, 32))

# # st.sidebar.header("Stock Analysis")
# # st.sidebar.subheader("Start Info")
# # month_s = st.sidebar.selectbox('Month Start', month_list)
# # day_s = st.sidebar.selectbox("Day Start", list_day)
# # year_s = st.sidebar.text_input("Enter the Start Year")

# # st.sidebar.subheader("End Info")
# # month_e = st.sidebar.selectbox('Month End', month_list)
# # day_e = st.sidebar.selectbox("Day End", list_day)
# # year_e = st.sidebar.text_input("Enter the Ending Year")

# # st.sidebar.subheader("Stock Section")
# # stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock")

# # if st.sidebar.button('Analyze'):
# #     st.write(f"Stock Symbol: {stock_to_for_info}")
# #     st.write(f"Start Date: {year_s}-{month_s}-{day_s}")
# #     st.write(f"End Date: {year_e}-{month_e}-{day_e}")

# #     stocks = yf.download(stock_to_for_info, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")
    
# #     if not stocks.empty:
# #         inf = ["Close","Open"]
# #         close = stocks.loc[:, "Close"]
# #         dataframe = stocks[inf]
# #         st.dataframe(dataframe)
# #         st.line_chart(close)
# #     else:
# #         st.write("No data available for the specified stock symbol and date range.")
# # ------------------------------------------------------------------------------------------------
# # correct code hai

# # import streamlit as st 
# # import pandas as pd
# # import yfinance as yf

# # st.title("Stock Market Analyzer")
# # st.subheader("Analyze Any Stock")
# # st.text("Hi! I am Stock Analyst")

# # # sidebar
# # month_list = list(range(1,13))

# # list_day = list(range(1, 32))

# # st.sidebar.header("Stock Analysis")
# # st.sidebar.subheader("Start Info")
# # month_s = st.sidebar.selectbox('Month Start', month_list)
# # day_s = st.sidebar.selectbox("Day Start", list_day)
# # year_s = st.sidebar.text_input("Enter the Start Year")

# # st.sidebar.subheader("End Info")
# # month_e = st.sidebar.selectbox('Month End', month_list)
# # day_e = st.sidebar.selectbox("Day End", list_day)
# # year_e = st.sidebar.text_input("Enter the Ending Year")

# # st.sidebar.subheader("Stock Section")
# # stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock (comma-separated if multiple)")

# # if st.sidebar.button('Analyze'):
# #     stocks_to_analyze = [stock.strip() for stock in stock_to_for_info.split(',')]
    
# #     all_stocks_close = pd.DataFrame()  # Initialize an empty DataFrame to hold closing prices of all stocks
    
# #     for stock_symbol in stocks_to_analyze:
# #         stocks = yf.download(stock_symbol, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")

# #         if not stocks.empty:
# #             close = stocks["Close"]
# #             all_stocks_close[stock_symbol] = close  # Add closing prices of this stock to the DataFrame
# #         else:
# #             st.write(f"No data available for the specified stock symbol '{stock_symbol}' and date range.")
    
# #     if not all_stocks_close.empty:
# #         st.write("Closing Prices for Selected Stocks:")
# #         st.dataframe(all_stocks_close)
        
# #         st.write("Closing Prices Chart:")
# #         st.line_chart(all_stocks_close)
# #         st.scatter_chart(all_stocks_close)
# #     else:
# #         st.write("No data available for the specified stock symbols and date range.")
# # ----------------------------------------------------------------------------------------------------

# # import streamlit as st 
# # import pandas as pd
# # import yfinance as yf

# # st.title("Stock Market Analyzer")
# # st.subheader("Analyze Any Stock")
# # st.text("Hi! I am Stock Analyst")

# # # sidebar
# # month_list = list(range(1,13))

# # list_day = list(range(1, 32))

# # st.sidebar.header("Stock Analysis")
# # st.sidebar.subheader("Start Info")
# # month_s = st.sidebar.selectbox('Month Start', month_list)
# # day_s = st.sidebar.selectbox("Day Start", list_day)
# # year_s = st.sidebar.text_input("Enter the Start Year")

# # st.sidebar.subheader("End Info")
# # month_e = st.sidebar.selectbox('Month End', month_list)
# # day_e = st.sidebar.selectbox("Day End", list_day)
# # year_e = st.sidebar.text_input("Enter the Ending Year")

# # st.sidebar.subheader("Stock Section")
# # stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock (comma-separated if multiple)")

# # if st.sidebar.button('Analyze'):
# #     stocks_to_analyze = [stock.strip() for stock in stock_to_for_info.split(',')]
    
# #     all_stocks_close = pd.DataFrame()  # Initialize an empty DataFrame to hold closing prices of all stocks
    
# #     first_date = None
# #     last_date = None
    
# #     for stock_symbol in stocks_to_analyze:
# #         stocks = yf.download(stock_symbol, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")

# #         if not stocks.empty:
# #             close = stocks["Close"]
# #             all_stocks_close[stock_symbol] = close  # Add closing prices of this stock to the DataFrame
            
# #             # Update first and last date
# #             if first_date is None or stocks.index.min() < first_date:
# #                 first_date = stocks.index.min()
# #             if last_date is None or stocks.index.max() > last_date:
# #                 last_date = stocks.index.max()
            
# #             # Get opening and closing prices at start and end dates
# #             start_open_price = stocks.loc[stocks.index[0], "Open"]
# #             start_close_price = stocks.loc[stocks.index[0], "Close"]
# #             end_open_price = stocks.loc[stocks.index[-1], "Open"]
# #             end_close_price = stocks.loc[stocks.index[-1], "Close"]
# #             precentage_gain = ((end_close_price-start_close_price)/start_close_price)*100
            
# #             st.info(f"Stock: {stock_symbol}")
# #             st.write(f"Start Date: {stocks.index[0].strftime('%Y-%m-%d')}")
# #             st.write(f"Start Open Price: {start_open_price}")
# #             # st.write(f"Start Close Price: {start_close_price}")
# #             st.write(f"End Date: {stocks.index[-1].strftime('%Y-%m-%d')}")
# #             # st.write(f"End Open Price: {end_open_price}")
# #             st.write(f"End Close Price: {end_close_price}")
# #             if(precentage_gain>=0):
# #              st.success(f"Percentage Gain is: {precentage_gain}")
# #             else:
# #                 st.error(precentage_gain)
            
# #         else:
# #             st.write(f"No data available for the specified stock symbol '{stock_symbol}' and date range.")
    
# #     if not all_stocks_close.empty:
# #         st.write("Closing Prices for Selected Stocks:")
# #         st.dataframe(all_stocks_close)
        
# #         st.write("Closing Prices Chart:")
# #         st.line_chart(all_stocks_close)
        
# #         st.write(f"First Date: {first_date.strftime('%Y-%m-%d') if first_date else 'N/A'}")
# #         st.write(f"Last Date: {last_date.strftime('%Y-%m-%d') if last_date else 'N/A'}")
# #     else:
# #         st.write("No data available for the specified stock symbols and date range.")

# # ---------------------------------------------------------------------------------------------
# # import streamlit as st 
# # import pandas as pd
# # import yfinance as yf

# # st.title("Stock Market Analyzer")
# # st.subheader("Analyze Any Stock")
# # st.text("Hi! I am Stock Analyst")

# # # Sidebar options
# # CHART_TYPES = ['Line Chart', 'Bar Chart']

# # # Sidebar
# # month_list = list(range(1,13))
# # list_day = list(range(1, 32))

# # st.sidebar.header("Stock Analysis")
# # st.sidebar.subheader("Start Info")
# # month_s = st.sidebar.selectbox('Month Start', month_list)
# # day_s = st.sidebar.selectbox("Day Start", list_day)
# # year_s = st.sidebar.text_input("Enter the Start Year")

# # st.sidebar.subheader("End Info")
# # month_e = st.sidebar.selectbox('Month End', month_list)
# # day_e = st.sidebar.selectbox("Day End", list_day)
# # year_e = st.sidebar.text_input("Enter the Ending Year")

# # st.sidebar.subheader("Stock Section")
# # stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock (comma-separated if multiple)")

# # # Chart type selection
# # chart_type = st.sidebar.selectbox("Select Chart Type", CHART_TYPES)

# # if st.sidebar.button('Analyze'):
# #     stocks_to_analyze = [stock.strip() for stock in stock_to_for_info.split(',')]
    
# #     all_stocks_close = pd.DataFrame()  # Initialize an empty DataFrame to hold closing prices of all stocks
    
# #     first_date = None
# #     last_date = None
    
# #     for stock_symbol in stocks_to_analyze:
# #         stocks = yf.download(stock_symbol, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")

# #         if not stocks.empty:
# #             close = stocks["Close"]
# #             all_stocks_close[stock_symbol] = close  # Add closing prices of this stock to the DataFrame
            
# #             # Update first and last date
# #             if first_date is None or stocks.index.min() < first_date:
# #                 first_date = stocks.index.min()
# #             if last_date is None or stocks.index.max() > last_date:
# #                 last_date = stocks.index.max()
            
# #             # Get opening and closing prices at start and end dates
# #             start_open_price = stocks.loc[stocks.index[0], "Open"]
# #             start_close_price = stocks.loc[stocks.index[0], "Close"]
# #             end_open_price = stocks.loc[stocks.index[-1], "Open"]
# #             end_close_price = stocks.loc[stocks.index[-1], "Close"]
# #             precentage_gain = ((end_close_price-start_close_price)/start_close_price)*100
            
# #             st.info(f"Stock: {stock_symbol}")
# #             st.write(f"Start Date: {stocks.index[0].strftime('%Y-%m-%d')}")
# #             st.write(f"Start Open Price: {start_open_price}")
# #             # st.write(f"Start Close Price: {start_close_price}")
# #             st.write(f"End Date: {stocks.index[-1].strftime('%Y-%m-%d')}")
# #             # st.write(f"End Open Price: {end_open_price}")
# #             st.write(f"End Close Price: {end_close_price}")
# #             if(precentage_gain>=0):
# #              st.success(f"Percentage Gain is: {precentage_gain} %")
# #             else:
# #                 st.error(f"Percentage Loss is: {precentage_gain} %")
            
# #         else:
# #             st.write(f"No data available for the specified stock symbol '{stock_symbol}' and date range.")
    
# #     if not all_stocks_close.empty:
# #         st.write("Closing Prices for Selected Stocks:")
# #         st.dataframe(all_stocks_close)
        
# #         st.write("Closing Prices Chart:")
# #         if chart_type == 'Line Chart':
# #             st.line_chart(all_stocks_close)
# #         elif chart_type == 'Bar Chart':
# #             st.bar_chart(all_stocks_close)
# #         st.write(f"First Date: {first_date.strftime('%Y-%m-%d') if first_date else 'N/A'}")
# #         st.write(f"Last Date: {last_date.strftime('%Y-%m-%d') if last_date else 'N/A'}")
# #     else:
# #         st.write("No data available for the specified stock symbols and date range.")
# # --------------------------------------------------------------------------------



# import streamlit as st 
# import pandas as pd
# from datetime import datetime
# import yfinance as yf
# from nsepy import get_history

# st.title("Stock Market Analyzer")
# st.subheader("Analyze Any Stock")
# st.text("Hi! I am Stock Analyst")

# # Sidebar options
# CHART_TYPES = ['Line Chart', 'Bar Chart']

# # Sidebar
# month_list = list(range(1,13))
# if(month_list%2 != 0):
#  list_day = list(range(1, 32))
# elif(month_list==2):
#  list_day = list(range(1,29))
# else:
#     list_day = list(range(1,31))
# st.sidebar.header("Stock Analysis")
# st.sidebar.subheader("Start Info")
# month_s = st.sidebar.selectbox('Month Start', month_list)
# day_s = st.sidebar.selectbox("Day Start", list_day)
# year_s = st.sidebar.text_input("Enter the Start Year")

# st.sidebar.subheader("End Info")
# month_e = st.sidebar.selectbox('Month End', month_list)
# day_e = st.sidebar.selectbox("Day End", list_day)
# year_e = st.sidebar.text_input("Enter the Ending Year")

# st.sidebar.subheader("Stock Section")
# stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock (comma-separated if multiple)")

# # Additional features
# show_high_low = st.sidebar.checkbox("Show High and Low Prices")
# show_volume = st.sidebar.checkbox("Show Volume")
# time_interval = st.sidebar.selectbox("Select Time Interval", ['Daily', 'Weekly', 'Monthly'])
# time_period = st.sidebar.selectbox("Filter by Time Period", ['Last 30 Days', 'Last 6 Months', 'Last 1 Year'])

# # Chart type selection
# chart_type = st.sidebar.selectbox("Select Chart Type", CHART_TYPES)

# if st.sidebar.button('Analyze'):
#     stocks_to_analyze = [stock.strip() for stock in stock_to_for_info.split(',')]
    
#     all_stocks_close = pd.DataFrame()  # Initialize an empty DataFrame to hold closing prices of all stocks
    
#     first_date = None
#     last_date = None
    
#     for stock_symbol in stocks_to_analyze:
#         stocks = yf.download(stock_symbol, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")

#         if not stocks.empty:
#             close = stocks["Close"]
#             all_stocks_close[stock_symbol] = close  # Add closing prices of this stock to the DataFrame
            
#             # Update first and last date
#             if first_date is None or stocks.index.min() < first_date:
#                 first_date = stocks.index.min()
#             if last_date is None or stocks.index.max() > last_date:
#                 last_date = stocks.index.max()
            
#             # Additional features
#             if show_high_low:
#                 high = stocks["High"]
#                 low = stocks["Low"]
#                 st.write(f"High Price: {high.max()} | Low Price: {low.min()}")
            
#             if show_volume:
#                 volume = stocks["Volume"]
#                 st.write(f"Volume: {volume.sum()}")
            
#             if time_interval == 'Weekly':
#                 stocks = stocks.resample('W').mean()
#             elif time_interval == 'Monthly':
#                 stocks = stocks.resample('M').mean()
            
#             # Get opening and closing prices at start and end dates
#             start_open_price = stocks.loc[stocks.index[0], "Open"]
#             start_close_price = stocks.loc[stocks.index[0], "Close"]
#             end_open_price = stocks.loc[stocks.index[-1], "Open"]
#             end_close_price = stocks.loc[stocks.index[-1], "Close"]
#             precentage_gain = ((end_close_price-start_close_price)/start_close_price)*100
            
#             st.info(f"Stock: {stock_symbol}")
#             st.write(f"Start Date: {stocks.index[0].strftime('%Y-%m-%d')}")
#             st.write(f"Start Open Price: {start_open_price}")
#             # st.write(f"Start Close Price: {start_close_price}")
#             st.write(f"End Date: {stocks.index[-1].strftime('%Y-%m-%d')}")
#             # st.write(f"End Open Price: {end_open_price}")
#             st.write(f"End Close Price: {end_close_price}")
#             if(precentage_gain>=0):
#              st.success(f"Percentage Gain is: {precentage_gain} %")
#             else:
#                 st.error(f"Percentage Loss is: {precentage_gain} %")
            
#         else:
#             st.write(f"No data available for the specified stock symbol '{stock_symbol}' and date range.")
    
#     if not all_stocks_close.empty:
#         st.write("Closing Prices for Selected Stocks:")
#         st.dataframe(all_stocks_close)
        
#         st.write("Closing Prices Chart:")
#         if chart_type == 'Line Chart':
#             st.line_chart(all_stocks_close)
#         elif chart_type == 'Bar Chart':
#             st.bar_chart(all_stocks_close)
#         st.write(f"First Date: {first_date.strftime('%Y-%m-%d') if first_date else 'N/A'}")
#         st.write(f"Last Date: {last_date.strftime('%Y-%m-%d') if last_date else 'N/A'}")
#     else:
#         st.write("No data available for the specified stock symbols and date range.")


# import streamlit as st 
# import pandas as pd
# import yfinance as yf

# st.title("Stock Market Analyzer")
# st.subheader("Analyze Any Stock")
# st.text("Hi! I am Stock Analyst")

# # Sidebar options
# CHART_TYPES = ['Line Chart', 'Bar Chart']

# # Sidebar
# month_list = list(range(1, 13))

# # Create the list_day dynamically based on selected month
# def get_days_in_month(month):
#     if month == 2:
#         return list(range(1, 30))
#     elif month in [4, 6, 9, 11]:
#         return list(range(1, 31))
#     else:
#         return list(range(1, 32))

# st.sidebar.header("Stock Analysis")
# st.sidebar.subheader("Start Info")
# month_s = st.sidebar.selectbox('Month Start', month_list)
# day_s = st.sidebar.selectbox("Day Start", get_days_in_month(month_s))
# year_s = st.sidebar.text_input("Enter the Start Year")

# st.sidebar.subheader("End Info")
# month_e = st.sidebar.selectbox('Month End', month_list)
# day_e = st.sidebar.selectbox("Day End", get_days_in_month(month_e))
# year_e = st.sidebar.text_input("Enter the Ending Year")

# st.sidebar.subheader("Stock Section")
# stock_to_for_info = st.sidebar.text_input("Enter the name Of The Stock (comma-separated if multiple)")

# # Additional features
# show_high_low = st.sidebar.checkbox("Show High and Low Prices")
# show_volume = st.sidebar.checkbox("Show Volume")
# time_interval = st.sidebar.selectbox("Select Time Interval", ['Daily', 'Weekly', 'Monthly'])
# time_period = st.sidebar.selectbox("Filter by Time Period", ['Last 30 Days', 'Last 6 Months', 'Last 1 Year'])

# # Chart type selection
# chart_type = st.sidebar.selectbox("Select Chart Type", CHART_TYPES)

# if st.sidebar.button('Analyze'):
#     stocks_to_analyze = [stock.strip() for stock in stock_to_for_info.split(',')]
    
#     all_stocks_close = pd.DataFrame()  # Initialize an empty DataFrame to hold closing prices of all stocks
    
#     first_date = None
#     last_date = None
    
#     for stock_symbol in stocks_to_analyze:
#         stocks = yf.download(stock_symbol, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")

#         if not stocks.empty:
#             close = stocks["Close"]
#             all_stocks_close[stock_symbol] = close  # Add closing prices of this stock to the DataFrame
            
#             # Update first and last date
#             if first_date is None or stocks.index.min() < first_date:
#                 first_date = stocks.index.min()
#             if last_date is None or stocks.index.max() > last_date:
#                 last_date = stocks.index.max()
            
#             # Additional features
#             if show_high_low:
#                 high = stocks["High"]
#                 low = stocks["Low"]
#                 st.write(f"High Price: {high.max()} | Low Price: {low.min()}")
            
#             if show_volume:
#                 volume = stocks["Volume"]
#                 st.write(f"Volume: {volume.sum()}")
            
#             if time_interval == 'Weekly':
#                 stocks = stocks.resample('W').mean()
#             elif time_interval == 'Monthly':
#                 stocks = stocks.resample('M').mean()
            
#             # Get opening and closing prices at start and end dates
#             start_open_price = stocks.loc[stocks.index[0], "Open"]
#             start_close_price = stocks.loc[stocks.index[0], "Close"]
#             end_open_price = stocks.loc[stocks.index[-1], "Open"]
#             end_close_price = stocks.loc[stocks.index[-1], "Close"]
#             percentage_gain = ((end_close_price - start_close_price) / start_close_price) * 100
            
#             st.info(f"Stock: {stock_symbol}")
#             st.write(f"Start Date: {stocks.index[0].strftime('%Y-%m-%d')}")
#             st.write(f"Start Open Price: {start_open_price}")
#             st.write(f"End Date: {stocks.index[-1].strftime('%Y-%m-%d')}")
#             st.write(f"End Close Price: {end_close_price}")
#             if percentage_gain >= 0:
#                 st.success(f"Percentage Gain: {percentage_gain:.2f}%")
#             else:
#                 st.error(f"Percentage Loss: {percentage_gain:.2f}%")
            
#         else:
#             st.write(f"No data available for the specified stock symbol '{stock_symbol}' and date range.")
    
#     if not all_stocks_close.empty:
#         st.write("Closing Prices for Selected Stocks:")
#         st.dataframe(all_stocks_close)
        
#         st.write("Closing Prices Chart:")
#         if chart_type == 'Line Chart':
#             st.line_chart(all_stocks_close)
#         elif chart_type == 'Bar Chart':
#             st.bar_chart(all_stocks_close)
        
#         st.write(f"First Date: {first_date.strftime('%Y-%m-%d') if first_date else 'N/A'}")
#         st.write(f"Last Date: {last_date.strftime('%Y-%m-%d') if last_date else 'N/A'}")
#     else:
#         st.write("No data available for the specified stock symbols and date range.")



import streamlit as st
import pandas as pd
import yfinance as yf
import requests

st.title("Stock Market Analyzer")
st.subheader("Analyze Any Stock")
st.text("Hi! I am Stock Analyst")

# Alpha Vantage API key (replace with your own API key)
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

# Function to get ticker symbol from company name
def get_ticker_symbol(company_name, api_key):
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "bestMatches" in data and data["bestMatches"]:
        return data["bestMatches"][0]["1. symbol"]
    else:
        return None

# Sidebar options
CHART_TYPES = ['Line Chart', 'Bar Chart']

# Sidebar
month_list = list(range(1, 13))

# Create the list_day dynamically based on selected month
def get_days_in_month(month):
    if month == 2:
        return list(range(1, 30))
    elif month in [4, 6, 9, 11]:
        return list(range(1, 31))
    else:
        return list(range(1, 32))

st.sidebar.header("Stock Analysis")
st.sidebar.subheader("Start Info")
month_s = st.sidebar.selectbox('Month Start', month_list)
day_s = st.sidebar.selectbox("Day Start", get_days_in_month(month_s))
year_s = st.sidebar.text_input("Enter the Start Year")

st.sidebar.subheader("End Info")
month_e = st.sidebar.selectbox('Month End', month_list)
day_e = st.sidebar.selectbox("Day End", get_days_in_month(month_e))
year_e = st.sidebar.text_input("Enter the Ending Year")

st.sidebar.subheader("Stock Section")
company_names = st.sidebar.text_input("Enter the names of the companies (comma-separated if multiple)")

# Additional features
show_high_low = st.sidebar.checkbox("Show High and Low Prices")
show_volume = st.sidebar.checkbox("Show Volume")
time_interval = st.sidebar.selectbox("Select Time Interval", ['Daily', 'Weekly', 'Monthly'])
time_period = st.sidebar.selectbox("Filter by Time Period", ['Last 30 Days', 'Last 6 Months', 'Last 1 Year'])

# Chart type selection
chart_type = st.sidebar.selectbox("Select Chart Type", CHART_TYPES)

if st.sidebar.button('Analyze'):
    company_list = [company.strip() for company in company_names.split(',')]
    ticker_symbols = []
    
    for company in company_list:
        ticker_symbol = get_ticker_symbol(company, API_KEY)
        if ticker_symbol:
            ticker_symbols.append(ticker_symbol)
        else:
            st.write(f"Could not find ticker symbol for the company '{company}'.")
    
    if ticker_symbols:
        all_stocks_close = pd.DataFrame()
        first_date = None
        last_date = None
        
        for ticker_symbol in ticker_symbols:
            stocks = yf.download(ticker_symbol, start=f"{year_s}-{month_s}-{day_s}", end=f"{year_e}-{month_e}-{day_e}")
            
            if not stocks.empty:
                close = stocks["Close"]
                all_stocks_close[ticker_symbol] = close
                
                # Update first and last date
                if first_date is None or stocks.index.min() < first_date:
                    first_date = stocks.index.min()
                if last_date is None or stocks.index.max() > last_date:
                    last_date = stocks.index.max()

                if show_high_low:
                    high = stocks["High"]
                    low = stocks["Low"]
                    st.write(f"High Price: {high.max()} | Low Price: {low.min()}")

                if show_volume:
                    volume = stocks["Volume"]
                    st.write(f"Volume: {volume.sum()}")
                
                if time_interval == 'Weekly':
                    stocks = stocks.resample('W').mean()
                elif time_interval == 'Monthly':
                    stocks = stocks.resample('M').mean()

                start_open_price = stocks.loc[stocks.index[0], "Open"]
                start_close_price = stocks.loc[stocks.index[0], "Close"]
                end_open_price = stocks.loc[stocks.index[-1], "Open"]
                end_close_price = stocks.loc[stocks.index[-1], "Close"]
                percentage_gain = ((end_close_price - start_close_price) / start_close_price) * 100
                
                st.info(f"Stock: {ticker_symbol}")
                st.write(f"Start Date: {stocks.index[0].strftime('%Y-%m-%d')}")
                st.write(f"Start Open Price: {start_open_price}")
                st.write(f"End Date: {stocks.index[-1].strftime('%Y-%m-%d')}")
                st.write(f"End Close Price: {end_close_price}")
                if percentage_gain >= 0:
                    st.success(f"Percentage Gain: {percentage_gain:.2f}%")
                else:
                    st.error(f"Percentage Loss: {percentage_gain:.2f}%")
            else:
                st.write(f"No data available for the specified stock symbol '{ticker_symbol}' and date range.")
        
        if not all_stocks_close.empty:
            st.write("Closing Prices for Selected Stocks:")
            st.dataframe(all_stocks_close)

            st.write("Closing Prices Chart:")
            if chart_type == 'Line Chart':
                st.line_chart(all_stocks_close)
            elif chart_type == 'Bar Chart':
                st.bar_chart(all_stocks_close)

            st.write(f"First Date: {first_date.strftime('%Y-%m-%d') if first_date else 'N/A'}")
            st.write(f"Last Date: {last_date.strftime('%Y-%m-%d') if last_date else 'N/A'}")
    else:
        st.write("No valid ticker symbols found for the provided company names.")
        
        
        
        