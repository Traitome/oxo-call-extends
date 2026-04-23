---
name: agrvate
category: annotation
description: Rapid identification of Staphylococcus aureus agr locus type and agr operon variants
tags: [staphylococcus, agr, typing, variant, pathogen]
author: oxo-call-community
source_url: "https://github.com/VishnuRaghuram94/AgrVATE"
---

## Concepts

- **Tool Overview**: AgrVATE identifies and analyzes the accessory gene regulator (agr) locus in S. aureus, classifying agr groups and detecting operon variants.
- **Core Function**: Assigns agr specificity group using kmer search, then extracts and analyzes the agrBDCAI operon for variants and frameshift mutations.
- **Input/Output**: Input: S. aureus genome assembly (FASTA). Output: agr group assignment, variant calls, operon sequence.
- **Workflow**: kmer-based group assignment → in-silico PCR extraction → variant calling → frameshift detection.
- **Installation**: Install via bioconda: `conda install -c bioconda agrvate`

## Pitfalls

- **S. aureus Only**: Designed specifically for Staphylococcus aureus - other species not supported.
- **Assembly Quality**: Requires reasonably complete genome assembly - fragmented assemblies may miss agr locus.
- **Novel Groups**: May not correctly assign novel or divergent agr groups not in the database.
- **Primer Binding**: In-silico PCR requires conserved primer binding sites - mutations may prevent extraction.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options for AgrVATE analysis.

### Basic agr typing
**Args:** `agrvate -i assembly.fasta -o results/`
**Explanation:** Identifies agr group and analyzes operon variants from genome assembly.

### Specify output prefix
**Args:** `agrvate -i assembly.fasta -o results/ --prefix sample1`
**Explanation:** Uses custom prefix for output files.

### Skip variant calling
**Args:** `agrvate -i assembly.fasta -o results/ --skip-variants`
**Explanation:** Only performs agr group assignment without detailed variant analysis.

### Custom kmer database
**Args:** `agrvate -i assembly.fasta -o results/ --kmer-db custom_db/`
**Explanation:** Uses custom kmer database for agr group assignment.

### Batch process assemblies
**Args:** `agrvate -i assembly1.fasta -o results/s1/ && agrvate -i assembly2.fasta -o results/s2/`
**Explanation:** Processes multiple S. aureus assemblies sequentially.

### Output agr operon sequence
**Args:** `agrvate -i assembly.fasta -o results/ --extract-operon`
**Explanation:** Extracts and saves the agr operon nucleotide sequence.
