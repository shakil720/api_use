import requests
api_key = ""

# test_url ="https://web.dev/"
test_url = input("Please enter the URL of the test page: ")
api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}?&key={api_key}"
# print(api_url)

r = requests.get(api_url)

if r.status_code == 200:
    data = r.json()
    cls = data.get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
    print(cls)
else:
    print("Something went wrong")






