import conf
import requests
import csv
from datetime import datetime

# Call API
api_key = conf.alpha_vantage_api_key

# # CSV of Active Stocks
# CSV_URL = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}'

# with requests.Session() as s:
#     download = s.get(CSV_URL)
#     decoded_content = download.content.decode('utf-8')
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         print(row)

# # Filter Out ETFs

def extract_stock_tickers(csv_file_path, years_limit):
    tickers = []
    current_date = datetime.now()
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == 'Stock':
                entry_date = datetime.strptime(row[4], '%Y-%m-%d')
                age = (current_date - entry_date).days / 365.25
                if age > years_limit:
                    tickers.append(row[0])
    return tickers

# # Filter Out Exclusion List

def get_excluded_tickers(config_file_path):
    with open(config_file_path, mode='r') as file:
        excluded_tickers = file.read().splitlines()
    return excluded_tickers

# Example usage
csv_file_path = 'path_to_your_file.csv'
years_limit = 25
config_file_path = 'path_to_config_file.txt'
excluded_tickers = get_excluded_tickers(config_file_path)
stock_tickers = extract_stock_tickers(csv_file_path, years_limit)
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



# One of the most widely used methods of calculating the required rate is the Capital Asset Pricing Model (CAPM). Under the CAPM, the rate is determined using the following formula:

# RRR = rf + ß(rm – rf)
# Where:

# RRR – required rate of return
# rf – risk-free rate
# ß – beta coefficient of an investment
# rm – return of a market
# The CAPM framework adjusts the required rate of return for an investment’s level of risk (measured by the beta) and inflation (assuming that the risk-free rate is adjusted for the inflation level).

# Another method of calculating the required rate is the Weighted Average Cost of Capital (WACC). The WACC approach is frequently utilized in corporate finance. Unlike the CAPM, the WACC takes into consideration the capital structure of a company. Due to this, the required rate obtained from the WACC is used in the corporate decision-making process of undertaking new projects. It can be calculated using the following formula:

# RRR = wDrD(1 – t) + were
# Where:

# wD – weight of debt
# rD – cost of debt
# t – corporate tax rate
# we – weight of equity
# re – cost of equity
# The WACC determines the overall cost of the company’s financing. Therefore, the WACC can be viewed as a break-even return that determines the profitability of a project or an investment decision.

# Dividend growth formula
# DGR = [(Recent dividend (D2) - Previous dividend (D1)) x 100] / Previous dividend. Compounded method formula: Where Dp is the company's dividend value for a specific period (p), Dq is the company's dividend value for the initial period (q), and n is the time difference between p and q.