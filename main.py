# import a csv specified at the command line
# read the csv into a python data structure friendly to jinja
# use a hardcoded template (for now), render the template in memory as a string
# print the string to standard out

import sys
import csv
from jinja2 import Template

import settings

csv_filename = sys.argv[1]
csv_file = open(csv_filename, 'r')
csv_reader = csv.DictReader(csv_file)

boxes = []
for box in csv_reader:
    boxes.append(box)

template_file = open(settings.TEMPLATE_FILENAME, 'r')
template_string = template_file.read()
template = Template(template_string)

six_date = sys.argv[2]

rendered_template = template.render({'boxes': boxes,
                                     'six_date': six_date})

sys.stdout.write(rendered_template)
