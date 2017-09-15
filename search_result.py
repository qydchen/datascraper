import urllib2
from bs4 import BeautifulSoup

# example:
# quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
# page = urllib2.urlopen(quote_page)
# soup = BeautifulSoup(page, 'html.parser')
# name_box = soup.find('h1', attrs={'class': 'name'})
# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print name

rating = 'data-average-rating'
review = 'data-review-count'
title = 'data-title'


smart_tv = 'https://www.bestbuy.com/site/searchpage.jsp?st=smart+tv&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=category_facet%3DSAAS~All+Flat-Panel+TVs~abcat0101001&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
smart_tv_page = urllib2.urlopen(smart_tv)
smart_tv_scrape = BeautifulSoup(smart_tv_page, 'html.parser')
smart_tv_children = smart_tv_scrape.findChildren()
print 'smart tv search'
for child in smart_tv_children:
    smart_tv_rating = child.find('div', attrs={'name': 'data-average-rating'})
    smart_tv_review = child.find('div', attrs={'name': 'data-review-count'})
    smart_tv_title = child.find('div', attrs={'name': 'data-title'})
    print smart_tv_rating
    print smart_tv_review
    print smart_tv_title

# li = soup.find('li', {'class': 'text'})
# children = li.findChildren()
# for child in children:
#     print child

# soup.find("li", { "class" : "test" },recursive=False)

# 4.7
# 207
# Samsung - 43" Class (42.5" Diag.) - LED - 2160p - Smart - 4K Ultra HD TV

# curved_smart_tv = 'https://www.bestbuy.com/site/searchpage.jsp?st=curved+smart+tv&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
# page = urllib2.urlopen(curved_smart_tv)
# curved_smart_tv_page = urllib2.urlopen(curved_smart_tv)
# curved_smart_tv_scrape = BeautifulSoup(curved_smart_tv_page, 'html.parser')
# curved_smart_tv_rating = curved_smart_tv_scrape.find('div', attrs={'class': 'list-item'})[rating]
# curved_smart_tv_review = curved_smart_tv_scrape.find('div', attrs={'class': 'list-item'})[review]
# curved_smart_tv_title = curved_smart_tv_scrape.find('div', attrs={'class': 'list-item'})[title]
# print 'curved smart tv search'
# print curved_smart_tv_rating
# print curved_smart_tv_review
# print curved_smart_tv_title

# 4.7
# 212
# Samsung - 55" Class (54.6" Diag.) - LED - Curved - 2160p - Smart - 4K Ultra HD TV

# create a class
# use beautifulsoup to gather the data
# import it into a csv file
# use python readlines,
# each day's worth of data set should be one csv file
# have program iterate through each folder
# input should be date and have it parsed into folder name

# class SearchResult:
#     def __init__(self, *args):
#
#     def create_list(self, *args):

# class LinkedList:
#     def __init__(self, *args):
#         self.head = self.create_list(*args)
#
#     def create_list(self, *args):
#         last_node = None
#         for nval in reversed(args):
#             current_node = Node(nval)
#             current_node.next = last_node
#             last_node = current_node
#         return last_node
#
#     def print_ll(self):
#         self._print_ll(self.head)
#
#     def _print_ll(self, node):
#         if node is None:
#             return
#         else:
#             print(node.val)
#             self._print_ll(node.next)
#
#     def reverse_print_ll(self):
#         self._reverse_print_ll(self.head)
#
#     def _reverse_print_ll(self, node):
#         if node is None:
#             return
#         else:
#             self._reverse_print_ll(node.next)
#             print(node.val)
#
#     def iterative_print(self):
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.val)
#             current_node = current_node.next
#
#     def pop(self):
#         if self.head.next is None:
#             self.head = None
#             return
#         else:
#             self.head = self.head.next
#             return self.head.val
#
#     def push(self, val):
#         if self.head is None:
#             self.head = Node(val)
#             return self.head.val
#
#         current_node = self.head
#
#         while current_node is not None:
#             if current_node.next is None:
#                 current_node.next = Node(val)
#                 return current_node.next.val
#             else:
#                 current_node = current_node.next
#
#     def insert(self, val, idx):
#         current_idx = 0
#         current_node = self.head
#         newNode = Node(val)
#         if idx == 0:
#             self.head = newNode
#             self.head.next = current_node
#             return
#         while current_idx < idx - 1:
#             current_node = current_node.next
#             current_idx += 1
#         newNode.next = current_node.next
#         current_node.next = newNode
