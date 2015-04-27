import csv
import json


Count ={}
Sum = {}
Average = {}
with open('exp_seq_breast.tsv') as csvfile:
    reader = csv.reader(csvfile, delimiter='	')
    print "hello"
    reader.next()
    Specimen_Array = [[row[3], row[7], row[8]] for row in reader if 'GAF' in row[6]]
    for item in Specimen_Array:
        if item[1] in Count:
            Count[item[1]] += 1
            Sum[item[1]] += float(item[2])
        else:
            Count[item[1]] = 1
            Sum[item[1]] = float(item[2])
    for key in Count:
        Average[key] = Sum[key] / Count[key]

        
with open ('json/BreastAvg.json', mode = 'w') as filename:      
        json.dump(Average, filename)
print "hello"
