# Personal_Finance_CLI
Building a CLI tool that utilizes Python to aggregate information about stocks which I can call through the terminal to see what stocks I should be investing in right now and which ones I should be selling


Using Typer as the CLI tool library

- Functions:
    - Add stocks based on name and it adds it to your running list
    - Recommends you 3 stocks every day to add to your portfolio
    - Gives you a random fun fact quote from the intelligent investor book




TO DO:
    Initial app:
 - Initialize basic app, using Typer [x]
 - Connect to Yahoo Finance and successfully pull data [x]
 - When called, should add/remove any companies I added to my "portfolio" based on symbol [x]
    
    Recommendation platform:
- Figure out how to implement gpt, or to make gpt calls []
- Decide on a model to use to help assist with recommending []
- Have the gpt give 3 recommneded stocks based on my current portfolio, for the day []

    Book tip:
- Parse through intelligent investor
- Give quotes from the book that might be helpful in investing