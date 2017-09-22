import csv
import numpy as np
from datetime import datetime
from datetime import timedelta
from scipy.stats.stats import pearsonr

class ReadData:
    def __init__(self, start_file='091417', end_file=datetime.today().strftime("%m%d%y")):
        # will by default run ALL csv files from the first day this program started gathering data to today
        self.start_file = start_file
        self.end_file = end_file
        self.data = {}
        self.results = {} # memoize results here
        self.id_count = 0 # used to implement id across multiple files and counter for all rows
        self.init_file_read()

    def init_file_read(self):
        if self.end_file is not None:
            total_days = self.days_between(self.start_file, self.end_file)
            add_day = 0
            while add_day <= total_days:
                filename = self.fetch_file(self.start_file, add_day)
                self.read_file(filename)
                add_day += 1
        else: # if the user input None, only run a file for one day
            self.read_file(self.start_file)

    def read_file(self, filename):
        with open('./data/{0}'.format(filename)) as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            for row in read:
                self.data[self.id_count] = row
                self.id_count += 1

    def view_data(self):
        print self.data

    def length(self):
        print self.id_count

    def view_results(self):
        print self.results

    def brand_ownership(self, search_param): # for question 1: what % of search results are owned by each brand
        if 'brand_ownership' not in self.results:
            self.results['brand_ownership'] = {}

        if search_param in self.results['brand_ownership']:
            print self.results['brand_ownership'][search_param]
        else:
            search_ownership = self.results['brand_ownership'] = {}
            brands = {}
            counter = 0.0
            for id in self.data:
                search_term = self.data[id][1]
                brand = self.data[id][2]
                if search_term == search_param:
                    if brand not in brands:
                        brands[brand] = 1.0
                        counter += 1.0
                    else:
                        brands[brand] += 1.0
                        counter += 1.0
            search_ownership[search_param] = self.make_percentage(brands, counter)
            print search_ownership[search_param]

    def top_brands(self, search_param): # for question 2: what % of the top 3 search results are owned by each brand
        if 'top_brands' not in self.results:
            self.results['top_brands'] = {}

        if search_param in self.results['top_brands']:
            print self.results['top_brands'][search_param]
        else:
            search_top_brands = self.results['top_brands'] = {}
            top_brands = {}
            counter = 0.0
            for id in self.data:
                rank = int(self.data[id][0])
                search_term = self.data[id][1]
                brand = self.data[id][2]
                if (search_term == search_param) & (rank < 4):
                    if (brand not in top_brands):
                        top_brands[brand] = 1.0
                        counter += 1.0
                    else:
                        top_brands[brand] += 1.0
                        counter += 1.0
            search_top_brands[search_param] = self.make_percentage(top_brands, counter)
            print search_top_brands[search_param]

    def review_vs_ranking(self): # is there a correlation between the number of reviews and search ranking
        if 'review_vs_ranking' in self.results:
            print self.results['review_vs_ranking']
        else:
            review = self.make_vector(4)
            ranking = self.make_vector(0)
            correl = pearsonr(review, ranking)
            self.results['review_vs_ranking'] = correl
            print correl

    def rating_vs_ranking(self): # is there a correlation between the rating and search ranking
        if 'rating_vs_ranking' in self.results:
            print self.results['rating_vs_ranking']
        else:
            rating = self.make_vector(3)
            ranking = self.make_vector(0)
            correl = pearsonr(rating, ranking)
            self.results['rating_vs_ranking'] = correl
            print correl

    def make_vector(self, col_num):
        vector = []
        for id in self.data:
            vector.append(self.data[id][col_num])
        return np.array(vector).astype(np.float)

    def make_percentage(self, brands_obj, counter):
        search_result = {}
        for brand in brands_obj:
            search_result[brand] = "{0:.0f}%".format(brands_obj[brand]/counter * 100)
        return search_result

    # parses the date into a file name
    def fetch_file(self, date, incre):
        datetime_obj = datetime.strptime(date, '%m%d%y') + timedelta(days=incre)
        new_filename = datetime_obj.strftime('%m%d%y')
        return new_filename

    # calculate the days between to gather the files
    def days_between(self, d1, d2):
        d1 = datetime.strptime(d1, '%m%d%y')
        d2 = datetime.strptime(d2, '%m%d%y')
        return abs((d2 - d1).days)

# two_days = ReadData('091417','091517')
# two_days.brand_ownership('smart_tv')
# two_days.top_brands('smart_tv')
# two_days.brand_ownership('curved_smart_tv')
# two_days.view_data()
# two_days.length()

# one_day = ReadData('091617', None)
# one_day.brand_ownership('smart_tv')
# one_day.top_brands('smart_tv')
# one_day.brand_ownership('curved_smart_tv')
# one_day.view_data()
# one_day.length()

all_days = ReadData('091417', '091917')
# all_days.view_data()
all_days.brand_ownership('smart_tv')
all_days.brand_ownership('curved_smart_tv')
all_days.top_brands('smart_tv')
all_days.top_brands('curved_smart_tv')
all_days.review_vs_ranking()
all_days.rating_vs_ranking()
# all_days.view_results()
