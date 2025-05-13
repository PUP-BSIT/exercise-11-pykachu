import requests 

def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
        print(f"\n{quote} \n- {author}")
    else:
        print("Error: Unable to fetch quote.")