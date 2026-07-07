---
name: hymet2
category: metagenomics
description: HYMET2 - Hybrid Metagenomic Tool for taxonomic identification
tags: [hymet2, metagenomics, taxonomic classification]
author: oxo-call-community
source_url: "https://github.com/inesbmartins02/HYMET2"
---

## Concepts

- **Tool Overview**: HYMET2 is a taxonomic identification tool for metagenomic sequence analysis using a hybrid approach.
- **Dual-phase Strategy**: Combines rapid k-mer screening with precise alignment for accurate taxonomic classification.
- **Mash Integration**: Uses Mash Screen for rapid candidate reference genome identification.
- **Dynamic Alignment**: Employs Mashmap2 for large genomes and Minimap2 for smaller sequences.
- **Weighted LCA**: Uses weighted lowest common ancestor algorithm for taxonomic assignments with confidence scoring.
- **Installation**: `conda install -c bioconda hymet2`

## Pitfalls

- **Database Requirements**: Requires reference database (e.g., GTDB) for classification.
- **Memory Usage**: Processing large metagenomic datasets may require significant memory.
- **Input Quality**: Low-quality reads should be preprocessed before classification.
- **Reference Genome Selection**: Choice of reference database affects classification accuracy.
- **Taxonomic Resolution**: Species-level identification may be limited by database coverage.
- **Computation Time**: Full classification can be time-consuming for complex communities.

## Examples

### Basic taxonomic classification
**Args:** `hymet2 classify -i metagenome.fastq -o taxonomy.tsv`
**Explanation:** Classifies metagenomic reads and outputs taxonomic assignments.

### Custom reference database
**Args:** `hymet2 classify -i reads.fastq -db custom_db/ -o results.tsv`
**Explanation:** Uses a custom reference database for classification.

### Preprocessing with quality control
**Args:** `hymet2 pipeline -i raw_reads.fastq -o processed/ --qc`
**Explanation:** Runs complete pipeline with quality control preprocessing.

### Host DNA depletion
**Args:** `hymet2 classify -i reads.fastq -host host_reference.fasta -o results.tsv`
**Explanation:** Removes host sequences before taxonomic classification.

### Generate summary report
**Args:** `hymet2 report -i taxonomy.tsv -o summary.html`
**Explanation:** Generates an HTML summary report of taxonomic profiles.