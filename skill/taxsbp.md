---
name: taxsbp
category: metagenomics
description: TaxSBP - taxonomic structured bin packing for metagenomic bin assignment using NCBI taxonomy.
tags: [taxsbp, metagenomics, binning, taxonomy, ncbi, structured-bin-packing]
author: oxo-call-community
source_url: "https://github.com/pirovc/taxsbp"
---

## Concepts

- **Tool Overview**: taxsbp (v1.1.1) - TaxSBP (Taxonomic Structured Bin Packing) implements approximation algorithms for the hierarchically structured bin packing problem adapted for the NCBI Taxonomy database.
- **Core Function**: Assigns metagenomic sequencing reads or contigs to taxonomic bins using a structured bin packing approach that respects taxonomic hierarchy.
- **Algorithm**: Uses bin packing optimization to efficiently assign sequences to taxonomic bins while minimizing misclassification.
- **Installation**: `conda install -c bioconda taxsbp` or `pip install taxsbp`
- **Dependencies**: Requires pylca and binpacking Python packages for taxonomy lowest common ancestor calculations and bin packing algorithms.
- **Input**: Takes FASTA/FASTQ sequence files and a pre-built database index (such as from Kraken or other classifiers).

## Pitfalls

- **Database Requirement**: taxsbp requires a database with taxonomy information - it does not build its own classifier database.
- **Taxonomy Consistency**: Uses NCBI taxonomy IDs - ensure consistency with other taxonomy-based tools in your pipeline.
- **Memory Usage**: Large metagenomic datasets can require significant memory for bin packing computation.
- **Bin Assignment**: The structured bin packing approach may assign sequences to higher taxonomic ranks when lower rank assignment is uncertain.
- **Version Compatibility**: Python 3.5+ required. Some dependencies may have version conflicts with older Python versions.
- **Output Format**: Outputs assignments with taxids - subsequent tools may need taxid-to-name conversion.

## Examples

### Display help
**Args:** `taxsbp -h`
**Explanation:** Show all available command-line options and usage information.

### Basic bin assignment
**Args:** `taxsbp -i sequences.fasta -d kraken_db -o assignments.txt`
**Explanation:** Assign sequences in FASTA file to taxonomic bins using Kraken database. Output contains sequence ID and assigned taxid.

### With taxonomy tree
**Args:** `taxsbp -i sequences.fasta -d kraken_db -o assignments.txt -t taxonomy.dmp`
**Explanation:** Include NCBI taxonomy tree file for structured bin packing respecting taxonomic hierarchy.

### Filter by rank
**Args:** `taxsbp -i sequences.fasta -d kraken_db -o assignments.txt -r species`
**Explanation:** Only assign sequences to taxonomic bins at the species rank or higher confidence.

### Multiple sequence files
**Args:** `taxsbp -i sample1.fasta sample2.fasta -d kraken_db -o assignments/`
**Explanation:** Process multiple input files in a single run, outputting to specified directory.

### Verbose output
**Args:** `taxsbp -i sequences.fasta -d kraken_db -o assignments.txt -v`
**Explanation:** Enable verbose logging to see processing progress, read counts, and assignment statistics.

### Threshold adjustment
**Args:** `taxsbp -i sequences.fasta -d kraken_db -o assignments.txt -t 0.5`
**Explanation:** Adjust the confidence threshold for bin assignment. Higher values require more confidence for taxonomic assignment.
