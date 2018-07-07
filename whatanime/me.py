import requests

def me(token):
    endpoint="https://whatanime.ga/api/me"
    payload={"token":token}
    r = requests.get(endpoint, params=payload)
    return(r.json())
