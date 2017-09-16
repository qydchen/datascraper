import urllib2
import csv
import os
from datetime import datetime
from bs4 import BeautifulSoup

smart_tv = 'https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&st=smart%20tv&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&nrp=&sp=&qp=category_facet%3DSAAS~All%20Flat-Panel%20TVs~abcat0101001%5Ebrand_facet%3DBrand~Samsung%5Ebrand_facet%3DBrand~LG%5Ebrand_facet%3DBrand~Sony%5Ebrand_facet%3DBrand~Toshiba&list=n&af=true&iht=y&usc=All%20Categories&ks=960&keys=keys'
curved_smart_tv = 'https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&st=curved%20smart%20tv&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&nrp=&sp=&qp=brand_facet%3DBrand~Samsung&list=n&af=true&iht=y&usc=All%20Categories&ks=960&keys=keys'

class BestBuyScrape:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def scrape(self):
        self._scrape(self.url)

    def _scrape(self, url):
        rating = 'data-average-rating'
        review = 'data-review-count'
        title = 'data-title'
        scrape = BeautifulSoup(urllib2.urlopen(url), 'html.parser')
        file_name = datetime.today().strftime("%m%d%y") # filenames will represent the day it was scraped
        list_items = scrape.find('div', attrs={'class': 'list-items'})

        if not os.path.exists('data'): # if there's no data folder, make one
            os.makedirs('data')
        with open('./data/{0}'.format(file_name), 'a') as csv_file:
            writer = csv.writer(csv_file)
            for (idx, child) in enumerate(list_items.children):
                # idx + 1 is used to denote ranking for each day
                writer.writerow([idx + 1, self.name, self.parse_title(child[title]), child[rating], child[review],])

    def parse_title(self, title):
        return title.split()[0]

import_smart_tv = BestBuyScrape(smart_tv, 'smart_tv')
import_smart_tv.scrape()

import_curved_smart_tv = BestBuyScrape(curved_smart_tv, 'curved_smart_tv')
import_curved_smart_tv.scrape()
