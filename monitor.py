import urllib.request
import shutil


f1 = open('file1', 'r')
f2 = open('file2', 'wb')
first = '<title>'

for line in f1:
    print(line)
    with urllib.request.urlopen(line) as response:
        shutil.copyfileobj(response, f2)
        if first in open('file2').read():
            print('trovato')
