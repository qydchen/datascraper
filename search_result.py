import urllib2
from bs4 import BeautifulSoup

def parse_title(title):
    return title.split()[0]

smart_tv = 'https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&st=smart%20tv&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&nrp=&sp=&qp=category_facet%3DSAAS~All%20Flat-Panel%20TVs~abcat0101001%5Ebrand_facet%3DBrand~Samsung%5Ebrand_facet%3DBrand~LG%5Ebrand_facet%3DBrand~Sony%5Ebrand_facet%3DBrand~Toshiba&list=n&af=true&iht=y&usc=All%20Categories&ks=960&keys=keys'
curved_smart_tv = 'https://www.bestbuy.com/site/searchpage.jsp?cp=1&searchType=search&st=curved%20smart%20tv&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&nrp=&sp=&qp=brand_facet%3DBrand~Samsung&list=n&af=true&iht=y&usc=All%20Categories&ks=960&keys=keys'

def scrape_bestbuy(url):
    rating = 'data-average-rating'
    review = 'data-review-count'
    title = 'data-title'
    scrape = BeautifulSoup(urllib2.urlopen(url), 'html.parser')
    list_items = scrape.find('div', attrs={'class': 'list-items'})
    for child in list_items.children:
        print parse_title(child[title]), child[rating], child[review]

scrape_bestbuy(smart_tv)
print '*************************************************'
scrape_bestbuy(curved_smart_tv)

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
