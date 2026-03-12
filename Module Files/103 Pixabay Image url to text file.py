from httpx import get
from pprint import pprint

api_key = "54975452-35364a4966174202e8083335b"
query = "yellow+flowers"
api_url = f"https://pixabay.com/api/?key={api_key}&q={query}"


r = get(api_url)
api_data = r.json().get("hits")
# pprint(api_data)

for data in api_data:
    image_url = data.get("webformatURL")
    file = open("images.txt", "a+")
    file.writelines(image_url+"\n")
    file.close()

# r = get(url)
# api_data = r.json()
# image_url = api_data.get("hits")
# hits = image_url[0].get("pageURL")
#
# print(hits)