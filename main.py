import typer

app = typer.Typer()


#Initial app: gives the stocks I'm currently investing in
@app.command()
def top3(stock):
    pass

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