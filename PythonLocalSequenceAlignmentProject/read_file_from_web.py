import urllib


def read_file_from_web(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    print(text)
    return text
