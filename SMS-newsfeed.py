import os
import twilio
import request_weather
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'MY SID'
auth_token = 'MY token'
client = Client(account_sid, auth_token, http_client=proxy_client) # Notice the keyword argument
data = request_weather.get_weather_dictionary("XXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXX")

temperature = str(data["main"]["temp"])
weather_condition = str(data["weather"][0]["description"])
wind_speed = str(data["wind"]["speed"])
max_temp = str(data["main"]["temp_min"])
min_temp = str(data["main"]["temp_max"])

body = """The temperature of Waterloo is {}  degree, The weather condition is {}
The wind speed is  {} km/h   The maximum temperature is {} degree
The minimum temperature is {} degree"""
message = client.messages \
                .create(body= body.format(temperature, weather_condition, wind_speed, max_temp, min_temp),from_='+1(xxx)xxx-xxxx',to='+1(xxx)xxx-xxxx')
#                   phone number from twillio to my phone number

print(message.sid)

print(data)
