import conf
import requests
import csv
from datetime import datetime

# !! SET UP CACHE FOR ACTIVE STOCKS, INVALIDATE QUARTERLY/ANNUALLY !!

# Globals
api_key = conf.alpha_vantage_api_key
years_limit = conf.num_of_years_in_existence

tickers_to_exclude = conf.tickers_to_exclude
sectors_to_exclude = conf.sectors_to_exclude

# Core Functions
def create_parquet():
    return

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
    return tickers

def filter_by_sector(sector):
    filtered_by_sector = []
    return filtered_by_sector

# Main Function
# MAINLY CHATGPT SUGGESTIONS, EDIT BEFORE PROD, FOR SUGGESTION ONLY
def pipeline_execution():
    active_stock_load()
    stock_tickers = extract_stock_tickers_by_age(csv_file_path, years_limit)
   
    # !! SETUP CACHE HERE !!

    # For Tickers in Results
    # Filter Out Div and Save Companies who have Div
    function = 'DIVIDENDS' # Dividend History of the company
    ticker_api_call(function, 'AAPL', api_key)
    # If they have Div, save data to CSV/Parquet

    # Filter Out Div Growth (25 Years)
    # Calculate Dividend Growth Model
    # Price = Current Annual Dividend / (Desired Rate of Return - Expected Rate of Div Growth)
    for ticker in stock_tickers:
        if ticker not in tickers_to_exclude:
            function = 'DIVIDENDS' # Dividend History of the company
            ticker_api_call(function, ticker, api_key)

        # For each Selected Stock, Gather Company Overview
            function = 'OVERVIEW' # Overview of the company
            ticker_api_call(function, ticker, api_key)

# Debugging/Testing
csv_file_path = 'path_to_your_file.csv'
