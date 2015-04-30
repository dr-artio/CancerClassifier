import json
import csv
import math



# the predicted cancer will tell us which of the [cancer]Avg.json files we have
#to load.  It will be opened as Average_data below

#one.tsv is single the patient input that the user submits
with open('one.tsv') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    reader.next()
    Specimen_Array = [[row[3], row[7], row[8]] for row in reader if 'GAF' in row[6]]
with open('BreastAvg.json') as filename:
    Average_data = json.load(filename)



#variables to hold the 2 largest and smallest changes in gene expression
#relative to the avg for that cancer

def get_gene_ids(data, avg_data):
    """
    Function expects two dictionaries with
    expression values and same set of keys
    :param data:
        First dict with current values
    :param avg_data:
        Second dict with avg values
    :return:
        GeneIDs 2 smallest and 2 largest
    """
    difference = {}
    Current_Largest_One = 0
    LargestID_One = ""
    Current_Largest_Two = 0
    LargestID_Two = ""
    Current_Smallest_One = 0
    SmallestID_One = ""
    Current_Smallest_Two = 0
    SmallestID_Two = ""

    for item in data:
        value = data[item]
        avg_value = avg_data[item]

        if avg_value > 0:
            difference[item] = value / avg_value
            if difference[item] > Current_Largest_One:
                 Current_Largest_Two = Current_Largest_One
                 LargestID_Two = LargestID_One
                 Current_Largest_One = difference[item]
                 LargestID_One = item
            elif difference[item] > Current_Largest_Two:
                Current_Largest_Two = difference[item]
                LargestID_Two = item
        if value == 0:
            if avg_value > float(Current_Smallest_One):
                Current_Smallest_Two = float(Current_Smallest_One)
                SmallestID_Two = SmallestID_One
                Current_Smallest_One = float(Average_data[item])
                SmallestID_One = item
            elif float(Average_data[item]) > float(Current_Smallest_Two):
                Current_Smallest_Two = float(Average_data[item])
                SmallestID_Two = item

    return SmallestID_One, SmallestID_Two, LargestID_One, LargestID_Two



    
