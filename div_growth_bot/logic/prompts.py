# Include ChatGPT Prompts Here:
import openai
import conf

# Set your OpenAI API key
chatgpt_api_key = conf.chatgpt_api_key

def chatgpt_explanation_prompt(stock_info):
    # Variables Schema Destructuring:
    (
        stock_ticker,
        stock_name,
        stock_div_growth_over_5,
        stock_PE,
        stock_PB,
        stock_debt_to_asset,
        stock_assets_liabilities,
        stock_growth_projections
    ) = stock_info

    CHATGPT_EXPLANATION_PROMPT = f'''
    I am using a stock picker bot that analyzes key statistics to provide suggestions for stocks with a history of dividend growth that intersect with signals for value investing.
    Can you provide to me an explanation as to why the following stock was chosen, given that;

    The stock chosen is: {stock_name}, with the ticker: {stock_ticker}.

    The price to earnings ratio is: {stock_PE},
    The price to book ratio is: {stock_PB},
    The dividend has grown {stock_div_growth_over_5} over the past 5 years,
    The Debt to Asset Ratio is: {stock_debt_to_asset},
    The Assets/Liabilities is: {stock_assets_liabilities},
    And the projected growth of the stock in the near future is {stock_growth_projections}?


    Please explain it to me in very concise and simple terminology.  Feel free to provide any additional information that you think is relevant.
    '''



def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or another model like "gpt-3.5-turbo"
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Example usage
prompt = "Write a Python function to calculate the factorial of a number."
response = get_chatgpt_response(prompt)
print(response)

