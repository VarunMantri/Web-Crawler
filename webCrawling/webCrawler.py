
__author__="Varun Rajiv Mantri"

'''
* webCrawler: starts from the seed-link and crawls the internet adding scraped content to a local text file
'''

import urllib.request as u
from bs4 import BeautifulSoup


def main():
    seedLink="https://en.wikipedia.org/wiki/Web_crawler"
    activeLinks = []
    target=open('localStorage.txt','w')
    activeLinks.append(seedLink)
    webCrawler(1,activeLinks,target)
    target.write("some data not written")
    target.close()
    print('crawling completed')


def webCrawler(counter,activeLinks,target):
    '''
    this methods crawls the internet recursively adding data on each website to a local text file
    :param counter: keeps the count of websites visited
    :param activeLinks: a list used as a queue for breadth-first crawling
    :param target: address/location of local text file
    :return: None
    '''
    print(counter)
    if counter==100 or len(activeLinks)==0:
        return
    link=activeLinks.pop(0)
    try:
        page = u.urlopen(link)
        counter = counter + 1
        soup = BeautifulSoup(page)
        target.write("->link: "+link)
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

        webCrawler(counter, activeLinks,target)
    except Exception:
        print('http error hit')
        return webCrawler(counter,activeLinks,target)
    except u.URLError:
        print('url error hit')
        return webCrawler(counter,activeLinks,target)



if __name__=="__main__":
    main()