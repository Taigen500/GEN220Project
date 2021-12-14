#!/usr/bin/env python3
#name: Script1-Copy1

import os,gzip
from Bio import SeqIO
from Bio.Seq import Seq

URLproteomes = {'https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000803/UP000000803_7227.fasta.gz', 'https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000589/UP000000589_10090.fasta.gz'}
#fasta=os.path.basename(URLproteomes)
#if not os.path.exists(fasta):
#    os.system("curl -O {}".format(URLproteomes))
    
    
#UBR5querydict = {'https://www.uniprot.org/uniprot/O95071.fasta', 'https://www.uniprot.org/uniprot/P51592.fasta', 'https://www.uniprot.org/uniprot/Q80TP3.fasta'}

seqcounter = 0
fastaproteome = []
for url in URLproteomes:
    fasta=os.path.basename(url)
    if not os.path.exists(fasta):
        os.system("curl -O {}".format(url))
    with gzip.open( fasta ,"rt") as infh:
        for seq_record in SeqIO.parse( infh , "fasta"):
            fastaproteome.append(seq_record)
            seqcounter += 1

filename = input("What to call this file (no space after colon):")
SeqIO.write(fastaproteome, filename, "fasta")

print("The number of sequences from the processed proteomes: {}".format(seqcounter))



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