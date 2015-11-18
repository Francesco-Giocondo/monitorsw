import urllib.request


def get_urls():
    url_list = []
    with open('file1', 'r') as f1:
        for line in f1:
            url_list.append(line)

    return url_list


def find_tag(url_list, tag):
    for url in url_list:
        with urllib.request.urlopen(url) as response:
            body_byte = response.read()
            body_str = body_byte.decode(encoding='utf-8')
            if body_str.find(tag):
                print('trovato')
