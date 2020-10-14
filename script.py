from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
import os.path
def summarize_contents(filename):
  record = SeqIO.read(filename, "genbank")
        print("Name: ", record.name)
        print("Path: ", os.path.dirname(filename))
  record =list(SequIO.parse(filename, "genbank"))
        print("Recird_found: "%len (records))
  for seq_record in SeqIO.parse(filename,"genbank")
        print("ID:",record.id)
  location = SeqFeature.location(filname, "genbank")
        print("Location: " , SeqFeature.location)
  summarize_contents(filename)
