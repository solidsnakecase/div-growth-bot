# Dividend Growth Bot (Gordon Growth)

**WIP: MVP in development**
**Edit: (8/6/2024) Project shelved, AlphaVantage API has a limit of 25 Calls/day, which does not allow for the enumeration of the data necessary for analysis.  Will start development again when appropriate API is found accessible for free, as this meets the needs of the project.**

## About

**Not Limited to S&P 500 Stocks**

### Options
- How many stocks to recommend
- Web/CLI Options
- Exclude Following Stocks
- Exclude/Include Certain Stock Categories/Tags (ie. Tech, Consumer Staples, Blue Chip)

(Uses AlphaVantage API, has a 25 Call/day limit on free tier.)

### To Do
- Pipe Module
- Analysis Module
- Dockerize
(Test the Following for the Web Option):
> docker run -p 80:80 your_image_name --web

- Exclusion Module
- Selection Module
- Chat Module
- Web Visualization Module
- HTMX
- Light/Dark Mode
- Overall Market Status (Downtrend/Uptrend)
- News Option to Web
- Budgeting Module
- Sector Module

### Housekeeping
- Refactoring
- Trim Imports
- Testing/Error Handling
- Remove Data, Use Memory Instead, Move Notebook for Reference