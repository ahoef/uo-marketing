# import a csv specified at the command line
# read the csv into a python data structure friendly to jinja
# use a hardcoded template (for now), render the template in memory as a string
# print the string to standard out

import sys
import csv
from jinja2 import Template

import settings

# UPDATE THIS LIST WITH ANY NEWLY DISCOVERED BAD CHARACTERS.
CHARACTER_CORRECTIONS = {
    "\xd0": "-",
    "\xd2": "'",
    "\xd5": "'",
}

def remove_bad_characters(string):
    for bad, good in CHARACTER_CORRECTIONS.items():
        string = string.replace(bad, good)
    return string

category_code = sys.argv[1]
category_name = sys.argv[2]
formatted_date = sys.argv[3]


csv_filename = 'resources/%s.csv' % category_code
csv_file = open(csv_filename, 'rU')
csv_raw_lines = csv_file.readlines()

csv_lines = []
for line in csv_raw_lines:
    csv_lines.append(remove_bad_characters(line))

csv_reader = csv.DictReader(csv_lines)

boxes = []
for box in csv_reader:
    boxes.append(box)

template_file = open(settings.TEMPLATE_FILENAME, 'r')
template_string = template_file.read()
template = Template(template_string)

rendered_template = template.render({'boxes': boxes,
                                     'formatted_date': formatted_date,
                                     'category_code': category_code,
                                     'category_name': category_name })

outfile = open('%s.html' % category_code, 'w')
outfile.write(rendered_template)
outfile.close()

print "DONE WITH %s!" % category_code
