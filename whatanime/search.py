import requests

def search(api_token, image):
    endpoint="https://whatanime.ga/api/search"
    params={"token":api_token}
    data={"image":image}
    r = requests.post(endpoint, params=params, data=data)
    if r.status_code==403:
        return("API token invalid")
    elif r.status_code==401:
        return("API token missing")
    elif r.status_code==413:
        return("The image is too large, please reduce the image size to below 1MB")
    elif r.status_code==429:
        return("You have exceeded your quota. Please wait and try again soon.")
    elif r.status_code==200:
        return(r.json())
