00#!/bin/usr/python

import json

 
with open ('json/bladder.json') as filename:
   bladdder_data = json.load(filename)

with open ('json/blood.json') as filename:
   blood_data = json.load(filename)

with open ('json/brain.json') as filename:
   brain_data = json.load(filename)

with open ('json/breast.json') as filename:
   breast_data = json.load(filename)

with open ('json/cervix.json') as filename:
   cervix_data = json.load(filename)

with open ('json/colorectal.json') as filename:
   colorectal_data = json.load(filename)

with open ('json/headneck.json') as filename:
   headneck_data = json.load(filename)

with open ('json/kidney.json') as filename:
   kidney_data = json.load(filename)

with open ('json/liver.json') as filename:
   liver_data = json.load(filename)

with open ('json/lung.json') as filename:
   lung_data = json.load(filename)

with open ('json/ovary.json') as filename:
   ovary_data = json.load(filename)

with open ('json/pancreas.json') as filename:
   pancreas_data = json.load(filename)

with open ('json/prostate.json') as filename:
   prostate_data = json.load(filename)

with open ('json/skin.json') as filename:
   skin_data = json.load(filename)

with open ('json/uterus.json') as filename:
   uterus_data = json.load(filename)