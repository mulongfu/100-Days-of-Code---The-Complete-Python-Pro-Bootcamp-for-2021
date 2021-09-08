import requests
from twilio.rest import Client

Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "993f08cfd03f476b5238bf75c93b648e"

account_sid = "AC77d620b5101683bb8592f427d0414b1c"
auth_token = "28ce653cac582072728529a097c2337c"

client = Client(account_sid, auth_token)

param = {
    "lat": "24.813829",
    "lon": "120.967484",
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

res = requests.get(Endpoint, params=param).json()
for i in res["hourly"][0:12]:
    if int(i["weather"][0]["id"]) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Hi there", from_="+12027937305", to="+886988109085"
        )
        print(message.status)
