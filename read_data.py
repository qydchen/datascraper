import csv
from datetime import datetime
from datetime import timedelta

class ReadData:
    def __init__(self, start_file='091417', end_file=datetime.today().strftime("%m%d%y")):
        # will by default run from the first day this program started gathering data to today
        self.start_file = start_file
        self.end_file = end_file
        self.reader = {}
        self.results = {'brand_ownership': {}} # memoize results here
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
                self.reader[self.id_count] = row
                self.id_count += 1

    def view(self):
        print self.reader

    def count(self):
        print self.id_count

    def brand_ownership(self, search_param): # for question 1
        if search_param in self.results['brand_ownership']:
            print self.results['brand_ownership'][search_param]
        else:
            brands = {}
            search_result = {}
            counter = 0.0
            for item in self.reader:
                search_term = self.reader[item][1]
                brand = self.reader[item][2]
                if search_term == search_param:
                    if brand not in brands:
                        brands[brand] = 1.0
                        counter += 1.0
                    else:
                        brands[brand] += 1.0
                        counter += 1.0
            for brand in brands:
                percent = "{0:.0f}%".format(brands[brand]/counter * 100)
                search_result[brand] = percent
            self.results['brand_ownership'][search_param] = search_result
            print self.results['brand_ownership'][search_param]

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

three_days = ReadData('091417','091617')
three_days.brand_ownership('smart_tv')
three_days.brand_ownership('curved_smart_tv')
three_days.view()
three_days.count()

one_day = ReadData('091617', None)
three_days.brand_ownership('smart_tv')
one_day.brand_ownership('curved_smart_tv')
one_day.view()
one_day.count()

# An example view:
# {
#     0: ['1', 'smart_tv', 'LG', '4.6', '274'],
#     1: ['2', 'smart_tv', 'Samsung', '4.6', '5899'],
#     2: ['3', 'smart_tv', 'LG', '4.6', '187'],
#     3: ['4', 'smart_tv', 'Samsung', '4.6', '3318'],
#     4: ['5', 'smart_tv', 'Samsung', '4.7', '219'],
#     5: ['6', 'smart_tv', 'Samsung', '4.6', '2538'],
#     6: ['7', 'smart_tv', 'LG', '4.8', '51'],
#     7: ['8', 'smart_tv', 'LG', '4.6', '231'],
#     8: ['9', 'smart_tv', 'LG', '4.5', '443'],
#     9: ['10', 'smart_tv', 'Samsung', '4.7', '360'],
#     10: ['11', 'smart_tv', 'LG', '4.5', '130'],
#     11: ['12', 'smart_tv', 'Samsung', '4.6', '2052'],
#     12: ['13', 'smart_tv', 'Samsung', '4.5', '99']
# }
