import csv, string, datetime, glob

files = glob.glob("*.csv")

headers = csv.reader(open(files[-1], "rU"), dialect=csv.excel)

headers.next()
headers.next()
headers.next()

for row in headers:
    print row