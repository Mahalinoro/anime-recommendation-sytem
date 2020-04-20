import csv
import pprint

reader = csv.DictReader(open('DataSource.csv'))

dict_list = []

for line in reader:
    dict_list.append(line)
pprint.pprint(dict_list)

