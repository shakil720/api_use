import httpx

url_list = [
    "https://mewmewshopbd.com/blog/best-dog-food",
    "https://www.dogfoodadvisor.com/",
    "https://www.forbes.com/sites/forbes-personal-shopper/article/best-dry-dog-food/",
]

for url in url_list:
    r = httpx.get(url)
    print(url,r.status_code, sep="-----------")

