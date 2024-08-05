# Imports all Config/Env Variables

from dotenv import load_dotenv
import os

load_dotenv('../../.env', override=True)
load_dotenv('../../.conf', override=True)

alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
chatgpt_api_key = os.getenv('CHATGPT_API_KEY')
exclude_these_tickers = os.getenv('EXCLUDE_THESE_TICKERS')
num_of_desired_stocks = os.getenv('NUM_OF_DESIRED_STOCKS')
chatgpt_explanation = os.getenv('CHATGPT_EXPLANATION')
budgeting_feature = os.getenv('BUDGETING_FEATURE')
total_budget = os.getenv('TOTAL_BUDGET')

# # Print all environment variables for debugging
# for key, value in os.environ.items():
#     print(f'{key}: {value}')