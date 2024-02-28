import requests

def process_api(page):
    api_url= f"https://jsonmock.hackerrank.com/api/stocks?page={page}"
    response = requests.get(api_url)

    if(response.status_code == 200):
        jsondata = response.json()
        datalist = jsondata["data"]
        mysum = 0
    
        for i in datalist:
            mysum += i["close"]

        return mysum


url= f"https://jsonmock.hackerrank.com/api/stocks?page=1"
res = requests.get(url)
total = 0
if(res.status_code == 200):
    jsondata = res.json()
    pages = jsondata["total_pages"]
    noofrecords = jsondata["total"]
    for i in range(1,pages+1):
        print(process_api(i))
        total += process_api(i)
    print("Total sum:", total)
    print("Mean data:", total/noofrecords)

    
