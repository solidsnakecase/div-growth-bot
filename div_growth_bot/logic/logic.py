# Include Main Stock Logic Here

import conf
import pipe

# Gather Cleaned Data

# Perform Analysis

# # Selected Variables
#   - Chosen Stock Ticker
#       > Full Name
#       > P/E
#       > P/B
#       > Div Growth
#       > Price Projection

# # Include ChatGPT Explanation
if conf.chatgpt_explanation is True:
    # Call ChatGPT Function
    print("ChatGPT Explanation is True")
else:
    # Do Nothing
    print("ChatGPT Explanation is False")

def print_results():
    # Placeholder for the logic to print results to the terminal
    print("Printing stock selections to the terminal...")
    print(pipe.pipe_load())
    print(conf.total_budget)
    print(conf.num_of_desired_stocks)

print_results()