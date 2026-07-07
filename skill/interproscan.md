---
name: interproscan
category: annotation
description: InterProScan integrates predictive information about protein function from multiple databases including Pfam, PANTHER, SMART, and PROSITE
tags: [interproscan, annotation, protein, domain]
author: oxo-call-community
source_url: "https://github.com/ebi-pf-team/interproscan"
---

## Concepts

- **Tool Overview**: InterProScan (v5.59_91.0) is a powerful protein function annotation tool that integrates predictive information from 13 different databases
- **Core Function**: Scans protein sequences against multiple signature databases to identify domains, families, and functional sites
- **Integrated Databases**: CDD, COILS, Gene3D, HAMAP, MobiDBLite, PANTHER, Pfam, PIRSF, PRINTS, ProDom, PROSITE, SFLD, SMART, SUPERFAMILY, TIGRFAM
- **Output Formats**: Supports TSV, XML, GFF3 output formats
- **Installation**: `conda install -c bioconda interproscan`

## Pitfalls

- **Memory Requirements**: InterProScan requires significant memory for large sequence sets
- **Database Download**: Some databases like PANTHER require separate installation
- **Internet Dependency**: The pre-calculated match lookup service requires network access
- **Input Format**: Only FASTA format is supported for protein sequences
- **Long Runtime**: Running against all databases can be time-consuming

## Examples

### Basic protein annotation
**Args:** `interproscan.sh -i proteins.fasta -o annotations.tsv -f tsv`
**Explanation:** Performs functional annotation of protein sequences and outputs results in TSV format.

### Include GO terms
**Args:** `interproscan.sh -i proteins.fasta -o annotations_with_go.tsv -f tsv --goterms`
**Explanation:** Includes Gene Ontology terms in the annotation output.

### Run with specific databases
**Args:** `interproscan.sh -appl Pfam,SMART,PANTHER -i proteins.fasta -o specific_db_results.tsv -f tsv`
**Explanation:** Runs annotation using only specified databases (Pfam, SMART, PANTHER).

### Enable lookup service
**Args:** `interproscan.sh -i proteins.fasta -o results.tsv -f tsv -iprlookup -pa`
**Explanation:** Enables InterPro lookup and PANTHER classification for more comprehensive annotations.

### Specify output format
**Args:** `interproscan.sh -i proteins.fasta -o results.gff3 -f gff3`
**Explanation:** Outputs results in GFF3 format for genome browser visualization.

### Run with temporary directory
**Args:** `interproscan.sh -i proteins.fasta -o annotations.tsv -f tsv -T /tmp/interproscan_temp`
**Explanation:** Uses specified temporary directory for intermediate files.