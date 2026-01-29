import requests
query=input("enter your intrest=")
print(query)
api ="541b5be6791c4492a04be4a21069b177"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-08-19&to=2025-08-19&sortBy=popularity&apiKey={api}"
print(url)
r=requests.get(url)

data = r.json()
articles = data['articles']
for index,article in enumerate(articles):
    print(index+1,article["title"], article["url"])
    print("\n**********************\n")

# If pip is not found in your terminal, try using the following commands to install the requests module:

# For Python 3, you can use:
# python3 -m pip install requests

# Or, if you are using Windows:
# py -m pip install requests

# If you are using a virtual environment, make sure it is activated before running the above command.

# If you still have issues, you may need to reinstall pip:
# python3 -m ensurepip --upgrade

# After installing, you can import and use the requests module as shown above.
