import requests
import numpy
from twilio.rest import Client

# pythonanywhere address = https://www.pythonanywhere.com/user/Drakkarok/tasks_tab/
# id = drakkaroktesting@Gmail.com

WEATHER_WEBSITE_DOC_5DAYS3HOURS = "https://openweathermap.org/forecast5"
WEATHER_API_ENDPOINT_5DAYS3HOURS = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API_ENDPOINT_ONECALL = "https://api.openweathermap.org/data/2.5/onecall"

API_KEY_PYTHON_PROJECT = "key"

LAT_BUCHAREST = "44.439663"
LON_BUCHAREST = "26.096306"

ACCOUNT_SID = "sid"
AUTH_TOKEN = "token"

parameters = {
    "lat": f"{LAT_BUCHAREST}",
    "lon": f"{LON_BUCHAREST}",
    "appid": API_KEY_PYTHON_PROJECT,
}

weather_request = requests.get(WEATHER_API_ENDPOINT_5DAYS3HOURS, params=parameters)
weather_request.raise_for_status()
weather_data = weather_request.json()
weather_this_hour = weather_data
print(numpy.round(weather_data["list"][0]["main"]["temp"] - 273.15, 2))

weather_condition_for_12hours = []

for forecast in range(0, 5):
    weather_condition_for_12hours.append(int(weather_data["list"][forecast]["weather"][0]["id"]))

print(weather_condition_for_12hours)

print(weather_data["list"])

if any(700 > code for code in weather_condition_for_12hours):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an umbrella with you!",
        from_="+12705801469",
        to="+40721939647"
    )
    print(message.status)
else:
    print("Just cloudy")


