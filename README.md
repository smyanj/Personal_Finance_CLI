# Personal_Finance_CLI
Building a CLI tool that utilizes Python to aggregate information about stocks which I can call through the terminal to see what stocks I should be investing in right now and which ones I should be selling


Using Typer as the CLI tool library

- Functions:
    - Add stocks based on name and it adds it to your running list
    - Recommends you 3 stocks every day to add to your portfolio
    - Gives you a random fun fact quote from the intelligent investor book




Using this app!

# 📊 Personal Finance CLI Tool

A command-line tool for tracking your stock portfolio, receiving financial insights, and extracting investing wisdom — powered by GPT.

---

## 🚀 Features

- ✅ Add and remove stocks from your watchlist
- 📈 View your top performing stocks
- 💬 Get GPT-generated advice on your stock portfolio
- 📚 Extract insightful quotes from *The Intelligent Investor*

---

## 🛠️ Setup

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/Personal_Finance_CLI.git
   cd Personal_Finance_CLI



## .env setup
OPEN_AI_KEY=your_openai_api_key
YAHOO_api_key=your_yahoo_api_key
YAHOO_client_secret=your_yahoo_client_secret

## Usage with Typer
Use:
python main.py [COMMAND] or --help which will provide this menu


## Top Stocks which shows current watchlist and stock data

## add-company: adds company to current watchlist based on ticker
## remove-company: removes company from watchlist based on ticker


## Stocks-Advice: gives recommendations based on current portfolio