# Include Main Stock Logic Here
# !! Move to Main when completed !!

import conf
import pipe
import model
import prompts

def chatgpt_option():
    if conf.chatgpt_explanation is True:
        explanation = prompts.get_chatgpt_response()
        return explanation
    else:
        return # Do Nothing

def app_logic():
    # Placeholder for the logic to print results to the terminal
    print("Printing stock selections to the terminal...")

    # Gather Cleaned Data
    pipe.pipeline_execution()

    # Perform Analysis

    stock_decisions = model.analysis_results()

    # # Include ChatGPT Explanation
    
    # # ChatGPT Variables Schema Tuple:
    # stock_info = (
    #     stock_ticker,
    #     stock_name,
    #     stock_div_growth_over_5,
    #     stock_PE,
    #     stock_PB,
    #     stock_debt_to_asset,
    #     stock_assets_liabilities,
    #     stock_growth_projections
    # )

    for picks in stock_decisions:
        pick_explanation = chatgpt_option()


app_logic()