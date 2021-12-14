#!/usr/bin/env python3
# name: Script3.py

import os
from Bio import SeqIO
from Bio.Seq import Seq

UBRboxarray = {'https://www.uniprot.org/uniprot/Q5T4S7.fasta', 'https://www.uniprot.org/uniprot/O95071.fasta', 'https://www.uniprot.org/uniprot/Q8N806.fasta', 'https://www.uniprot.org/uniprot/Q8IWV7.fasta', 'https://www.uniprot.org/uniprot/Q8IWV8.fasta'}

seqcounter = 0
multiSeqdict = []
for url in UBRboxarray:
    fasta=os.path.basename(url)
    if not os.path.exists(fasta):  
        os.system("curl -O {}".format(url))
    for seq_record in SeqIO.parse( fasta , "fasta"):
        multiSeqdict.append(seq_record)
        seqcounter += 1

filename = input("What to call this multiple sequences file (no space after colon):")

SeqIO.write(multiSeqdict, filename, "fasta")

print("The number of sequences in the multiple sequence file generated: {}".format(seqcounter))


# from Lec 2/3 python, lec 4 too, HW3, and Script1.py
"""
-----------------------------------------first script

import os
from Bio import SeqIO
from Bio.Seq import Seq

UBR5querydict = {'https://www.uniprot.org/uniprot/O95071.fasta', 'https://www.uniprot.org/uniprot/P51592.fasta', 'https://www.uniprot.org/uniprot/Q80TP3.fasta'}

seqcounter = 0
multiSeqdict = []
for url in UBR5querydict:
    fasta=os.path.basename(url)
    if not os.path.exists(fasta):
        os.system("curl -O {}".format(url))
    for seq_record in SeqIO.parse( fasta , "fasta"):
        multiSeqdict.append(seq_record)
        seqcounter += 1

filename = input("What to call this multiple sequences file (no space after colon):")

SeqIO.write(multiSeqdict, filename, "fasta")

print("The number of sequences in the multiple sequence file generated: {}".format(seqcounter))
-------------------------------------------first script run
ehay001@jupyter:~/project$ srun -p short -N 1 -n 4 --mem 4gb --pty bash -l
ehay001@i04:~/project$ module unload miniconda2/4.4.10 
ehay001@i04:~/project$ module load miniconda3

ehay001@i04:~/project$ python3 Script2.py 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2937  100  2937    0     0   4775      0 --:--:-- --:--:-- --:--:--  4767
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2943  100  2943    0     0   4946      0 --:--:-- --:--:-- --:--:--  4954
What to call this multiple sequences file (no space after colon):UBR5_HumMouDro.fa
The number of sequences in the multiple sequence file generated: 3
"""




"""
--------------------------second script, commandline list input
import os
from Bio import SeqIO
from Bio.Seq import Seq

UBR5querydict = {nput("The list of urls to parse:")}

seqcounter = 0
multiSeqdict = []
for url in UBR5querydict:
    fasta=os.path.basename(url)
    if not os.path.exists(fasta):
        os.system("curl -O {}".format(url))
    for seq_record in SeqIO.parse( fasta , "fasta"):
        multiSeqdict.append(seq_record)
        seqcounter += 1

filename = input("What to call this multiple sequences file (no space after colon):")

SeqIO.write(multiSeqdict, filename, "fasta")

print("The number of sequences in the multiple sequence file generated: {}".format(seqcounter))

--------------------------second script run
ehay001@i55:~/project$ module unload miniconda2/4.4.10
ehay001@i55:~/project$ module load miniconda3
ehay001@i55:~/project$ python3 Script2.py

The list of urls to parse:'https://www.uniprot.org/uniprot/O95071.fasta', 'https://www.uniprot.org/uniprot/P51592.fasta', 'https://www.uniprot.org/uniprot/Q80TP3.fasta'

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16180  100 16180    0     0  14857      0  0:00:01  0:00:01 --:--:-- 14871

<!DOCTYPE html SYSTEM "about:legacy-compat">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head><title>Error</title><meta content="IE=edge" http-equiv="X-UA-Compatible"/><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"/><meta content="width=device-width, initial-scale=1" name="viewport"/><link href="/" rel="home"/><link href="https://creativecommons.org/licenses/by/4.0/" rel="license"/><link type="image/vnd.microsoft.icon" href="/favicon.ico" rel="shortcut icon"/><link href="/uniprot.min.css2021_04" type="text/css" rel="stylesheet"/><link href="/tippy.css" type="text/css" rel="stylesheet"/><script type="text/javascript">
                        var BASE = '/';
                </script><script src="/js-compr.js2021_04" type="text/javascript"></script><script type="text/javascript">
                                uniprot.isInternal = false;
                                uniprot.namespace = 'uniprot';
                                uniprot.releasedate = '2021_04';
                        </script><script type="text/javascript">
                        ;
                </script><meta content="nositelinkssearchbox" name="google"/></head><body class="namespace-uniprot" typeof="WebPage" prefix="up: http://purl.uniprot.org/core/" vocab="http://schema.org/"><span id="evidenceToolTip" style="display:none">&#xd;
                                    &lt;p>An evidence describes the source of an annotation, e.g. an experiment that has been published in the scientific literature, an orthologous protein, a record from another database, etc.&lt;/p>&#xd;
&#xd;
&lt;p>&lt;a href="/manual/evidences">More...&lt;/a>&lt;/p>&#xd;
                                </span><p style="display:none"><a accesskey="2" href="#content">Skip Header</a></p><div id="masthead-container"><div class="masthead" id="local-masthead"><div id="local-title"><a id="logo" accesskey="1" href="/"><img alt="" src="/images/logos/Logo_medium.png" title="UniProt home"/></a></div><div class="namespace-uniprot" id="local-search"><form method="get" action="/uniprot" id="search-form"><div id="namespace-background"><div class="searchBoxIndicator" style="display:none" id="searchBoxIndicator1"> </div><div onclick="location.href=&apos;/help/text-search&apos;;" class="searchBoxIndicator" style="display:none" id="searchBoxIndicator2"> </div><div onclick="location.href=&apos;/help/advanced_search &apos;;" class="searchBoxIndicator" style="display:none" id="searchBoxIndicator3"> </div><a class="namespace-select" id="select-namespace" onclick="return false;" href=""><span class="caret_white" id="selected-namespace">UniProtKB</span></a><ul style="display:none" class="select-namespace-options"><a href="#" class="closeBox" id="closeNamespaceOptions">x</a><li><ul><li class="fixedHeight_namespaces"><h3 class="namespace_uniprot"><a class="namespace-option uniprot" href="#" id="uniprot">UniProtKB</a></h3><p>Protein knowledgebase</p></li><li class="fixedHeight_namespaces"><h3 class="namespace_uniparc"><a class="namespace-option uniparc" href="#" id="uniparc">UniParc</a></h3><p>Sequence archive</p></li><li class="fixedHeight_namespaces"><h3 class="namespace_help"><a class="namespace-option help" href="#" id="help">Help</a></h3><p>Help pages, FAQs, UniProtKB manual, documents, news archive and Biocuration projects.</p></li></ul></li><li><ul><li class="fixedHeight_namespaces"><h3 class="namespace_uniref"><a class="namespace-option uniref" href="#" id="uniref">UniRef</a></h3><p>Sequence clusters</p></li><li class="fixedHeight_namespaces"><h3 class="namespace_proteomes"><a class="namespace-option proteomes" href="#" id="proteomes">Proteomes</a></h3><p>Protein sets from fully sequenced genomes</p></li><li class="fixedHeight_namespaces"><h3 class="namespace_unirule">Annotation systems</h3><p class="supportingLeadingText">Systems used to automatically annotate proteins with high accuracy:</p><ul class="supportingDataOptions"><li><a class="namespace-option supporting" href="#" id="unirule">UniRule (Expertly curated rules)</a></li><li><a class="namespace-option supporting" href="#" id="arba">ARBA (System generated rules)</a></li></ul></li></ul></li><li><ul><li class="fixedHeight_namespaces"><h3 class="supporting"><span>Supporting data</span></h3><p class="supportingLeadingText">Select one of the options below to target your search:</p><ul class="supportingDataOptions"><li><a class="namespace-option supporting" href="#" id="citations">Literature citations</a></li><li><a class="namespace-option supporting" href="#" id="taxonomy">Taxonomy</a></li><li><a class="namespace-option supporting" href="#" id="keywords">Keywords</a></li><li><a class="namespace-option supporting" href="#" id="locations">Subcellular locations</a></li><li><a class="namespace-option supporting" href="#" id="database">Cross-referenced databases</a></li><li><a class="namespace-option supporting" href="#" id="diseases">Human diseases</a></li></ul></li></ul></li></ul><input value="" id="topQuery" type="hidden"/><div id="queryContainer"><input autocomplete="off" autofocus="autofocus" id="query" value="" accesskey="4" name="query" type="search"/></div><a class="caret_grey" href="#" id="advanced-search-toggle">Advanced</a><input value="score" name="sort" type="hidden"/><a id="search-button" title="Search" data-icon="1" class="icon icon-functional button">Search</a><div style="display:none" class="advSearch" id="query-builder-container"><a href="#" class="closeBox" id="closeAdvanceSearch">x</a><div id="advanced-search"></div></div></div></form></div><div id="nav"><ul id="local-nav"><li class="mobileHomeLink"><a href="/">Home</a></li><li class="first"><a class="tooltipped" title="Find regions of local similarity between sequences" href="/blast" id="top-blast-link">BLAST</a></li><li><a class="tooltipped" title="Align two or more protein sequences with the Clustal Omega program" href="/align" accesskey="9" id="top-align-link">Align</a></li><li class="last"><a class="tooltipped" title="Submit a list of identifiers to retrieve the corresponding UniProt entries, or to map them from or to an external database" rel="help" href="/uploadlists" id="upload-lists-nav">Retrieve/ID mapping</a></li><li class="last"><a class="tooltipped" title="Submit a list of peptides to find UniProt sequences containing them" rel="help" href="/peptidesearch" id="peptidesearch-lists-nav">Peptide search</a></li><li id="sparql-list" class="last"><a class="tooltipped" title="Query the UniProt Knowledge Graph with SPARQL" href="https://sparql.uniprot.org/sparql" id="sparql-lists-nav">SPARQL</a></li><li class="functional last"><a accesskey="9" href="/contact" id="contact">Contact</a></li><li class="functional"><a rel="help" href="/help/" id="help">Help</a></li></ul></div></div></div><div class="warn" id="browserwarning">You are using a version of browser that may not display all the features of this website. Please consider upgrading <a href="/help/browser_support">your browser</a>.</div><main class="uniprot" property="schema:mainEntity" resource="" typeof="" id="content"><section id="page-header"><div style="position:relative;"><div id="top-right-actions"><div style="display:none" id="basket"><a href="#" data-icon="b" class="closed basket-empty icon icon-static caret_white button" id="basket-list">Basket <span style="display:none" id="basket-count">0</span></a></div><div style="z-index: 3;display:none" id="basket-contents"><div id="closeBasket"><span class="basketText">(max 400 entries)</span><button class="closeBox">x</button></div><div id="emptyBasketContent"><h3><span class="context-help tooltipped-click">
                                        Your basket is currently empty. <sup> i</sup><span style="display:none"><span class="tooltipped">
                                    &lt;p>When browsing through different UniProt proteins, you can use the 'basket' to save them, so that you can back to find or analyse them later.&lt;p>&lt;a href='/help/basket' target='_top'>More...&lt;/a>&lt;/p></span></span></span></h3><p>Select item(s) and click on "Add to basket" to create your own collection here<br/> (400 entries max)<br/></p><div id="emptyBasketContentHelp"></div></div><div style="display:none" id="loadingBasketContent"></div><div id="filledBasketContents"><ul id="basketTabs" class="tabs"><li><a id="uniprotBasketTab" class="uniprot tab basketTab">UniProtKB (<span class="uniprot-basket-count">0</span>)</a></li><li><a id="unirefBasketTab" class="uniref tab basketTab">UniRef (<span class="uniref-basket-count">0</span>)</a></li><li><a id="uniparcBasketTab" class="uniparc tab basketTab">UniParc (<span class="uniparc-basket-count">0</span>)</a></li></ul><div class="tabsContent" style="display: none" id="basket-uniprot"></div><div class="tabsContent" style="display: none" id="basket-uniref"></div><div class="tabsContent" style="display: none" id="basket-uniparc"></div></div><div id="basket-actions"><div class="action-buttons-grouped"><button title="Select two or more entries and click here to align them" data-icon="i" class="button icon icon-functional align disabled" id="basket-align-button">Align</button><button data-icon="t" title="Select an entry and click here to run a BLAST search on it" class="button icon-functional icon blast disabled" id="basket-blast-button">BLAST</button><button title="Map ids to other databases" class="button icon-functional disabled" id="basket-map-button">Map Ids</button><button data-icon="=" title="Download results" class="button icon icon-functional download disabled" id="basket-download-button">Download</button><span class="icon-right"><button title="Full View" class="button fullView disabled" id="basket-view-button">Full View</button><button title="Remove Selected entries" class="button remove disabled" id="basket-remove-button">Remove</button><button title="Clear basket" class="button clear disabled" id="basket-clear-button">Clear</button></span></div></div></div><form action="/align/" method="post" id="basket-alignForm"><input value="no" name="landingPage" type="hidden"/><input value="clustalo" name="program" type="hidden"/><input value="yes" name="redirect" type="hidden"/><input value="" name="alignQuery" id="basket-alignQuery" type="hidden"/></form><form action="/blast/" method="post" id="basket-blastForm"><input value="yes" name="redirect" type="hidden"/><input value="no" name="landingPage" type="hidden"/><input value="uniprotkb_refprotswissprot" name="dataset" type="hidden"/><input value="10" name="threshold" type="hidden"/><input value="" name="matrix" type="hidden"/><input value="false" name="filter" type="hidden"/><input value="true" name="gapped" type="hidden"/><input value="250" name="numal" type="hidden"/><input value="" id="basket-blastQuery" name="blastQuery" type="hidden"/></form><form action="" method="post" id="basket-downloadForm"><input value="" name="query" type="hidden"/></form></div></div></section> <br clear="all"/><div class="main"><div id="noResultsMessage"><h2>Sorry, this page was not found.</h2><p>
                                        Can't find what you are looking for? Please
                                        <a href="/contact?subject=">contact us</a></p><p>The resource you requested could not be found. It has either been
                        moved, never existed, or you might have mistyped the address.
                </p><ul><li>
                                If you believe this is an error or need further help
                                <a href="/contact">please contact us</a>
                                .
                        </li><li>
                                You can also start navigating from the
                                <a href="/">main page</a>
                                .
                        </li><li>You can also try using the search functionality above.</li></ul></div></div></main><footer id="page-footer"><section><h5>Tools</h5><ul><li><a href="/blast">BLAST</a></li><li><a href="/align">Align</a></li><li><a href="/uploadlists">Retrieve/ID mapping</a></li><li><a href="/peptidesearch">Peptide search</a></li></ul></section><section><h5>Core data</h5><ul><li><a href="/uniprot">Protein knowledgebase (UniProtKB)</a></li><li><a href="/uniref">Sequence clusters (UniRef)</a></li><li><a href="/uniparc">Sequence archive (UniParc)</a></li><li><a href="/proteomes">Proteomes</a></li></ul></section><section><h5>Supporting data</h5><ul><li><a href="/citations">Literature citations</a></li><li><a href="/taxonomy">Taxonomy</a></li><li><a href="/keywords">Keywords</a></li><li><a href="/locations">Subcellular locations</a></li><li><a href="/database">Cross-referenced databases</a></li><li><a href="/diseases">Diseases</a></li></ul></section><section><h5>Information</h5><ul><li><a href="/help/about">About UniProt</a></li><li><a href="/help">Help</a></li><li><a href="/help/?fil=section:faq">FAQ</a></li><li><a href="/help/?fil=section:manual">UniProtKB manual</a></li><li><a href="/help/technical">Technical corner</a></li><li><a href="/help/?query=*&amp;fil=section:biocuration">Expert biocuration</a></li></ul></section><section><div class="uniprotlogo"><img src="/images/logos/uniprot-rgb-optimized.svg"/></div><span>&copy; 2002 &ndash;
                        <span property="copyrightYear">2021</span>
                        <a accesskey="9" href="/help/about">UniProt Consortium</a> | <a href="/help/license">License &amp; Disclaimer</a> | <a href="/help/privacy">Privacy Notice</a></span><div resource="/help/about#UniProt" id="logos" typeof="NGO" property="creator"><span hidden="hidden" property="name">UniProt Consortium</span><span resource="/help/about#EBI" typeof="Organization" class="ebi" property="member"><span class="hidden" property="name">European Bioinformatics Institute</span><a href="https://www.ebi.ac.uk/" property="url"></a></span><span resource="/help/about#PIR" typeof="Organization" class="pir" property="member"><span class="hidden" property="name">Protein Information Resource</span><a href="https://pir.georgetown.edu/" property="url"></a></span><span resource="/help/about#SIB" typeof="Organization" class="sib" property="member"><span class="hidden" property="name">SIB Swiss Institute of Bioinformatics</span><a href="https://www.sib.swiss/" property="url"></a></span></div></section></footer><div id="elixir-coretrust-ribbon"><a typeof="Organization" href="https://www.coretrustseal.org/" property="reviewedBy"><img alt="UniProt is an CoreTrustSeal certified data repository" id="coretrustseal-logo" src="/images/logos/CoreTrustSeal-logo-transparent.png"/></a><a typeof="Organization" href="https://www.elixir-europe.org/platforms/data/core-data-resources" property="reviewedBy"><img height="64px" width="64px" id="elixir-cdr-logo" src="/images/elixir-cdr.gif"/><h5><span class="elixir-banner-name">UniProt is an ELIXIR core data resource</span></h5></a></div><div id="UniProt-Funding"><span>
                        Main <a href="https://www.uniprot.org/help/about">funding</a> by:
                </span><a property="funder" typeof="Organization" href="https://www.nih.gov/" id="nihFundingLink" class="funder"><span property="name">National Institutes of Health</span></a><a property="funder" typeof="Organization" href="https://www.embl.org/" id="ebiFundingLink" class="funder"><img src="/images/embl-logo.png" style="width:auto;height:45px;"/><span hidden="hidden" property="name">The European Molecular Biology Laboratory</span></a><a property="funder" typeof="GovernmentOrganization" href="https://www.sbfi.admin.ch/sbfi/en/home.html" id="seriFundingLink" class="funder"><img src="/images/seri-logo.png"/><span hidden="hidden" property="name">State Secretariat for Education, Research and Innovation</span><span hidden="hidden" property="alternateName">SERI</span></a></div><script src="https://www.google-analytics.com/analytics.js" async="async"></script><script>
                                                window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
                                                ga('create', 'UA-6228219-1', 'auto');
                                                ga('set', 'dimension1', '');
                                                ga('set', 'dimension2', '');
                                                ga('set', 'anonymizeIp', true);
                                                ga('set', 'forceSSL', true);
                                                ga('send', 'pageview');
                                        </script><div class="privacy-panel" id="privacy-panel"><p class="privacy-panel__text">We'd like to inform you that we have updated our <a href="/help/privacy">Privacy Notice</a> to comply
with Europe’s new General Data Protection Regulation (GDPR) that applies since 25 May 2018.</p><a id="privacy-panel-accept" class="privacy-panel__button">Do not show this banner again</a></div><script src="/scripts/node-bundle.js" type="text/javascript"></script><script src="/scripts/common-bundle.js" type="text/javascript"></script></body></html>>sp|Q80TP3|UBR5_MOUSE E3 ubiquitin-protein ligase UBR5 OS=Mus musculus OX=10090 GN=Ubr5 PE=1 SV=2
MTSIHFVVHPLPGTEDQLNDRLREVSEKLNKYNLNSHPPLNVLEQATIKQCVVGPNHAAF
LLEDGRICRIGFSVQPDRLELGKPDNNDGSKLNSSSGTGRTSRPGRTSDSPWFLSGSETL
GRLAGNTLGSRWSSGVGGSGGGSSGRSSAGARDSRRQTRVIRTGRDRGSGLLGSQPQPVI
PASVIPEELISQAQVVLQGKSRSVIIRELQRTNLDVNLAVNNLLSRDDEDGDDGDDTASE
SYLPGEDLMSLLDADIHSAHPSVIIDADAMFSEDISYFGYPSFRRSSLSRLGSSRERDSE
LLRERESVLRLRERRWLDGASFDNERGSTSKEGESNPDKKNTPVQSPVSLGEDLQWWPDK
DGTKFTCIGALYSELLAVSSKGELYQWKWSESEPYRNAQNPSLHHPRATFLGLTNEKIVL
LSANSIRATVATENNKVATWVDETLSSVASKLEHTAQTYSELQGERIVSLHCCALYTCAQ
LENNLYWWGVVPFSQRKKMLEKARAKNKKPKSSAGISSMPNITVGTQVCLRNNPLYHAGA
VAFSISAGIPKVGVLMESVWNMNDSCRFQLRSPESLKSMEKASKTLETKPESKQEPVKTE
MGPPPSPASTCSDASSIASSASMPYKRRRSTPAPREEEKVNEEQWPLREVVFVEDVKNVP
VGKVLKVDGAYVAVKFPGTSTNTTCQNSSGPDADPSSLLQDCRLLRIDELQVVKTGGTPK
VPDCFQRTPKKLCIPEKTEILAVNVDSKGVHAVLKTGSWVRYCVFDLATGKAEQENNFPT
SSVAFLGQDERSVAIFTAGQESPIVLRDGNGTIYPMAKDCMGGIRDPDWLDLPPISSLGM
GVHSLINLPANSTIKKKAAIIIMAVEKQTLMQHILRCDYEACRQYLVNLEQAVVLEQNRQ
MLQTFISHRCDGNRNILHACVSVCFPTSNKETKEEEEAERSERNTFAERLSAVEAIANAI
SVVSSNGPGNRAGSSNSRSLRLREMMRRSLRAAGLGRHEAGASSSDHQDPVSPPIAPPSW
VPDPPSMDPDGDIDFILAPAVGSLTTAATGSGQGPSTSTIPGPSTEPSVVESKDRKANAH
FILKLLCDSAVLQPYLRELLSAKDARGMTPFMSAVSGRAYSAAITILETAQKIAKAEVSA
SEKEEDVFMGMVCPSGTNPDDSPLYVLCCNDTCSFTWTGAEHINQDIFECRTCGLLESLC
CCTECARVCHKGHDCKLKRTSPTAYCDCWEKCKCKTLIAGQKSARLDLLYRLLTATNLVT
LPNSRGEHLLLFLVQTVARQTVEHCQYRPPRIREDRNRKTASPEDSDMPDHDLEPPRFAQ
LALERVLQDWNALRSMIMFGSQENKDPLSASSRIGHLLPEEQVYLNQQSGTIRLDCFTHC
LIVKCTADILLLDTLLGTLVKELQNKYTPGRREEAIAVTMRFLRSVARVFVILSVEMASS
KKKNNFIPQPIGKCKRVFQALLPYAVEELCNVAESLIVPVRMGIARPTAPFTLASTSIDA
MQGSEELFSVEPLPPRPSSDQASSSSQSQSSYIIRNPQQRRISQSQPVRGRDEEQDDIVS
ADVEEVEVVEGVAGEEDHHDEQEEHGEENAEAEGHHDEHDEDGSDMELDLLAAAETESDS
ESNHSNQDNASGRRSVVTAATAGSEAGASSVPAFFSEDDSQSNDSSDSDSSSSQSDDIEQ
ETFMLDEPLERTTNSSHANGAAQAPRSMQWAVRNPQHQRAASTAPSSTSTPAASSAGLIY
IDPSNLRRSGTISTSAAAAAAALEASNASSYLTSASSLARAYSIVIRQISDLMGLIPKYN
HLVYSQIPAAVKLTYQDAVNLQNYVEEKLIPTWNWMVSVMDSTEAQLRYGSALASAGDPG
HPNHPLHASQNSARRERMTAREEASLRTLEGRRRATLLSARQGMMSARGDFLNYALSLMR
SHNDEHSDVLPVLDVCSLKHVAYVFQALIYWIKAMNQQTTLDTPQLERKRTRELLELGID
NEDSEHENDDDTSQSATLNDKDDDSLPAETGQNHPFFRRSDSMTFLGCIPPNPFEVPLAE
AIPLADQPHLLQPNARKEDLFGRPSQGLYSSSAGSGKCIVEVTMDRNCLEVLPTKMSYAA
NLKNVMNMQNRQKKEGEEQSLLAEEADSSKPGPSAPDVAAQLKSSLLAEIGLTESEGPPL
TSFRPQCSFMGMVISHDMLLGRWRLSLELFGRVFMEDVGAEPGSILTELGGFEVKESKFR
REMEKLRNQQSRDLSLEVDRDRDLLIQQTMRQLNNHFGRRCATTPMAVHRVKVTFKDEPG
EGSGVARSFYTAIAQAFLSNEKLPNLDCIQNANKGTHTSLMQRLRNRGERDREREREREM
RRSSGLRAGSRRDRDRDFRRQLSIDTRPFRPASEGNPSDDPDPLPAHRQALGERLYPRVQ
AMQPAFASKITGMLLELSPAQLLLLLASEDSLRARVDEAMELIIAHGRENGADSILDLGL
LDSSEKVQENRKRHGSSRSVVDMDLEDTDDGDDNAPLFYQPGKRGFYTPRPGKNTEARLN
CFRNIGRILGLCLLQNELCPITLNRHVIKVLLGRKVNWHDFAFFDPVMYESLRQLILASQ
SSDADAVFSAMDLAFAIDLCKEEGGGQVELIPNGVNIPVTPQNVYEYVRKYAEHRMLVVA
EQPLHAMRKGLLDVLPKNSLEDLTAEDFRLLVNGCGEVNVQMLISFTSFNDESGENAEKL
LQFKRWFWSIVEKMSMTERQDLVYFWTSSPSLPASEEGFQPMPSITIRPPDDQHLPTANT
CISRLYVPLYSSKQILKQKLLLAIKTKNFGFV
Traceback (most recent call last):
  File "Script2.py", line 16, in <module>
    for seq_record in SeqIO.parse( fasta , "fasta"):
  File "/opt/linux/centos/7.x/x86_64/pkgs/miniconda3/4.3.31/lib/python3.6/site-packages/Bio/SeqIO/FastaIO.py", line 178, in FastaIterator
    with as_handle(handle, "rU") as handle:
  File "/opt/linux/centos/7.x/x86_64/pkgs/miniconda3/4.3.31/lib/python3.6/contextlib.py", line 81, in __enter__
    return next(self.gen)
  File "/opt/linux/centos/7.x/x86_64/pkgs/miniconda3/4.3.31/lib/python3.6/site-packages/Bio/File.py", line 120, in as_handle
    with open(handleish, mode, **kwargs) as fp:
FileNotFoundError: [Errno 2] No such file or directory: "Q80TP3.fasta'"
"""



"""
-------------------------------script three 
import os
from Bio import SeqIO
from Bio.Seq import Seq

UBR5querydict = input("The list of urls to parse:")

seqcounter = 0
multiSeqdict = []
for url in UBR5querydict:
    fasta=os.path.basename(url)
    if not os.path.exists(fasta):
        os.system("curl -O {}".format(url))
    for seq_record in SeqIO.parse( fasta , "fasta"):
        multiSeqdict.append(seq_record)
        seqcounter += 1

filename = input("What to call this multiple sequences file (no space after colon):")

SeqIO.write(multiSeqdict, filename, "fasta")

print("The number of sequences in the multiple sequence file generated: {}".format(seqcounter))

-------------------------------script three run
ehay001@i55:~/project$ python3 Script2.py
The list of urls to parse:{'https://www.uniprot.org/uniprot/O95071.fasta', 'https://www.uniprot.org/uniprot/P51592.fasta', 'https://www.uniprot.org/uniprot/Q80TP3.fasta'}
curl: (3) unmatched brace in URL position 1:
{
 ^
Traceback (most recent call last):
  File "Script2.py", line 16, in <module>
    for seq_record in SeqIO.parse( fasta , "fasta"):
  File "/opt/linux/centos/7.x/x86_64/pkgs/miniconda3/4.3.31/lib/python3.6/site-packages/Bio/SeqIO/FastaIO.py", line 178, in FastaIterator
    with as_handle(handle, "rU") as handle:
  File "/opt/linux/centos/7.x/x86_64/pkgs/miniconda3/4.3.31/lib/python3.6/contextlib.py", line 81, in __enter__
    return next(self.gen)
  File "/opt/linux/centos/7.x/x86_64/pkgs/miniconda3/4.3.31/lib/python3.6/site-packages/Bio/File.py", line 120, in as_handle
    with open(handleish, mode, **kwargs) as fp:
FileNotFoundError: [Errno 2] No such file or directory: '{'
"""