from httpx import get

api_key = "54975452-35364a4966174202e8083335b"
url = f"https://pixabay.com/api/?key={api_key}&q=yellow+flowers&image_type=photo"


r = get(url)
api_data = r.json()
image_url = api_data.get("hits")
hits = image_url[0].get("pageURL")

print(hits)