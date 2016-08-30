# coding=utf-8
import csv
import sys
import func
import urlparse
import requests
from bs4 import BeautifulSoup


def hashspider(url, log_path):

    urls = [url]
    visited = [url]
    #print log_path

    while len(urls) > 0:
        sys.stdout.flush()
        try:
            htmltext = requests.get(urls[0]).text
            urlhash = func.md5(htmltext[10:600])

            csvfiler = file(log_path + 'webhash.csv', 'rb')
            reader = csv.reader(csvfiler)
            exists = False # exists or not?
            for line in reader:
                if urls[0] == line[0]:
                    exists = True
                    if urlhash != line[1]:
                        print line, 'has been tampered!', urlhash
                        exit()
                else:
                    pass
            csvfiler.close()
            if exists == False:  # Not exists, so it should be written into the log file.
                with open(log_path + 'webhash.csv', 'ab+') as csvfile:
                    spamwriter = csv.writer(csvfile, dialect='excel')
                    spamwriter.writerow([urls[0], urlhash])
                    csvfile.close()

            print urls[0], '[Good]'
        except:
            print urls[0], '[Bad]'

        soup = BeautifulSoup(htmltext, "html.parser")

        urls.pop(0)
        print len(urls),

        for tag in soup.findAll('a', href = True):
            tag['href'] = urlparse.urljoin(url, tag['href'])
            if url in tag['href'] and tag['href'] not in visited and "#" not in tag['href']: # While in the sanme domin
                urls.append(tag['href'])
                visited.append(tag['href'])
