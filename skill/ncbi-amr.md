---
name: ncbi-amr
category: annotation
description: AMRFinder identifies acquired antimicrobial resistance genes in protein or nucleotide sequences.
tags: [ncbi-amr, annotation, antimicrobial-resistance, amr, bacteria]
author: oxo-call-community
source_url: "https://github.com/ncbi/amr/wiki"
---

## Concepts

- **Tool Overview**: AMRFinder v1.04 is NCBI's tool for identifying acquired antimicrobial resistance genes in bacterial sequences.
- **Core Function**: Detects acquired AMR genes and point mutations conferring resistance in protein or nucleotide sequences.
- **Algorithm**: Compares input sequences against NCBI's curated AMR reference database using sequence alignment.
- **Input Format**: Accepts protein or nucleotide FASTA files, or GenBank/EMBL format files.
- **Output**: Produces tab-separated reports with AMR gene matches, resistance phenotypes, and confidence scores.
- **Use Case**: Antimicrobial resistance surveillance, clinical microbiology, and bacterial genome analysis.

## Pitfalls

- **Deprecated Tool**: Superseded by AMRFinderPlus; consider using ncbi-amrfinderplus instead.
- **Database Updates**: Requires regular database updates for accurate results.
- **False Positives**: May report false positives for highly conserved genes.
- **Input Quality**: Results depend on sequence quality and completeness.
- **Version Differences**: Options may vary between versions.
- **Species Specificity**: Some resistance genes are species-specific.

## Examples

### Display help
**Args:** `amrfinder --help`
**Explanation:** Shows available options and usage instructions.

### Basic AMR detection
**Args:** `amrfinder -i input.fasta -o amr_results.tsv`
**Explanation:** Identifies AMR genes in input sequences.

### Protein sequence input
**Args:** `amrfinder --protein input.faa -o results.tsv`
**Explanation:** Analyzes protein sequences for AMR genes.

### Nucleotide sequence input
**Args:** `amrfinder --nucleotide input.fna -o results.tsv`
**Explanation:** Analyzes nucleotide sequences for AMR genes.

### Update database
**Args:** `amrfinder --update`
**Explanation:** Updates the AMR reference database.

### Output JSON format
**Args:** `amrfinder -i input.fasta --json -o results.json`
**Explanation:** Outputs results in JSON format.