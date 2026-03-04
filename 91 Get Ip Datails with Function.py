import requests

def res_data(url):
    res = requests.get(api_find_url)
    if res.status_code == 200:
        data = res.json()
    return data

api_find_url = "https://api.ipify.org?format=json"

# res = requests.get(api_find_url)
# if res.status_code == 200:
#     data = res.json()

ip_data = res_data(api_find_url)
ip = ip_data.get('ip')


ip_location_url = f"https://ipapi.co/{ip}/json/"

ip_details = res_data(ip_location_url)
city = ip_details.get("city")
region = ip_details.get("region")
country = ip_details.get("country")


sentence = f"This {ip} is located in {city} {region}, {country}"
print(sentence)
