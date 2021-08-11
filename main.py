import requests
from twilio.rest import Client

api_key = YOUR API KEY 
account_sid = YOUR ACCOUNT ID
auth_token = YOUR AUTHORIZTION TOKEN

LAT = YOUR LATITUDE
LONG = YOUR LONGITUDE
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
        body="Hey, its going to rain today, do not forget to carry ☔☔",
        from_=YOUR TWILLIO MOBILE NUMBER,
        to=YOUR MOBILE NUMBER
    )
    print(message.status)
