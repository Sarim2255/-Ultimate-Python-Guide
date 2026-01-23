import requests 
query = input("What type of news you are intrested in today?\n")
api = "61fb6af492454afa9118b8ec2b52abb6"


url =f"https://newsapi.org/v2/everything?q={query}&from=2025-07-16&sortBy=publishedAt&apiKey={api}"
print(url)

r = requests.get(url)

data = r.json()
articles  = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"],  article["url"])
    print("\n -------------------------------------\n")
