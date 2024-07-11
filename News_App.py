import requests
import json

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-29&sortBy=publishedAt&apiKey=417fda7f69c84246bf1ce9adf344f175"

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)

    for article in data['articles']:
        print(article['title'])
        print(article['description'])
        print("\n----------------------------------------\n")
else:
    print("Error: Failed to retrieve data from the API.")
    data = None

