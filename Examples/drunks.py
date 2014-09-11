import csv, string

reader = csv.reader(open("drunks.csv", "rU"), dialect=csv.excel)

reader.next()

mylist = []

for row in reader:
    mylist.append(row)

for index, obj in enumerate(mylist):  
    if int(obj[1])>19:
        exclamation = "Holy shit!"
        judgement = "real drunk"
    elif int(obj[1])<10:
        exclamation = "Teetotaler alert!"
        judgement = "lightweight"
    else:
        exclamation = "Meh."
        judgement = "amateur"
        
    if obj[0]=="Sara":
        pronoun = "She"
    else:
        pronoun = "he"
    
    record = 45
    difference = record - int(obj[1])
    percent = (float(obj[1])/float(record))*100
    
    previous = mylist[index-1]
        
    print "%s %s is a %s. %s drank %s in one sitting once. That's %i off the record of %i, or %.1f percent. Compare that to %s, who drank %s in one sitting once." % (exclamation, obj[0], judgement, pronoun.title(), obj[1], difference, record, percent, previous[0], previous[1])