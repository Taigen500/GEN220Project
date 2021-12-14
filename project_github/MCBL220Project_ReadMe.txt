
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Overall directive: Assume an unknown or unverified protein sequence was obtained of the human protein UBR4. 
Here, however, the sequence will be downloaded and saved (UBR4_Q5T4S7.fasta).
Want to determine if homologs exist in mouse and fruit fly species.
Determine relatedness to possible paralogs.

_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 1: The sequence will be downloaded and saved (UBR4_Q5T4S7.fasta).
______________________________________________________________________________________________________

$ curl -o UBR4_Q5T4S7.fasta "https://www.uniprot.org/uniprot/Q5T4S7.fasta"

_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 2: Use hmmscan to search one protein sequence, the unknown human protein UBR4, against the pfam database to find highly significant local alignment matches.
_______________________________________________________________________________________________________

$ srun -p short -N 1 -n 4 --mem 4gb --pty bash -l 
$ module load hmmer
$ module load db-pfam 
 ## more readable format, make data into column delimited
$ hmmscan --domtblout UBR4_Pfam.hmmsearch.tbl $PFAM_DB/Pfam-A.hmm UBR4_Q5T4S7.fasta > UBR4_Pfam.hmmsearch.out
$ more UBR4_Pfam.hmmsearch.tbl
 ## full alignment format
$ hmmscan $PFAM_DB/Pfam-A.hmm UBR4_Q5T4S7.fasta > UBR4_Pfam.hmmsearch.out
$ more UBR4_Pfam.hmmsearch.out
_______________________________________________________________________________________________________
OUTPUT RESULT: From the top best E value and most matching domain sequences, it can be determined that the query sequence best matches human UBR4.
Top Results of matching domains: 
    PF19423.2 E3 ubiquitin-protein ligase UBR4 N-terminal 
    PF13764.9 E3 ubiquitin-protein ligase UBR4
    PF02207.23 Putative zinc finger in N-recognin (UBR box)
    PF02207.23 Putative zinc finger in N-recognin (UBR box)
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 3: Use fasta36 to verify matches against the human proteome since the previous search is against domain consensus sequences (not perfect matches). First download human proteome. Then run fasta36 with UBR4_Q5T4S7.fasta and human proteome.
_______________________________________________________________________________________________________

    # Generate human proteome file
$ module load miniconda3
$ python3 Script1.py 
    # printed out upon completion 
> The number of sequences from the processed human proteome UP000005640_9606: 20588
> The file humanproteome.fa was created in the users directory.
     # verify that the number of sequences matches the number at https://www.uniprot.org/proteomes/UP000005640, 20588 gene count
     
    # Run fasta36
$ srun -p short -N 1 -n 4 --mem 4gb --pty bash -l
$ module load fasta
$ fasta36 UBR4_Q5T4S7.fasta humanproteome.fa > UBR4xHumanPro.fasta36.out | more UBR4xHumanPro.fasta36.out
_______________________________________________________________________________________________________
OUTPUT RESULT:
The top hit corresponds to UBR4. The protein is UBR4.
sp|Q5T4S7|UBR4_HUMAN E3 ubiquitin-protein ligase U (5183) 33871 4815.6       0

COMMENTS:
Next best hits are:
sp|Q86XK2|FBX11_HUMAN F-box only protein 11 OS=Hom ( 927)  214 44.1  0.0052
    Motif that matches exactly: FFCDCGA within the UBR box 1650-1758 region of UBR4 and 823-926 region of F-box protein
sp|O95071|UBR5_HUMAN E3 ubiquitin-protein ligase U (2799)  205 42.6   0.045
sp|Q17RH7|TPRXL_HUMAN Putative protein TPRXL OS=Ho ( 258)  160 36.7    0.24
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 4: Get the proteome URLs for other species to test with the UBR4 sequence file for homologs (whole proteins or just domains = local alignment). Make an array. Paste array into script file: Script2.py
_______________________________________________________________________________________________________

# Uniprot -> proteomes button -> search drosophila/Mus musculus -> click proteome ID UP000005640/UP000000589 -> click and copy link from "Gene count: ..." "Download one protein sequence per gene (FASTA)" to download the whole proteome

Drosophila melanogaster (Fruit fly) 
https://www.uniprot.org/proteomes/UP000000803
Proteins: 22,088 
Gene Count: 13,821
Proteome files: 
https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000803/UP000000803_7227.fasta.gz

Mus musculus (Mouse)
https://www.uniprot.org/proteomes/UP000000589
Proteins: 55,341
Gene Count: 21,986
Proteome files: 
https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000589/UP000000589_10090.fasta.gz

    # Put these urls in an array
URLproteomes = {'https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000803/UP000000803_7227.fasta.gz', 'https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000589/UP000000589_10090.fasta.gz'}

    # paste array into Script2.py and save.
    
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 5: Create combined fasta database file of fruit fly and mouse proteomes
_______________________________________________________________________________________________________

$ module load miniconda3      ##needed for the biopython

    # Run Script2
$ python3 Script2.py
    # prompt and user input 
>    What to call this file (no space after colon):flymouseproteomes.fasta 

    # printed out upon completion
> The number of sequences from the processed proteomes: 35807
    # verify number of enteries in the combined fly & mouse proteome file is 35807 (13821 + 21,986 = 35807)
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 6: Align single human UBR4 protein to mouse and fly proteomes to find putative homologs and other proteins with similar domains.
_______________________________________________________________________________________________________

$ module load hmmer
$ phmmer UBR4_Q5T4S7.fasta flymouseproteomes.fasta > UBR4localalign.phmmer.out | more UBR4localalign.phmmer.out
_______________________________________________________________________________________________________
OUTPUT RESULT:
  
Top hits:
    E-value  score  bias    E-value  score  bias    exp  N  Sequence                       Description
    ------- ------ -----    ------- ------ -----   ---- --  --------                       -----------
          0 11478.4  55.9         0 11478.2  55.9   1.0  1  sp|A2AN08|UBR4_MOUSE            E3 ubiquitin-protein ligase UBR4
          0 3577.0  52.5          0 3225.8  19.8    4.7  4  sp|Q9VLT5|POE_DROME             Protein purity of essence OS=Dro
    1.1e-09   35.9   3.3    1.1e-09   35.9   3.3    2.1  1  sp|Q7TPD1|FBX11_MOUSE           F-box only protein 11 OS=Mus mus
    2.9e-08   31.2   3.9    2.9e-08   31.2   3.9    2.8  1  tr|Q9VH60|Q9VH60_DROME          F-box protein 11, isoform A OS=D
    5.8e-07   26.9  11.3    1.1e-06   26.0  11.3    1.3  1  sp|Q80TP3|UBR5_MOUSE            E3 ubiquitin-protein ligase UBR5
      1e-06   26.0   7.9    1.6e-06   25.4   7.9    1.1  1  sp|P51592|HYD_DROME             E3 ubiquitin-protein ligase hyd

COMMENTS:
These are full homologs of human UBR4:
    UBR4_MOUSE
    POE_DROME
    
These are proteins with domains that have high similarity to a UBR4 domain:
    For FBX11_MOUSE, the human UBR4 domain that matched:
        1650 edsdedslcnklctftitqke.fmnqhwyhchtckmvdgvgvctvcakvchkdheisyakygsffcdcgaked 1721 = UBR box domain
    For Q9VH60_DROME, the human UBR4 domain that matched:
        1650 edsdedslcnklctftitqk.efmnqhwyhchtckmvdgvgvctvcakvchkdheisyakygsffcdcgake 1720 = UBR box domain
        
F-box only protein 11 (927 aa, ~104 kDa) is encoded by the human FBXO11 gene. This protein plays a role in substrate recognition for the ubiquitin ligase complex.

These may be human UBR5 homologs:
    For UBR5_MOUSE, the human UBR4 domain that matched:
        1657 lcnklctftitqkefmnqhwyhchtckmvdgvgvctvcakvchkdheisyakyg.sffcdcgakedgsclalv 1728 = ALMOST the UBR box domain
    For HYD_DROME, the human UBR4 domain that matched:
        1641 aveeedsqaedsdedslc.nklctftitqkefmnqhwyhchtckmvdgvgvctvcakvchkdheisyakyg.sffcdcgakedgscl 1725 = ALMOST the UBR box domain
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 7: The "ubiquitin-protein ligase hyd" of HYD_DROME from the above hits seems like it is the human protein related to UBR4 called UBR5. Investigate the hits (only domain matches): sp|Q80TP3|UBR5_MOUSE and sp|P51592|HYD_DROME. Also get the human UBR5 protein sequence. Get protein sequence URLs from Uniprot. Make an array.
_______________________________________________________________________________________________________

sp|O95071|UBR5_HUMAN
Value = 'https://www.uniprot.org/uniprot/O95071.fasta'

sp|P51592|HYD_DROME 
Value = 'https://www.uniprot.org/uniprot/P51592.fasta'

sp|Q80TP3|UBR5_MOUSE
Value = 'https://www.uniprot.org/uniprot/Q80TP3.fasta'

UBR5querydict = {'https://www.uniprot.org/uniprot/O95071.fasta', 'https://www.uniprot.org/uniprot/P51592.fasta', 'https://www.uniprot.org/uniprot/Q80TP3.fasta'}

    # Paste the above array into the generated script: Script3.py
    # This script gets the sequences from Uniprot and makes one file.
    # Save the file.

    # run script
$ module load miniconda3
$ python3 Script3.py
    # prompt and user input
> What to call this multiple sequences file (no space after colon):UBR5_HumMouDro.fa
    # prints upon completion 
> The number of sequences in the multiple sequence file generated: 3

_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 8: See if the three sequences align well with muscle global alignment to determine the possiblity that HYD_DROME in Drodophila is a UBR5 homolog of human UBR5.
_______________________________________________________________________________________________________

$ module load muscle
muscle -clw -in "UBR5_HumMouDro.fa" -out "UBR5_MSA.txt"

_____________________________________________________________________________________________________
Result:
Appears to align well especially between human and mouse UBR5 sequences, with only gaps appearing in select segments between the Drosophila UBR5 sequence and the human/mouse UBR5 sequences. I believe that the HYD_DROME is a Drosophila UBR5 homolog of human UBR5. UBR5 is more related to UBR4 than to other UBR-box containing family members, this is likely why it matched.
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 9: Compare UBR4 with other UBR box (a zinc finger domain) containing proteins by searching just the box.
Search only UBR box against human proteome. This also determines other proteins in the human proteome with a UBR box-type domain and possible paralogs.
_______________________________________________________________________________________________________
## from Directive 2 output table: 
zf-UBR               PF02207.23    70 sp|Q5T4S7|UBR4_HUMAN -           5183   1.2e-06   28.6  14.8   1   2   3.6e-10   1.2e-06   28.6  14.8     2    59  1662  1720  1661  1726 0.82 Putative zinc finger in N-recognin (UBR box)
zf-UBR               PF02207.23    70 sp|Q5T4S7|UBR4_HUMAN -           5183   1.2e-06   28.6  14.8   2   2      0.31     1e+03    0.0   8.2    12    56  3657  3704  3648  3717 0.73 Putative zinc finger in N-recognin (UBR box)

## from Directive 2 out:
>> _  Putative zinc finger in N-recognin (UBR box)
   #    score  bias  c-Evalue  i-Evalue hmmfrom  hmm to    alifrom  ali to    envfrom  env to     acc
 ---   ------ ----- --------- --------- ------- -------    ------- -------    ------- -------    ----
   1 !   28.6  14.8   3.6e-10   1.2e-06       2      59 ..    1662    1720 ..    1661    1726 .. 0.82
   2 ?    0.0   8.2      0.31     1e+03      12      56 ..    3657    3704 ..    3648    3717 .. 0.73

  Alignments for each domain:
  == domain 1  score: 28.6 bits;  conditional E-value: 3.6e-10
                zf-UBR    2 Cskvfkkg....evvyrCltCsldetaviCeeCfkeskHegHelvelstkrnggvCdCGdee 59  
                            C+ +++++    + +y+C+tC++ +  ++C  C+k + H++He+ ++ +  ++++CdCG +e
  sp|Q5T4S7|UBR4_HUMAN 1662 CTFTITQKefmnQHWYHCHTCKMVDGVGVCTVCAKVC-HKDHEI-SYAK-YGSFFCDCGAKE 1720
                            6666655557779************************.******.4444.444******998 PP

  == domain 2  score: 0.0 bits;  conditional E-value: 0.31
                zf-UBR   12 vyrCltCsld..etaviCeeCfkeskHegHelvelstkrng.gvCd.CG 56  
                            + +C  Cs +  ++ ++C +C ++   + H++ ++++ +++ + C+ CG
  sp|Q5T4S7|UBR4_HUMAN 3657 TLQCPRCSASvpANPGVCGNCGENV-YQCHKCRSINYDEKDpFLCNaCG 3704
                            5678888888765678888888887.77777777777776678885477 PP



    # create a fasta file, UBR4_UBRbox.fa, by either copying the above (removing - and changing capitalization) or searching UBR4_Q5T4S7.fasta for the terminal sequences then pasting into text file:

    >sp|Q5T4S7|UBR4_HUMAN E3 ubiquitin-protein ligase UBR4 OS=Homo sapiens OX=9606 GN=UBR4 PE=1 SV=1; Putative zinc finger in N-recognin (UBR box), range 1662-1720
    CTFTITQKEFMNQHWYHCHTCKMVDGVGVCTVCAKVCHKDHEISYAKYGSFFCDCGAKE


    # Run fasta36
$ srun -p short -N 1 -n 4 --mem 4gb --pty bash -l
$ module load fasta
$ fasta36 UBR4_UBRbox.fa humanproteome.fa > UBRbox_HumanPro.fasta36.out | more UBRbox_HumanPro.fasta36.out
_______________________________________________________________________________________________________
OUTPUT RESULT:
The best scores are:                                      opt bits E(20588)
sp|Q5T4S7|UBR4_HUMAN E3 ubiquitin-protein ligase U (5183)  455 114.4 2.3e-25 *
sp|Q86XK2|FBX11_HUMAN F-box only protein 11 OS=Hom ( 927)  200 54.7 3.9e-08
sp|O95071|UBR5_HUMAN E3 ubiquitin-protein ligase U (2799)  185 51.2 1.3e-06  *
sp|Q8N806|UBR7_HUMAN Putative E3 ubiquitin-protein ( 425)  126 37.3   0.003  *
sp|Q9H5U6|ZCHC4_HUMAN rRNA N6-adenosine-methyltran ( 513)   99 31.0    0.29
sp|Q8IWV7|UBR1_HUMAN E3 ubiquitin-protein ligase U (1749)   99 31.0    0.97  *
sp|Q8IWV8|UBR2_HUMAN E3 ubiquitin-protein ligase U (1755)   95 30.1     1.9  *
sp|Q8NDW4|ZN248_HUMAN Zinc finger protein 248 OS=H ( 579)   85 27.7     3.1

* hits are apart of the UBR-box family
Only UBR5 has significant matches to UBR4.
Interestingly the FBX11, Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex, matches better to the UBR box domain (also substrate recognition) than UBR5 does.
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 10:  Align all five sequences to determine regions of homology between the sequences. First make multisequence file then use muscle.
________________________________________________________________________________________________________
    # Get the protein sequence URL from Uniprot
sp|Q5T4S7|UBR4_HUMAN (E(20588): 2.3e-25)  
    https://www.uniprot.org/uniprot/Q5T4S7.fasta
sp|O95071|UBR5_HUMAN (E(20588): 1.3e-06)
    https://www.uniprot.org/uniprot/O95071.fasta
sp|Q8N806|UBR7_HUMAN (E(20588): 0.003)
    https://www.uniprot.org/uniprot/Q8N806.fasta
sp|Q8IWV7|UBR1_HUMAN (E(20588): 0.97)
    https://www.uniprot.org/uniprot/Q8IWV7.fasta
sp|Q8IWV8|UBR2_HUMAN (E(20588): 1.9)
    https://www.uniprot.org/uniprot/Q8IWV8.fasta
    
    # make an array of the URLS
URLproteomes = {'https://www.uniprot.org/uniprot/Q5T4S7.fasta', 'https://www.uniprot.org/uniprot/O95071.fasta', 'https://www.uniprot.org/uniprot/Q8N806.fasta', 'https://www.uniprot.org/uniprot/Q8IWV7.fasta', 'https://www.uniprot.org/uniprot/Q8IWV8.fasta'}  

    # paste array into Script4.py and save 
    
    # run script
$ module load miniconda3      ##needed for the biopython
$ python3 Script4.py
    # prompt and user input 
>    What to call this file (no space after colon):UBRboxfam.fa 

    # printed out upon completion
> The number of sequences in the multiple sequence file generated: 5

    # run muscle multiple sequence alignment
$ module load muscle
muscle -clw -in "UBRboxfam.fa" -out "UBRbox_MSA.txt"

_____________________________________________________________________________________________________
Result:
The sequences are highly diverged but with some regions of homology. 
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 11: Interested in the C-terminal domain of UBR4.
Looking at just the C-terminal domain of human UBR4 to see if fly or mouse have proteins other than the UBR4 homologs contain this domain.
_______________________________________________________________________________________________________
    # from Directive 2 output table: 
E3_UbLigase_R4       PF13764.9    813 sp|Q5T4S7|UBR4_HUMAN -           5183         0 1141.0   0.0   1   1         0         0 1139.7   0.0     1   813  4367  5163  4367  5163 0.99 E3 ubiquitin-protein ligase UBR4
# Range 4367 to 5163 is very uninvestigated.
    
    # human UBR4 C-terminus sequence = UBR4_Cterm.fa
module load fasta
ssearch36 UBR4_Cterm.fa mouseproteome.fasta | more
ssearch36 UBR4_Cterm.fa flymouseproteomes.fasta > Cterm_moufly.ssearch.txt
_____________________________________________________________________________________________________
Result:

The best scores are:                                      s-w bits E(35806)
sp|A2AN08|UBR4_MOUSE E3 ubiquitin-protein ligase U (5180) 5277 1185.8       0
sp|Q9VLT5|POE_DROME Protein purity of essence OS=D (5322) 2629 593.7 2.9e-168
tr|A0A1D5RLM8|A0A1D5RLM8_MOUSE Predicted gene 1163 (5808)  176 45.3   0.004
sp|P23475|XRCC6_MOUSE X-ray repair cross-complemen ( 608)  126 34.9    0.56
tr|Q9VIE7|Q9VIE7_DROME Glutamine amidotransferase  ( 683)  120 33.5     1.6
sp|Q8BIJ7|RUFY1_MOUSE RUN and FYVE domain-containi ( 712)  116 32.6     3.2
sp|Q8VC56|RNF8_MOUSE E3 ubiquitin-protein ligase R ( 488)  112 31.8     3.7
tr|Q9Y0Y5|Q9Y0Y5_DROME Coatomer subunit epsilon OS ( 306)  106 30.7     5.2

COMMENTS: 
Other than the mouse and fly UBR4 homologs, nothing matches with high confidence. Although there is a hit on the cusp of significance: A0A1D5RLM8|A0A1D5RLM8_MOUSE Predicted gene 1163. Uniprot entry on this protein gives little information about it.
_______________________________________________________________________________________________________
________________________________________________________________________________________________________
Directive 12: Check the protein A0A1D5RLM8_MOUSE against human genome
_______________________________________________________________________________________________________
    # generate file 

curl -o A0A1D5RLM8_mouse.fa "https://www.uniprot.org/uniprot/A0A1D5RLM8.fasta"  
module load fasta
fasta36 A0A1D5RLM8_mouse.fa humanproteome.fa > A0A1D5RLM8_humanPor.fasta36.out | more A0A1D5RLM8_humanPor.fasta36.out
_____________________________________________________________________________________________________
Result:

The best scores are:                                      opt bits E(20588)
sp|Q8N7B9|EFCB3_HUMAN EF-hand calcium-binding doma ( 438) 2072 383.1 2.6e-105
sp|Q8IY85|EFC13_HUMAN EF-hand calcium-binding doma ( 973) 1197 226.4 8.4e-58
sp|Q9NZW4|DSPP_HUMAN Dentin sialophosphoprotein OS (1301)  400 83.9 8.6e-15
sp|Q7Z572|SPT21_HUMAN Spermatogenesis-associated p ( 469)  305 67.6 2.5e-10
sp|B3KS81|SRRM5_HUMAN Serine/arginine repetitive m ( 715)  260 59.3 1.2e-07
sp|Q08170|SRSF4_HUMAN Serine/arginine-rich splicin ( 494)  244 56.7 5.2e-07
sp|P35663|CYLC1_HUMAN Cylicin-1 OS=Homo sapiens OX ( 651)  221 52.4 1.3e-05
sp|Q17RH7|TPRXL_HUMAN Putative protein TPRXL OS=Ho ( 258)  208 50.7 1.7e-05
sp|Q7Z6E9|RBBP6_HUMAN E3 ubiquitin-protein ligase  (1792)  228 53.0 2.4e-05
sp|Q02224|CENPE_HUMAN Centromere-associated protei (2701)  230 53.1 3.4e-05
sp|Q96GE6|CALL4_HUMAN Calmodulin-like protein 4 OS ( 196)  193 48.2 7.5e-05
sp|O95218|ZRAB2_HUMAN Zinc finger Ran-binding doma ( 330)  196 48.4 0.00011
sp|Q5VTL8|PR38B_HUMAN Pre-mRNA-splicing factor 38B ( 546)  199 48.6 0.00016
sp|Q96QF7|ACRC_HUMAN Acidic repeat-containing prot ( 691)  197 48.1 0.00028
sp|Q9UKJ3|GPTC8_HUMAN G patch domain-containing pr (1502)  204 48.8 0.00036
sp|Q15648|MED1_HUMAN Mediator of RNA polymerase II (1581)  201 48.3 0.00056
sp|Q14978|NOLC1_HUMAN Nucleolar and coiled-body ph ( 699)  187 46.3 0.00098
sp|Q05519|SRS11_HUMAN Serine/arginine-rich splicin ( 484)  181 45.4  0.0012
sp|Q8N9E0|F133A_HUMAN Protein FAM133A OS=Homo sapi ( 248)  171 44.1  0.0016
sp|O95232|LC7L3_HUMAN Luc7-like protein 3 OS=Homo  ( 432)  177 44.8  0.0017
sp|Q15643|TRIPB_HUMAN Thyroid receptor-interacting (1979)  194 46.9  0.0018
sp|Q6KC79|NIPBL_HUMAN Nipped-B-like protein OS=Hom (2804)  197 47.2  0.0021
sp|Q13247|SRSF6_HUMAN Serine/arginine-rich splicin ( 344)  169 43.5  0.0033
sp|P27482|CALL3_HUMAN Calmodulin-like protein 3 OS ( 149)  155 41.5  0.0056
sp|Q13523|PRP4B_HUMAN Serine/threonine-protein kin (1007)  177 44.3  0.0057
sp|P29536|LMOD1_HUMAN Leiomodin-1 OS=Homo sapiens  ( 600)  170 43.3  0.0065
sp|Q86UP2|KTN1_HUMAN Kinectin OS=Homo sapiens OX=9 (1357)  177 44.1  0.0088

There is no UBR4  within the span of significant hits meaning that this mouse protein is likely not related to UBR4, although its domain structure might be important to the function in both proteins.
_______________________________________________________________________________________________________

Overall Conlcusion:
Human UBR4 is the protein.
There are UBR4 homologs in mouse and fruit fly species that align with high confidence.
The F-box 11 protein in humans (FBX11_HUMAN F-box only protein 11) and mice (Q7TPD1|FBX11_MOUSE) contains the highest confidence match to one of UBR4's domains (the UBR box in UBR4). It might indicate similar substrate recognition and will be pursued. 
Despite that UBR4 is apart of the UBR box containing protein family, the degree of matching to other members is insignificant and low.
Of the UBR box containing protein family members, UBR5 has the closest resemblance.
The UBR4 C-terminal domain is highly unique and does not have significant matches to other proteins within mice and fruit fly species.
The predicted mouse gene A0A1D5RLM8_MOUSE that matched to the UBR4 C-terminal domain 

_______________________________________________________________________________________________________


