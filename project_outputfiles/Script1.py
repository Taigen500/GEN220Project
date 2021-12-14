#!/usr/bin/env python3

import os,gzip
from Bio import SeqIO
from Bio.Seq import Seq

# UP000005640_9606 from https://www.uniprot.org/proteomes/UP000005640 on Dec 2021
URL= "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000005640/UP000005640_9606.fasta.gz"
filename = "humanproteome.fa"
fasta=os.path.basename(URL)
if not os.path.exists(fasta):
    os.system("curl -O {}".format(URL))

seqcounter = 0
fastaproteome = []
with gzip.open(fasta,"rt") as infh:
    for seq_record in SeqIO.parse( infh , "fasta"):
        fastaproteome.append(seq_record)
        seqcounter += 1

SeqIO.write(fastaproteome, filename, "fasta")

print("The number of sequences from the processed human proteome UP000005640_9606: {}".format(seqcounter))
print("The file {} was created in the users directory.".format(filename))



# from Lec 2/3 python, lec 4 too
"""
import urllib.request
fastaurl= input("From Uniprot, paste the proteome fasta database url of a species here:")
open = urllib.request.urlopen(fastaurl)
for line in info:
    linestrip = line.decode('UTF-8').strip()
    print(linestrip)
curl url"https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000803/UP000000803_7227.fasta.gz" > "Flyproteome.fasta.gz"

gunzip FlyMouseproteomes.fasta.gz

grep -c ">" FlyMouseproteomes.fasta
#https://techiesanswer.com/python-solution/how-to-run-unix-system-commands-from-python-program/

Info from HW3 mostly
"""