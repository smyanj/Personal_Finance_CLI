import typer

from myStocks import get_stock_data, display_stock_data, add_to_watchlist, load_watchlist, remove_from_watchlist
from pdfReader import extract_quote
#initializing app
app = typer.Typer()


#Initial app: gives the stocks I'm currently investing in
@app.command()
def topStocks():
    watchlist = load_watchlist()
    stocks = get_stock_data(watchlist)
    display_stock_data(stocks)

@app.command()
def add_company(ticker:str):
    result = add_to_watchlist(ticker)
    typer.echo(result)

@app.command()
def remove_company(ticker:str):
    result = remove_from_watchlist(ticker)
    typer.echo(result)


#Gives recomendation for today
@app.command()
def reccom():
    pass

#quote from intelligent investor
@app.command()
def pick_quote(page: int):
    """
    Extracts an insightful quote from a specific page of The Intelligent Investor.
    """
    quote = extract_quote(page_number=page)
    print(f"\n📖 GPT-Chosen Quote (Page {page}):\n\"{quote}\"")


if __name__ == "__main__":
    app()