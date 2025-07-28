from myStocks import get_stock_data, load_watchlist
from sk import mySk
from openai import OpenAI
from dotenv import load_dotenv
import os
from sk import mySk
import json
WATCHLIST_PATH = "watchlist.json"

load_dotenv()

#OpenAI.api_key = mySk

def build_recommendation_prompt():
    watchlist = load_watchlist()
    stock_data = get_stock_data(watchlist)

    message_list = [
        {
            "role": "system",
            "content": (
                "You are a professional financial advisor. "
                "Given a user's stock portfolio and current performance, "
                "you will provide a thoughtful analysis including performance summary, "
                "potential concerns, and suggestions for diversification or optimization. "
                "Only use the data provided — do not make up prices or trends."
            )
        },
        {
            "role": "user",
            "content": f"Here is my current stock portfolio:\n\n{stock_data}\n\nWhat are your insights and suggestions?"
        }
    ]

    return message_list


def send_recs(message_list):
    load_dotenv()
    client = OpenAI(api_key=mySk)

    message_list = build_recommendation_prompt()

    response = client.chat.completions.create(
        messages = message_list,
        model="gpt-3.5-turbo"
    )

    return response.choices[0].message.content.strip()