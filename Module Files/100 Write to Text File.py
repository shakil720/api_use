import httpx

url_list = [
    "https://mewmewshopbd.com/blog/best-dog-food",
    "https://www.daraz.com.bd/tag/best-dog-food/",
    "https://www.dogfoodadvisor.com/"
]

for url in url_list:
    r = httpx.get(url)
    text = f"{url}------------{r.status_code}"
    file = open("Link status check.txt", "a+")
    file.writelines(text+"\n")
    file.close()


file = open("Link status check.txt", "r+")
urllist = file.readline()
file.close()

print(urllist)


# text = "This is simple text4"
# file = open("abcd.txt","a+")
# file.writelines(text+"\n")
# file.close()