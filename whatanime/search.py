import requests

def search(api_token, image):
    endpoint="https://whatanime.ga/api/search"
    params={"token":api_token}
    data={"image":image}
    r = requests.post(endpoint, params=params, data=data)
    result=r.json()
    return(result)
