# import requests
# api_url = "https://api.ipify.org?format=json"
# response = requests.get(api_url)
#
# # print(response.status_code)
# # print(response.json())
#
#
# if response.status_code == 200:
#     data = response.json()
#     ip = data.get('ip')
#     print("your ip address is: ", ip)
#


import requests
api_url = "https://api.ipify.org?format=json"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    ip = data.get("ip")
    print("Your ip is:",ip)

