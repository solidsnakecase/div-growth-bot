import conf
import requests

import csv
import os
import time
from datetime import datetime, timedelta

import polars

# Temp To Do:
#   - Use dataframes to store data
#   - Finish cache_active_stocks function
#   - Finish filter_chain function
#   - Finish ticker_enumeration function
#   - Clean up code

# Globals (Delete when moving to Main)
api_key = conf.alpha_vantage_api_key
years_limit = conf.num_of_years_in_existence

tickers_to_exclude = conf.tickers_to_exclude
sectors_to_exclude = conf.sectors_to_exclude

# Core Functions
def create_parquet(dataframe, file_name):
    """
    Creates a Parquet file from the given data.

    Parameters:
    data (polars.DataFrame): The data to be saved as a Parquet file.
    file_name (str): The name of the output Parquet file.

    Returns:
    None
    """
    dataframe.write_parquet(file_name)

# Example usage:
# df = polars.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
# create_parquet(df, 'output.parquet')

def ticker_api_call(function, ticker, api_key):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()

    print(data) # Remove for Production
    # return data # Production: Save to Parquet

# Pipeline Functions

def active_stock_load():
    # Custom API Endpoint Call
    CSV_URL = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row) # Remove for Production
            # return row # Production: Save to Parquet

def extract_stock_tickers_by_age(csv_file_path, years_limit):
    tickers = []
    current_date = datetime.now()
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == 'Stock': # Filter out ETFs
                entry_date = datetime.strptime(row[4], '%Y-%m-%d')
                age = (current_date - entry_date).days / 365.25
                if age > years_limit:
                    tickers.append(row[0])
    return tickers # CHANGE THIS TO SAVE TO DATAFRAME, THEN PARQUET FUNCTION
    dataframe =
    create_parquet(dataframe, 'active_stocks_filtered_by_age.parquet')

def sector_filter(sector):
    filtered_by_sector = []
    return filtered_by_sector

def div_filter():
    stock_tickers = # Extracted Tickers
    for ticker in stock_tickers:
    # For Tickers in Results
    # Filter Out Div and Save Companies who have Div
    function = 'DIVIDENDS' # Dividend History of the company
    div_filter = ticker_api_call(function, 'AAPL', api_key)
    # If they have Div, save data to CSV/Parquet
    return

def div_growth_filter():
    stock_tickers = # Extracted Tickers
    for ticker in stock_tickers:
    # Filter Out Div Growth (25 Years)
    # Calculate Dividend Growth Model
    # Price = Current Annual Dividend / (Desired Rate of Return - Expected Rate of Div Growth)
    dataframe =
    create_parquet(dataframe, 'filtered_by_div_growth.parquet')


# Function Flow
def cache_active_stocks(function, *args, **kwargs):
    one_year_ago = datetime.now() - timedelta(days=365)
    
    # Check if file exists and is less than 1 year old, then cache if not
    file_path = '/data/active_stocks_filtered_by_age.parquet'
    if os.path.exists(file_path):
        file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
        if file_creation_time > one_year_ago:
            print(f"Using cached file: {file_path}")
            return  # File is valid, no need to run the function
    
    # Fix Below Code

    active_stock_load()
    extract_stock_tickers_by_age(csv_file_path, years_limit)

    # # File does not exist or is older than 1 year, run the function
    # print(f"Running function and caching result to: {file_path}")
    # result = function(*args, **kwargs)
    # create_parquet(result, file_path)

def filter_chain():
    sector_filter()
    div_filter()
    div_growth_filter()

def ticker_enumeration():
    # For each Selected Stock, Gather Company Overview
    function = 'OVERVIEW' # Overview of the company
    ticker_enumeration = ticker_api_call(function, ticker, api_key)
    create_parquet(ticker_enumeration, 'cleaned_dataset.parquet')

# Main Function
def pipeline_execution():
    cache_active_stocks()
    filter_chain()
    ticker_enumeration()

# Debugging/Testing
print(pipeline_execution())
