import csv
from datetime import datetime
from datetime import timedelta

class ReadData:
    def __init__(self, start_file, end_file=None):
        self.start_file = start_file
        self.end_file = end_file
        self.reader = {}
        self.id_count = 1
        self.init_file_read()

    def init_file_read(self):
        if self.end_file is not None:
            counter = self.days_between(self.start_file, self.end_file)
            add_day = 0
            while add_day <= counter:
                filename = self.fetch_file(self.start_file, add_day)
                self.read_file(filename)
                add_day += 1
        else:
            return self.read_file(self.start_file)

    def read_file(self, filename):
        with open('./data/{0}'.format(filename)) as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            for row in read:
                self.reader[self.id_count] = row
                self.id_count += 1

    def view(self):
        print self.reader

    # parses the date into a file name
    def fetch_file(self, date, incre):
        datetime_obj = datetime.strptime(date, '%m%d%y') + timedelta(days=incre)
        incremented_day = datetime_obj.strftime("%m%d%y")
        return incremented_day

    # calculate the days between to gather the files
    def days_between(self, d1, d2):
        d1 = datetime.strptime(d1, '%m%d%y')
        d2 = datetime.strptime(d2, '%m%d%y')
        return abs((d2 - d1).days)

newRead = ReadData('091517','091717')
newRead.view()
