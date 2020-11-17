from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation, SeqFeature
from .Interfaces import SequenceIterator, SequenceWriter
from Bio.SeqRecord import SeqRecord
import os.path


filename = "/mnt/c/Users/Arian Vázquez/Desktop/ejercicio-biopython/data/ls_orchid.gbk"
def summarize_contents(filename):
        lista = []
        lista = os.path.split(filename)
        records= list(SeqIO.parse(filename, "genbank"))
        cadena  = ("file: " + lista[1])
        cadena += ("path: " + lista[2])
        cadena += ("num_records = %i records" % len (records))
        for seq_record in SeqIO.parse(filename, "genbank"):
                cadena += ("Name: ", seq_record.name)
                cadena += ("ID: ", seq_record.id)
                cadena += ("Description: " + str (seq_record.descrition))
        print(cadena)

from Bio.Seq import Seq

list_of_seqs = [Seq("acgtaggttaccatcatg"), Seq("cgtgattggcctagccgt")]
def concatenate_and_get_reverse_of_complement():          
        concatenated = Seq("")
        for s in list_of_seqs():
                concatenated += s
        concatenated
        my_seq = concatenated
        print(my_seq.reverse_complement())


################################################
#Extrae las secuencias del archivo
###############################################
      
def extract_sequences
        if not os.path.exists("result_Fasta"):
                os.makedirs("result_Fasta")

        records = list(SeqIO.parse(fasta, "fasta"))
        for i, record in enumerate(records):
                file = open(f"result_Fasta/sequence{i}.fasta", "w")
                file.write(f">{record.id}\n{record.seq}")
                file.close()

        return print(f"sequence{i}.fasta")

extract_sequences(FASTA)


