import urllib.request
import shutil


def get_urls():
    url_list = []
    with open('file1', 'r') as f1:
        for line in f1:
            url_list.append(line)

    return url_list

#f2 = open('file2', 'wb')
#first = '<title>'
#
#for line in f1:
#    print(line)
#    with urllib.request.urlopen(line) as response:
#        shutil.copyfileobj(response, f2)
#        if first in open('file2').read():
#            print('trovato')
