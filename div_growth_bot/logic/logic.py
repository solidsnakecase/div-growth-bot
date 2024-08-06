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
    if conf.chatgpt_explanation is True:
        # Call ChatGPT Function
        print("ChatGPT Explanation is True")
    else:
        # Do Nothing
        print("ChatGPT Explanation is False")

app_logic()