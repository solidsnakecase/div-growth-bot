import conf
import requests
import csv
from datetime import datetime

def active_stock_load():
    api_key = conf.alpha_vantage_api_key

    CSV_URL = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row)

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

def filter_excluded_tickers(config_file_path):
    with open(config_file_path, mode='r') as file:
        excluded_tickers = file.read().splitlines()
    return excluded_tickers

# Example usage
csv_file_path = 'path_to_your_file.csv'
years_limit = 25
config_file_path = 'path_to_config_file.txt'
excluded_tickers = filter_excluded_tickers(config_file_path)
stock_tickers = extract_stock_tickers_by_age(csv_file_path, years_limit)
print(stock_tickers)

# For Tickers in Results
# Filter Out Div and Save Companies who have Div
# If they have Div, save data to CSV/Parquet
function = 'DIVIDENDS' # Dividend History of the company
url = f'https://www.alphavantage.co/query?function={function}&symbol=IBM&apikey={api_key}'
r = requests.get(url)
data = r.json()

print(data)

# Filter Out Div Growth (25 Years)
# Calculate Dividend Growth Model
# Price = Current Annual Dividend / (Desired Rate of Return - Expected Rate of Div Growth)
# See Calculations Below

# For each Selected Stock, Gather Company Overview
function = 'OVERVIEW' # Overview of the company

# Filter Out by Sector

# Return Cleaned Data as Parquet
