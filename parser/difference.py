import json
import csv
import math

difference = {}

#the predicted cancer will tell us which of the [cancer]Avg.json files we have
#to load.  It will be opened as Average_data below

#one.tsv is single the patient input that the user submits
with open('one.tsv') as csvfile:
    reader = csv.reader(csvfile, delimiter='	')
    reader.next()
    Specimen_Array = [[row[3], row[7], row[8]] for row in reader if 'GAF' in row[6]]
with open ('BreastAvg.json') as filename:
   Average_data = json.load(filename)



#variables to hold the 2 largest and smallest changes in gene expression
#relative to the avg for that cancer

Current_Largest_One = 0
LargestID_One = ""
Current_Largest_Two = 0
LargestID_Two = ""
Current_Smallest_One = 0
SmallestID_One = ""
Current_Smallest_Two = 0
SmallestID_Two = ""

for item in Specimen_Array:
    if float(Average_data[item[1]] > 0.0):
        difference[item[1]] = float(item[2]) / float(Average_data[item[1]])
        if difference[item[1]] > Current_Largest_One:
            Current_Largest_Two = Current_Largest_One
            LargestID_Two = LargestID_One
            Current_Largest_One = difference[item[1]]
            LargestID_One = item[1]
        elif difference[item[1]] > Current_Largest_Two:
            Current_Largest_Two = difference[item[1]]
            LargestID_Two = item[1]

        #for biggest loss of expression we have to use difference between
        #0 and the average cancer expression, if we do the above we simply
        #get the first gene with 0
        if float(item[2]) == 0.0:
            if float(Average_data[item[1]]) > float(Current_Smallest_One):
                Current_Smallest_Two = float(Current_Smallest_One)
                SmallestID_Two = SmallestID_One
                Current_Smallest_One = float(Average_data[item[1]])
                SmallestID_One = item[1]
            elif float(Average[item[1]]) > float(Current_Smallest_Two):
                Current_Smallest_Two = float(Average_data[item[1]])
                SmallestID_Two = item[1]




#print "Largest expression increase" , LargestID_One, ":", Current_Largest_One
#print "Second expression increase" ,LargestID_Two, ":"  ,Current_Largest_Two
#print "Largest Decrease in expresion", SmallestID_One, "by" ,Current_Smallest_One, "From Avg"
#print "Second Largest Decrease in expresion" ,SmallestID_Two, "by" ,Current_Smallest_Two, "From Avg"

    
