# Imports all Config/Env Variables

from dotenv import load_dotenv
import os

load_dotenv('../../.env', override=True)
load_dotenv('../../.conf', override=True)

# Core Variables
alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
num_of_desired_stocks = os.getenv('NUM_OF_DESIRED_STOCKS')
num_of_years_in_existence = os.getenv('NUM_OF_YEARS_IN_EXISTENCE')

# Optional Variables
chatgpt_api_key = os.getenv('CHATGPT_API_KEY')
chatgpt_explanation = os.getenv('CHATGPT_EXPLANATION')
budgeting_feature = os.getenv('BUDGETING_FEATURE')
total_budget = os.getenv('TOTAL_BUDGET')
tickers_to_exclude = os.getenv('EXCLUDE_THESE_TICKERS')
sectors_to_exclude = os.getenv('EXCLUDE_THESE_SECTORS')