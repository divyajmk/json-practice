#!/home/gitpod/.pyenv/shims/python3



import json


# Read in file as JSON
with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

# Create new csv file to append line to later 
with open("chacon.csv", "w", newline="") as csv_file:
    # Only want 5 outputs
    for d in data[:5]:
        # Pull out fields: name, html_url, updated_at, visibility
        name = d.get('name')
        html_url = d.get('html_url')
        updated_at = d.get('updated_at')
        visibility = d.get('visibility')

        # Assembles these four fields into a comma-separated line.
        line = name + ',' + html_url + ',' + updated_at + ',' + visibility

        # Appends this line to a new text file named chacon.csv
        csv_file.write(line + '\n')
