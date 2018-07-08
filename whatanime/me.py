import requests

def me(token):
    endpoint="https://whatanime.ga/api/me"
    payload={"token":token}
    r = requests.get(endpoint, params=payload)
    if r.status_code==403:
        raise Exception("API token invalid")
    elif r.status_code==401:
        raise Exception("API token missing")
    elif r.status_code==200:
        return(r.json())
