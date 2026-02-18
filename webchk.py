vers = "1.0.0"
def version():
    return vers

try:
    import requests
    from requests.exceptions import RequestException
except Exception:
    print("[ERROR] Requests could not be found X_X")
    exit()
def check(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        if 200 <= response.status_code < 400:
            return True
        else:
            return False
    except RequestException as e:
        return False
