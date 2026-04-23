---
name: cat
category: metagenomics
description: Taxonomic classification of contigs and metagenome-assembled genomes (MAGs)
tags: [cat, bat, taxonomy, classification, metagenomics, mags]
author: oxo-call-community
source_url: "https://github.com/MGXlab/CAT_pack"
---

## Concepts

- **Tool Overview**: CAT/BAT classifies contigs and MAGs taxonomically using protein homology.
- **Core Function**: Assigns taxonomy to assembled contigs (CAT) or bins (BAT) from metagenomes.
- **Algorithm**: Uses DIAMOND BLASTX against NCBI nr database with lowest common ancestor (LCA) assignment.
- **Input**: Contigs/MAGs in FASTA format and pre-built database.
- **Output**: Taxonomic assignments with confidence scores.
- **Database**: Requires CAT database with NCBI taxonomy and protein references.
- **Installation**: Install via bioconda: `conda install -c bioconda cat`

## Pitfalls

- **Database Required**: Must download CAT database (~100GB) before use.
- **DIAMOND Required**: Requires DIAMOND for protein search.
- **Memory Usage**: Database loading requires significant memory.
- **Fragmented Genomes**: Very short contigs may have unreliable classification.

## Examples

### Prepare database
**Args:** `CAT prepare --db_fasta nr.fa --tax_nodes nodes.dmp --tax_names names.dmp --db CAT_db`
**Explanation:** Prepares CAT database from NCBI taxonomy and protein files.

### Classify contigs
**Args:** `CAT contigs -c contigs.fa -d CAT_db -t taxonomy/ -o classification.tsv`
**Explanation:** Classifies metagenomic contigs using CAT database.

### Classify MAGs with BAT
**Args:** `BAT bins -b bins_folder/ -d CAT_db -t taxonomy/ -o bin_classification.tsv`
**Explanation:** Classifies metagenome-assembled genomes using BAT.

### Add names to classification
**Args:** `CAT add_names -i classification.tsv -o named_classification.tsv -t taxonomy/ --only_official`
**Explanation:** Converts taxonomic IDs to scientific names in classification output.

### Single MAG classification
**Args:** `BAT single_bin -b bin.fa -d CAT_db -t taxonomy/ -o single_classification.tsv`
**Explanation:** Classifies a single MAG file.

### Set fraction for LCA
**Args:** `CAT contigs -c contigs.fa -d CAT_db -t taxonomy/ -f 0.3 -o classification.tsv`
**Explanation:** Uses 30% fraction for LCA assignment (more sensitive).
