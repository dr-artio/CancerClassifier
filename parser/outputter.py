#!/usr/bin/python

# expands the output of the cancer classifier
# prints links to more info




#cancer_type = targetfromML
#predicted cancer type needs to be changed to whatever the cancer that predicted is
print 'Would you like to know more?'

cancer_type = 'predicted cancer type from server'

if cancer_type == 'blood':
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25909835")
if cancer_type == 'breast':
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25900382")
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMH0032825/")
if cancer_type == 'head_and_neck':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0024390/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25911053")
if cancer_type == 'lung':
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25902866")
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0021885/")
	print ("http://www.smokefree.gov")
if cancer_type == 'kidney':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0024306/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25905038")
if cancer_type == 'brain':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0024760/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25810009")
if cancer_type == 'colorectal':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0024240/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/19133603")
if cancer_type == 'uterus':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0023667/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25906951")
if cancer_type == 'skin':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0024658/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25596540")
	print ("http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dhpc&field-keywords=sunscreen&rh=n%3A3760901%2Ck%3Asunscreen")
if cancer_type == 'prostate':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0021890/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25794813")
if cancer_type == 'ovary':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0023653/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25765457")
if cancer_type == 'pancreas':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0021889/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25824606")
if cancer_type == 'bladder':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0021881/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25882565")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25882566")
if cancer_type == 'liver':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0021884/")
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0021884/")
if cancer_type == 'cervix':
	print ("http://www.ncbi.nlm.nih.gov/pubmedhealth/PMHT0021883/")
	print ("http://www.ncbi.nlm.nih.gov/pubmed/25773118")




