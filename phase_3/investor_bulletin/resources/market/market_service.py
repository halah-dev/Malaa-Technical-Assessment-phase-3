""" Market Service """

"""_summary_
this file to write any business logic for the Market
"""
import requests
import os


def get_market_data(symbol):
    response = requests.get(
        f"{os.getenv('API-Host')}/typprice",
        params={
            "apikey": os.getenv("API-Key"),
            "interval": "1min",
            "format": "JSON",
            "outputsize": "1",
            "dp": "2",
            "symbol": symbol,
        },
        headers={
            "API-Key": os.getenv("API-Key"),
            "API-Host": os.getenv("API-Host"),
        },
    )

    if "error" in response.json():
        return {"status": False, "message": response.json()["message"]}
    else:
        return {
            "status": True,
            "symbol": symbol,
            "price": response.json()["values"][0]["typprice"],
        }
