import requests


def getcovid():
    url = "https://api.covid19api.com/summary"  # url
    r = requests.get(url)  # get request
    data = r.json()  # convert to json
    return data["Countries"][168]["TotalConfirmed"]  # return total confirmed cases
