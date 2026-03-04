import requests
r = requests.get('https://jsonplaceholder.typicode.com/posts')
print(r.json())


for r in r:
    try:
        print(r.json()['title'])
    except:
        pass











