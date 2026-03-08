from httpx import get

base_url = "https://www.cocooncityhostel.com/wp-json/wp/v2"

page_api = f"{base_url}/pages"

print(page_api)

r = get(page_api)
api_data = r.json()

for page in api_data:
    print(page.get("link"))







