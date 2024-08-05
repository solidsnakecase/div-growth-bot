import webbrowser
from fastapi import FastAPI
import uvicorn
import matplotlib.pyplot as plt
from logic import logic

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Trading Bot"}

def display_website():
    # Start the FastAPI server
    url = "http://127.0.0.1:8000"
    webbrowser.open(url)
    print("Opening the website...")
    uvicorn.run(app, host="127.0.0.1", port=8000)


# # Display Visualizations for Stock Choices
# # Include Predictions in Visualizations

# # Display Chart
# # Display Stock Choices
# # Display ChatGPT Explanation

# # Display News Options

# # Include CTA for Starring the Repo