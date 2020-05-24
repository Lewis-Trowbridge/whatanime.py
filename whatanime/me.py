import requests


def me(token=""):

    endpoint = "https://trace.moe/api/me"
    payload = {"token": token}
    r = requests.get(endpoint, params=payload)
    if r.status_code == 200:
        return r.json()
    if r.status_code == 403:
        raise Exception("API token invalid")
