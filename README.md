# format_ST2_SCZ

----------------------
Synopsis
----------------------
Format and weight a raw genome-wide association table.

A table of 128 genome-wide significant associations for schizophrenia was saved from the study (https://www.nature.com/articles/nature13595#108-independent-associated-loci) - supplimentary table 2: (https://media.nature.com/original/nature-assets/nature/journal/v511/n7510/extref/nature13595-s1.pdf).

Coordinates are given as ranges for whole SNP LD sites. I wanted to save a row per LD site nucleotide. I also wanted to weight each LD site according to its association p-vlaue.

----------------------
Required input
----------------------
Reads file 

>SWGPGC_ST2.txt

= Supplimentary Table 2, provided in study (https://www.nature.com/articles/ng.686), saved from (https://media.nature.com/original/nature-assets/nature/journal/v511/n7510/extref/nature13595-s1.pdf).

----------------------
Running the script
----------------------
The script is written in Python 3.6

Run like:

>format_ST2_SCZ.py

----------------------
Output
----------------------

Formatted file, saved as

>SWGPGC_ST2_formatted.tsv

A row is present for each nucleotide position within a SNP's LD site. SNP LD sites are each given a score weighted by their assotiation p-value (scores of all SNP LD sites summed equal 1).

The formatted file headers are as follows:

>rank | index_SNP | A12 | chr | pos | pval | pval_score | pval_weight

----------------------
Dependencies
----------------------

None.

----------------------
Work in progress
----------------------

None.

----------------------
Further development
----------------------

Currently written for a specific file path, rather than provoiding the option to specify a file path.
