#!/bin/usr/python

import csv
from collections import Counter

current = ''
specimen = []
igcgsample = []
submitted = []
analysis = []
specimen_model = []
igcgsample_model = []
submitted_model = []
analysis_model = []
with open('exp_seq_uterus.tsv') as csvfile:
  reader = csv.reader(csvfile, delimiter='	')
  for row in reader:
    if row[2] not in specimen:
      specimen.append(row[2])
      specimen_model.append(row[6])
    if row[3] not in igcgsample:
      igcgsample.append(row[3])
      igcgsample_model.append(row[6])
    if row[4] not in submitted:
      submitted.append(row[4])
      submitted_model.append(row[6])
    if row[5] not in analysis:
      analysis.append(row[5])
      analysis_model.append(row[6])
      
specimen_model.remove('gene_model')
igcgsample_model.remove('gene_model')
submitted_model.remove('gene_model')
analysis_model.remove('gene_model')

count_model =  Counter(specimen_model)
print('icgc_specimen' + str(count_model))
count_model =  Counter(igcgsample_model)
print('icgc_sample' + str(count_model))
count_model =  Counter(submitted_model)
print('icgc_submitted' + str(count_model))
count_model =  Counter(analysis_model)
print('icgc_analysis' + str(count_model))