
# import requests
# api_find_url = "https://api.ipify.org?format=json"
#
# res = requests.get(api_find_url)
# if res.status_code == 200:
#     data = res.json()
#     ip = data.get('ip')
#
#
# ip_location_url = f"https://ipapi.co/{ip}/json/"
# r = requests.get(ip_location_url)
# if r.status_code == 200:
#     ip_details = r.json()
#     city = ip_details.get("city")
#     country = ip_details.get("country")
#     region = ip_details.get("region")
#
# sentence = f"This {ip} is located in {city} {region}, {country}"
# print(sentence)

import requests
ip_find_url = "https://api.ipify.org?format=json"
r = requests.get(ip_find_url)
if r.status_code == 200:
    data = r.json()
    ip = data.get("ip")

ip_location_url = f"https://ipapi.co/{ip}/json/"
res = requests.get(ip_location_url)
if res.status_code == 200:
    ip_details = res.json()
    city = ip_details.get("city")
    region = ip_details.get("region")
    country = ip_details.get("country")

sentence = f"This {ip} is located in {city}{region}, {country}"
print(sentence)

