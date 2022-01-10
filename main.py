from news_api import NewsAPI
from stock_api import StockAPI
from twilio.rest import Client

TWILIO_SID = "AC39506a4c9728379df62457082c79d2c8"
AUTH_TOKEN = "08bad80ff4fe03f417dd4b4c108447eb"
PHONE_NUMBER = "+18508468251"

stock_symbol = StockAPI().parameter["symbol"]
stock_percentage = StockAPI().percentage_of_change()
news = NewsAPI().alert()

client = Client(TWILIO_SID, AUTH_TOKEN)

message = client.messages.create(body=f"\n{stock_symbol}❤️{stock_percentage}\nHeadline: {news['title']}\nBrief: {news['description']}",
                                 from_=PHONE_NUMBER,
                                 to='+16142076539')
print(message.status)
