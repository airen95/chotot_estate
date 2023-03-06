import requests

def request_api(url: str) -> dict:
    payload={}
    headers = {
    'Cookie': '__cf_bm=_K8ppIZE3sAO_7Wtbfd89dkK_G6GvFboAUWk.bi8p60-1677263069-0-AYYU+H5X14PDa+9P1a0lRfTdxJmbLXCrLuS/g2qK/miqCahtQ126bk6EQzBNnnPwfhZUgKoPi6JG5qZu/7S0cUU='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    return f"Response fail by {response.status_code}"



