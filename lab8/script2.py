#!/home/gitpod/.pyenv/shims/python3

import json

# Read in file as JSON
with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

# Pull out fields: name, html_url, updated_at, visibility
# Assembles these four fields into a comma-separated line.
# Appends this line to a new text file named chacon.csv

for d in data:
    print(d['name'])



# Limit to 5 lines only