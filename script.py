from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os.path
def summarize_contents(filename):
  record = SeqIO.read(filename, "genbank")
        print("Name: ", record.name)
        print("Path: ", os.path.dirname(filename))
  for seq_record in SeqIO.parse(filename,"genbank"):
        print("ID:",record.id)
  summarize_contents(filename)
