import typer

from myStocks import get_stock_data, display_stock_data, add_to_watchlist, load_watchlist, remove_from_watchlist

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

def remove_company(ticker:str):
    result = remove_from_watchlist(ticker)
    typer.echo(result)

#Gives recommnedation for today
@app.command()
def rec():
    pass

#quote from intelligent investor
@app.command()
def book_quote():
    pass

if __name__ == "__main__":
    app()