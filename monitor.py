import urllib.request


def get_urls(url_file):
    """ Fetches url list from a file.
    """
    url_list = []
    with open(url_file, 'r') as f1:
        for line in f1:
            url_list.append(line)

    return url_list


def find_tag(url_list, tag):
    """ Fetches HTML pages from a list of urls and checks if the argument tag
    is present in the source.
    """
    for url in url_list:
        with urllib.request.urlopen(url) as response:
            body_byte = response.read()
            body_str = body_byte.decode(encoding='utf-8')
            if body_str.find(tag):
                print('trovato')

if __name__ == '__main__':
    url_file = 'file1'
    url_list = get_urls(url_file)
    find_tag(url_list, '<title>')
