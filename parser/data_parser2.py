00#!/bin/usr/python


#3-30-2015
#this program is supposed to parse .tsv files and extract gene, specimen identification and epxression information

import csv
from itertools import groupby
import json
from operator import itemgetter

class tumor:
        def __init__(self, gene):
                self.gene = gene

        def __str__(self):
                return "%s : %s" % (self.gene)
if __name__=='__main__':
        gene_dict = {}
        Specimen_Array = []
        tumors = []
        with open('exp_seq_uterus.tsv') as csvfile:
                reader = csv.reader(csvfile, delimiter='	')
                reader.next()
                Specimen_Array = [[row[3], row[7], row[8]] for row in reader if 'GAF' in row[6]]
                Specimen_Array.sort(key=lambda x: x[0])
                current = Specimen_Array[0][0]
                gene = []
                TumorDict = {}
                genedict = {}
                for item in Specimen_Array:
                        if item[0] == current:
                                genedict[item[1]] = float(item[2])
                                #print item[0]
                        else:
                                TumorDict[current] = genedict
                                current = item[0]
                                gene = []
                TumorDict[current] = genedict

with open ('json/uterus.json', mode = 'w') as filename:      
        json.dump(TumorDict, filename)
 
  
#with open ('json/bladder.json') as filename:
#   data = json.load(filename)
