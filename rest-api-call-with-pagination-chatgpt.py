import requests

def get_data_with_pagination(url, headers, page_size=10, page=1):
    params = {"page_size": page_size, "page": page}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    while "next" in response.links:
        response = requests.get(response.links["next"]["url"], headers=headers)
        data += response.json()

    return data

url = "https://api.example.com/endpoint"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
data = get_data_with_pagination(url, headers)
