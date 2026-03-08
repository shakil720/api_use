
from requests import get
import pprint
from pprint import pprint
city_name = "dhaka"
api_key = "63786c0f6e2c82f0d9890fd505c9a875"
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"



r = get(api_url)
api_data = r.json()
country = api_data.get("sys").get("country")
weather_data = api_data.get("main")
feels_like = weather_data.get("feels_like")
temp = weather_data.get("temp")


print(country,"Feels Like: ",feels_like,"Temp", temp)

# pprint(temp)







