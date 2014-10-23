from bs4 import BeautifulSoup
import urllib2, string, datetime, time, re
from datetime import timedelta

html = urllib2.urlopen("http://lincoln.ne.gov/city/health/animal/lost/lost.htm")

soup = BeautifulSoup(html)

dogs = soup.find(id='dog')

rows = dogs.findAll('tr')

for row in rows:
    cells = row.findAll('td')
    try:
        baddate = cells[0].string
        dateparse = baddate.split("-")
        missingdate = datetime.date(int(dateparse[0]), int(dateparse[1]), int(dateparse[2]))
        today = datetime.date.today()
        weekago = today - timedelta(days=2)
        if today > missingdate > weekago:
            print "NEW ONE!"
        else: 
            print "NOT NEW"
    except:
        pass