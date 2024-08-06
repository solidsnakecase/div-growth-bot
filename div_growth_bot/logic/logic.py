# Include Main Stock Logic Here
# !! Move to Main when completed !!

import conf
import pipe

def app_logic():
    # Placeholder for the logic to print results to the terminal
    print("Printing stock selections to the terminal...")

    # Gather Cleaned Data
    print(pipe.pipeline_execution())

    # Perform Analysis

    # # Include ChatGPT Explanation
    # !! MAKE STRUCT OUT OF RESULTS WITH FOLLOWING SCHEMA !!

    # ChatGPT Variables Schema:
    # stock_ticker =
    # stock_name =
    # stock_div_growth_over_5 =
    # stock_P/E = 
    # stock_P/B = 
    # stock_debt_to_asset =
    # stock_assets_liabilities =
    # stock_growth_projections =

    if conf.chatgpt_explanation is True:
        # Call ChatGPT Function
        print("ChatGPT Explanation is True")
    else:
        # Do Nothing
        print("ChatGPT Explanation is False")

app_logic()