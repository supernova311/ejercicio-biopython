from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os

filename= /home/supernova/Desktop/biopython-notebook/notebooks/data/ls_orchid.gbk
def summarize_contents(filename):
        records= list(SeqIO.parse(filename, "genbank"))
        print ("Path: ", os.path.dirname(filename))
        print ("num_records = %i records" % len(records))
        print ("n\n")
        for seq_record in SeqIO.parse(filename, "genbank"):
                print("Name: ", seq_record.name)
                print("ID: ", seq_record.id)
                print(Description: ", seq_record.descrition)

  summarize_contents(filename)
