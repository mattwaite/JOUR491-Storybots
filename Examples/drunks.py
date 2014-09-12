# First, you need to import libraries. Good practice is to make any imports first. 

import csv, string

# Now, to read a csv file, you have to create an object that uses the csv library's reader function. The code below opens the file in universal line ending mode, and in the excel dialect, which is a safe default most of the time.

reader = csv.reader(open("drunks.csv", "rU"), dialect=csv.excel)

# The first line of the file is going to be the header row, which you don't want, so skip ahead.

reader.next()

# Okay, this gets a little weird. The reader object here LOOKS like a list, but it's not a list. So, we have to make it into one.

drunklist = [] # This creates an empty list for us to shove things.

for row in reader: # Starts a loop through the reader object
    drunklist.append(row) # Shoves the row into our list.

# Now, to be able to compare a thing to the previous item in a list, you have to use enumerate. Enumerate makes each item in a list into a tuple with the index number and the item itself. By having the index, we can move up and down the index with simple math.
    
for index, obj in enumerate(drunklist):  # This splits the tuple into the index number and the object, which is our list from the CSV
    if int(obj[1])>19: # obj[1] in this case is the number of drinks
        exclamation = "Holy shit!"
        judgement = "real drunk"
    elif int(obj[1])<10:
        exclamation = "Teetotaler alert!"
        judgement = "lightweight"
    else:
        exclamation = "Meh."
        judgement = "amateur"
        
    if obj[0]=="Sara": # obj[0] is the name in the list
        pronoun = "she"
    else:
        pronoun = "he"
    
    record = 45
    difference = record - int(obj[1])
    percent = (float(obj[1])/float(record))*100
    
    previous = drunklist[index-1] # Here is where you get the previous item. Create an object, and set it to be your listname[index-1] to go back, +1 to go forward.
        
    print "%s %s is a %s. %s drank %s in one sitting once. That's %i off the record of %i, or %.1f percent. Compare that to %s, who drank %s in one sitting once." % (exclamation, obj[0], judgement, pronoun.title(), obj[1], difference, record, percent, previous[0], previous[1])