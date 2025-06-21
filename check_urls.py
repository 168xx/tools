import requests

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

def main():
    with open('url.txt', 'r') as file:
        urls = file.readlines()

    valid_urls = []
    for url in urls:
        url = url.strip()
        if url.startswith('http://') or url.startswith('https://'):
            if check_url(url):
                valid_urls.append(url)

    with open('ok.txt', 'w') as file:
        for url in valid_urls:
            file.write(url + '\n')

if __name__ == "__main__":
    main()