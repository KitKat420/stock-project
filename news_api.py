import requests
from stock_api import StockAPI

NEWS_API_KEY = "01a816f740df466aa35a5d46d79bf7f6"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything/"


class NewsAPI(StockAPI):
    def __init__(self):
        super().__init__()

        paramters = {
            "qInTitle": self.parameter["symbol"],
            "pageSize": 1,
            "apiKey": NEWS_API_KEY,
        }
        response = requests.get(url=NEWS_ENDPOINT, params=paramters)
        response.raise_for_status()
        self.news_data = response.json()

    def alert(self):
        if self.percentage_of_change() > 0.5:
            news = {
                "title": self.news_data["articles"][0]["title"],
                "description": self.news_data["articles"][0]["description"]
            }
            return news
