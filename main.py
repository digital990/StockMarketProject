import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "LRF8APBORCNIH36H"


NEW_ENDPOINT = " https://newsapi.org/v2/everything"
NEW_API_KEY = "4bb0fc6969af4b5385f05973010a1160"
TWILO_SID = "ACff0206a6553c34ad6bcc8753a45e2259"
AUTH_TOKEN = "66e829814da85738fa4acd60d2afb1f4"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)

# getting yesterday closing stock price
data = response.json()["Time Series (Daily)"]
data_list = [values for (key, values) in data.items()]
yesterday_data = data_list[0]
closing_price = yesterday_data["4. close"]
print("This is yesterday closing stock")
print(closing_price)

# get a day before yesterday closing stock price
day_before_yesterday = data_list[1]
day_before_yesterday_price = day_before_yesterday["4. close"]
print("This is day before yesterday closing stock")
print(day_before_yesterday_price)

up_emoji = "⬆️"
down_emoji = "⬇️"
diffrence = float(closing_price) - float(day_before_yesterday_price)
up_down = None

if diffrence > 3:
    up_down = up_emoji
else:
    up_down = down_emoji
print("Stock Difference")
print(diffrence)

diff_percent = round((diffrence / float(closing_price)) * 100)
print("Percentage Difference")
print(diff_percent)



if abs(diff_percent) > 0:
    new_params = {
        "apiKey": NEW_API_KEY,
        "q": COMPANY_NAME
    }

    news_response = requests.get(NEW_ENDPOINT, params=new_params)
    aritcles = news_response.json()["articles"]
    # print(aritcles)

    three_articles = aritcles[:3]
    print(three_articles)

    formatted_text = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline:  {article['title']} \n Brief: {article['description']}" for article in three_articles]

    client = Client(TWILO_SID, AUTH_TOKEN)

    for article in formatted_text:
        messages = client.messages.create(
            body = article,
            from_="+12565888458",
            to= "+2349067618414"
        )


    



