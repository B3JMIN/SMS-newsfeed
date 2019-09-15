import os
import twilio
import request_weather
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACeb461270643b040ab3518ebf18a16aa6'
auth_token = '0fc4402892c581a8825fd64dd55a873e'
client = Client(account_sid, auth_token, http_client=proxy_client) # Notice the keyword argument
data = request_weather.get_weather_dictionary("bd8d09d547fc2be92f89e8e5d6ff64cc","6176823")

temperature = str(data["main"]["temp"])
weather_condition = str(data["weather"][0]["description"])
wind_speed = str(data["wind"]["speed"])
max_temp = str(data["main"]["temp_min"])
min_temp = str(data["main"]["temp_max"])

body = """The temperature of Waterloo is {}  degree, The weather condition is {}
The wind speed is  {} km/h   The maximum temperature is {} degree
The minimum temperature is {} degree"""
message = client.messages \
                .create(body= body.format(temperature, weather_condition, wind_speed, max_temp, min_temp),from_='+16476915280',to='+12269884795')

print(message.sid)

print(data)