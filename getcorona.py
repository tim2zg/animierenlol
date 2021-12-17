import requests


def getcovid():
    url = "https://api.covid19api.com/summary"
    r = requests.get(url)
    data = r.json()
    return data["Countries"][168]["TotalConfirmed"]

