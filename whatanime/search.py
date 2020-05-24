import requests
from whatanime import exception as whatanimeexceptions


def search(image, token=""):

    endpoint = "https://trace.moe/api/search"
    data = {"image": image}
    params = {"token": token}
    search_request = requests.post(endpoint, data=data, params=params)
    if search_request.status_code == 200:
        return search_request.json()
    elif search_request.status_code == 400:
        raise ValueError("Image was empty")
    elif search_request.status_code == 403:
        raise ValueError("API token invalid")
    elif search_request.status_code == 413:
        raise whatanimeexceptions.ImageSizeTooLargeError("Image size is too large, please reduce the image size to below 10MB")
    elif search_request.status_code == 429:
        raise whatanimeexceptions.QuotaExceededError("You have exceeded your quota. Please wait and try again soon.")
    elif search_request.status_code == 500:
        raise whatanimeexceptions.APIError("Something went wrong on the API's end: error 500. This may be because the image is malformed.")
    elif search_request.status_code == 503:
        raise whatanimeexceptions.APIError("Something went wrong on the API's end: error 503.")


