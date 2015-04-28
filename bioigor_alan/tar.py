
import tarfile
import gzip
from collections import OrderedDict
import pickle
import numpy as np


def process_tsv(lines):
    patient = lines[0][0]
    genes_p = {}
    cancer_dict = {}
    with open("models/cancer_ids.txt") as f:
        canc = f.readlines()
    canc = map(lambda x: x.strip().split(), canc)
    for x, y in canc:
        cancer_dict[int(x)] = y
    for line in lines[1:]:
        line = line.split()
        genes_p[line[7]] = float(line[8])
    with open("models/gene_ids.txt") as f:
        ids = f.readlines()
    ids = map(lambda x: x.strip(), ids)
    genes_vector = []
    for aidi in ids:
        genes_vector.append(genes_p.get(aidi, 0))
    model = pickle.load(open("models/SVMlin2.pkl", 'rb'))
    outcome = model.predict([genes_vector])
    return cancer_dict[outcome[0]]



def process(tarfilename):
    output = []
    t = tarfile.open(tarfilename, 'r')
    for filename in t.getnames():
        try:
            f = t.extractfile(filename)
        except KeyError:
            print 'ERROR: Did not find %s in tar archive' % filename
        else:
            if 'gz' not in filename:
                metadata = f.read()
                try:
                    metadata = metadata.split("__")
                except Exception:
                    metadata = ["no metadata"]
                output.extend(metadata)
            else:
                with open("biofiles/" + filename, "wb") as ff:
                    ff.write(f.read())
                fff = gzip.open("biofiles/" + filename)
                file_content = fff.readlines()
                fff.close()
                outcome = process_tsv(file_content)
                output.append(outcome)
    return "\n".join(output)





#process('file_1.tar')
