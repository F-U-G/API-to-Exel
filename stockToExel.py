import requests

def getStockData():
    url = "https://apewisdom.io/api/v1.0/filter/wallstreetbets"
    response = requests.get(url)

    if response.status_code == requests.codes.ok: # check the status code for no errors
        return response.json()
    else:
        print(response.status_code)
        return None

data = getStockData()

if data == None:
    print("error, request failed")
else:
    print(data)

