import csv

# Open the file with the right mode

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1, 7,9])
    writer.writerow([9,11,170])

# Let's read the file

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    # The following won't run since we are already at the end of the file.
    # for row in reader:
    #     print(row)

"""JSON files"""

import json

movies = [

    {"id": 1, "year": 1982, "title": "Terminator"},
    {"id": 2,"year": 1989, "title": "Kindergarden cop"}
]

data = json.dumps(movies)
print(data)

# Write the above data into a file. Let's do it

from pathlib import Path
Path("movies.json").write_text(data)

# You can read the data too. 
# data = Path("movies.json").read_text()
# movies = json.loads(data)