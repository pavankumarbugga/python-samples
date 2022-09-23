import requests 
import sys 

if (len(sys.argv) != 2):
    sys.exit('Invalid arguments')

macadd = sys.argv[1]
#macadd = '44:38:39:ff:ef:57' // '00:00:5e:00:53:af'
URL = f'https://api.macaddress.io/v1?apiKey=at_4DQWZkkifAt779yLot6ir17F5wCK2&output=json&search={macadd}'
res = requests.get(URL)
if (res.status_code == 200):
    jsondata = res.json()
    print(jsondata['vendorDetails']['companyName'])
elif (res.status_code == 401):
    print("Access restricted. Enter the correct API key.")
elif (res.status_code == 402):
    print("Access restricted. Check the credits balance.")
elif (res.status_code == 422):
    print("Invalid MAC or OUI address was received.")
elif (res.status_code == 429):
    print("Too many requests. Try your call again later.")
elif (res.status_code == 500):
    print("Internal server error. Try your call again or contact us.")
else:
    print("Failure")
