
__author__="Varun Rajiv Mantri"

'''
* webCrawler: starts from the seed-link and crawls the internet adding scraped content to a local text file [uses politeness]
'''

import urllib.request as u
import time
from bs4 import BeautifulSoup


def main():
    seedLink="https://en.wikipedia.org/wiki/Web_crawler"
    activeLinks = []
    activeLinks.append(seedLink)
    webCrawler(1,activeLinks)
    print('crawling completed')


def webCrawler(counter,activeLinks):
    '''
    this methods crawls the internet recursively adding data on each website to a local text file
    :param counter: keeps the count of websites visited
    :param activeLinks: a list used as a queue for breadth-first crawling
    :return: None
    '''
    print(counter)
    if counter==15 or len(activeLinks)==0:
        return
    link=activeLinks.pop(0)
    try:
        page = u.urlopen(link)
        counter = counter + 1
        fileName='file'+str(counter)+'.txt'
        target = open(fileName, 'w+')
        soup = BeautifulSoup(page)
        target.write("->link: " + link)
        target.write("\n")
        target.write("{")
        for text in soup.select('p'):
            target.write(text.get_text())
            #target.write('\n')
        target.write("}\n\n")
        for a in soup.find_all('a', href=True):
            temp = a['href']
            if temp.find('http') is not -1:
                activeLinks.append(temp)
        target.close()
        time.sleep(1)  #using politeness
        webCrawler(counter, activeLinks)
    except Exception:
        print('http error hit')
        return webCrawler(counter,activeLinks)
    except u.URLError:
        print('url error hit')
        return webCrawler(counter,activeLinks)



if __name__=="__main__":
    main()