import requests
from twilio.rest import Client

api_key = "13bf399268bfb4b72d5eea7c28b43da4"
account_sid = 'AC56c0588ce9074d3aad0954b12deb7599'
auth_token = 'e58a4510b9e7daefb502481c8c6f227e'

LAT = 32.750286
LONG = 129.877670
EXCLUDE = 'current,minutely,daily'

response = requests.get(url=f'https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LONG}&exclude={EXCLUDE}&appid={api_key}')
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]

will_rain = False

weather_id_data = []
for hour_data in weather_slice:
    weather_id_data.append((hour_data['weather'][0]['id']))
print(weather_id_data)
for condition in weather_id_data:
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hey, its going to rain today, do not forget to carry carry ☔☔",
        from_='+12055760791',
        to='+919373893514'
    )
    print(message.status)
