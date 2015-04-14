00#!/bin/usr/python


#3-30-2015
#this program is supposed to parse .tsv files and extract gene, specimen identification and epxression information

import csv
from itertools import groupby
import json

class tumor:
        def __init__(self, gene, specimen, ):
                self.gene = gene
                self.specimen = specimen

        def __str__(self):
                return "%s : %s" % (self.gene, self.specimen)
if __name__=='__main__':
        gene_dict = {}
        Specimen_Array = []
        tumors = []
        with open('exp_seq_bladder.tsv') as csvfile:
                reader = csv.reader(csvfile, delimiter='	')
                reader.next()
                Specimen_Array = [[row[3], row[7], row[8]] for row in reader if 'GAF' in row[6]]
                
                for item in groupby(Specimen_Array, key=lambda x: x[0]):
                        gdict = {x[1]:float(x[2]) for x in item[1]}
                        tumors.append(tumor(gdict, item[0]))



with open ('json/bladder.json', mode = 'w') as filename:
  for i in tumors:
    json.dump(i.__dict__, filename)

