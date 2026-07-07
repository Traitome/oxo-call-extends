---
name: batch_brb
category: utility
description: batch_brb - Automated best reciprocal BLAST and phylogenetic analysis pipeline
tags: [batch_brb, utility, BLAST, phylogenetics, FastTree]
author: oxo-call-community
source_url: "https://github.com/erin-r-butterfield/batch_brb"
---

## Concepts

- **Tool Overview**: batch_brb (v1.1.1) automates best reciprocal BLAST (BRB) searches and phylogenetic analysis using FastTree, enabling batch processing of sequence datasets.
- **Core Function**: Automates reciprocal BLAST searches and generates phylogenetic trees from sequence data.
- **Best Reciprocal BLAST**: Identifies orthologous sequences through reciprocal BLAST searches.
- **Phylogenetic Analysis**: Constructs phylogenetic trees using FastTree for evolutionary analysis.
- **Batch Processing**: Processes multiple sequences in batch mode for large-scale analysis.
- **Input/Output**: Accepts FASTA sequence files; outputs BLAST results and phylogenetic trees.
- **Installation**: `conda install -c bioconda batch_brb`.

## Pitfalls

- **BLAST Database**: Requires pre-built BLAST database for searches.
- **Computational Time**: BLAST searches and tree construction can be time-consuming for large datasets.
- **Memory Usage**: Large sequence datasets may require substantial memory.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic BRB analysis
**Args:** `batch_brb -i sequences.fasta -d blast_db -o results/`
**Explanation:** Performs best reciprocal BLAST and phylogenetic analysis.

### Specify output format
**Args:** `batch_brb -i sequences.fasta -d blast_db -o results/ --format newick`
**Explanation:** Outputs phylogenetic tree in Newick format.

### Number of threads
**Args:** `batch_brb -i sequences.fasta -d blast_db -o results/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Custom FastTree options
**Args:** `batch_brb -i sequences.fasta -d blast_db -o results/ --fasttree-opts "-nt"`
**Explanation:** Passes custom options to FastTree for nucleotide alignment.

### Filter by e-value
**Args:** `batch_brb -i sequences.fasta -d blast_db -o results/ -e 1e-10`
**Explanation:** Filters BLAST results by e-value threshold.

### Batch mode with multiple files
**Args:** `batch_brb -i seq_list.txt -d blast_db -o results/`
**Explanation:** Processes multiple sequence files listed in text file.

### Display help
**Args:** `batch_brb --help`
**Explanation:** Shows all available command-line options and usage information.