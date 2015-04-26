#!/bin/usr/python

import csv
from itertools import groupby
import json
from operator import itemgetter


class tumor:
  def __init__(self, gene):
     self.gene = gene
  def __str__(self):
     return "%s : %s" % (self.gene)
    
              
def get_dict(cancer,bad_id):
  with open(cancer) as csvfile:
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
      else:
        TumorDict[current] = genedict
        genedict = {}
        current = item[0]
        gene = []
        TumorDict[current] = genedict
    for i in bad_id:
      del TumorDict[i] 
    return(TumorDict)    
        
        
def get_bad_ids(cancer):
  igcgsample = []
  genes = [[]]
  with open(cancer) as csvfile:
    reader = csv.reader(csvfile, delimiter='	')
    for row in reader:
      if 'sample' not in row[3] and 'GAF' in row[6]:
        if row[3] not in igcgsample:
          if igcgsample == []:
            genes[0].append(row[7])
          else:
            genes.append([row[7]])
          igcgsample.append(row[3])
        else:
          listindex = igcgsample.index(row[3])
          genes[listindex].append(row[7])
  num_genes = []
  for i in genes:
    num_genes.append(len(i))
    bad_id = []
  for i in range(len(num_genes)):
    if num_genes[i] != 20531:
      bad_id.append(igcgsample[i])
  return(bad_id)

def send_to_json(json_file,data):
  with open (json_file, mode = 'w') as filename:      
    json.dump(data, filename)

bad_breast = get_bad_ids('exp_seq_breast.tsv')
bad_colorectal = get_bad_ids('exp_seq_colorectal.tsv')
bad_prostate = get_bad_ids('exp_seq_prostate.tsv')
bad_uterus = get_bad_ids('exp_seq_uterus.tsv')

breast = get_dict('exp_seq_breast.tsv', bad_breast)
colorectal = get_dict('exp_seq_colorectal.tsv', bad_colorectal)
prostate = get_dict('exp_seq_prostate.tsv', bad_prostate)
uterus = get_dict('exp_seq_uterus.tsv', bad_uterus)

send_to_json('json/breast.json',breast)
send_to_json('json/colorectal.json',colorectal)
send_to_json('json/prostate.json',prostate)
send_to_json('json/uterus.json',uterus)
