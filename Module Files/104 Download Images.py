from requests import get

file = open("images.txt","r+")
url_list = file.readlines()
file.close()


new_url_list = []
for url in url_list:
    new_url = url.rstrip("\n")
    new_url_list.append(new_url)

single_url = new_url_list[0]
print(single_url)
r = get(single_url)
# file = open("pixa.jpg", "wb")
# file.write(r.content)
# file.close()
with open("google.jpg", "wb") as file:
    file.write(r.content)



