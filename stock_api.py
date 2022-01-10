import requests

STOCK_API_KEY = "1B2347XHZIDDEZXL"
STOCK_ENDPOINT = "https://www.alphavantage.co/query/"


class StockAPI:

    def __init__(self):
        self.parameter = {
            "function": "GLOBAL_QUOTE",
            "symbol": "TSLA",
            "apikey": STOCK_API_KEY,
        }

        response = requests.get(url=STOCK_ENDPOINT, params=self.parameter)
        response.raise_for_status()
        self.stock_data = response.json()
        self.open_price = float(self.stock_data["Global Quote"]["02. open"])
        self.prev_close_price = float(
            self.stock_data["Global Quote"]["08. previous close"])

    def percentage_of_change(self):
        """Compares previous close price to current open price of a stock and returns the percentage of the difference."""
        stock_difference = abs(self.open_price -
                               self.prev_close_price)

        percentage = stock_difference * 100

        result = percentage / self.open_price

        return result
