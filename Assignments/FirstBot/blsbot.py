import csv, string, datetime

reader = csv.reader(open("blsdata.csv", "rU"), dialect=csv.excel)

reader.next()

blslist = []

for row in reader:
    blslist.append(row)

currentyear = blslist[-1]
currentyear = filter(None,currentyear)

yearlen = len(currentyear)

if yearlen != 1:
    currentmonth = currentyear[-1]
    previousmonth = currentyear[-2]
    reportyear = int(currentyear[0])
    reportmonth = len(currentyear)-1
    reportdate = datetime.datetime(reportyear, reportmonth, 1)
else:
    currentmonth = currentyear[1]
    previousyear = blslist[-2]
    previousmonth = previousyear[-1]
    reportyear = int(currentyear[0])
    reportmonth = len(currentyear)-1
    reportdate = datetime.datetime(reportyear, reportmonth, 1)

previousyear = blslist[-2]
previousyearmonth = previousyear[yearlen-1]

if currentmonth > previousmonth:
    verb = "increased"
elif currentmonth == previousmonth:
    verb = "held steady"
else:
    verb = "decreased"
    
pctchange = ((float(currentmonth)-float(previousmonth))/float(previousmonth)*100)

print verb, abs(pctchange)