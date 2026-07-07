---
name: dvorfs
category: utility
description: "DVORFS tool for mining endogenous viral elements"
tags: [dvorfs, utility, endogenous-viral-elements, EVE, viral-sequences]
author: oxo-call-community
source_url: "https://github.com/ilevantis/dvorfs"
---

## Concepts

- **Tool Overview**: DVORFS is a tool for mining endogenous viral elements (EVEs) from genomic sequences.
- **Core Function**: Identifies and extracts viral sequences integrated into host genomes.
- **Input/Output**: Input: Genome sequences (FASTA). Output: Identified EVEs, annotations, statistics.
- **Algorithm**: Uses similarity searches and filtering to identify viral-derived sequences.
- **Key Features**: EVE identification, viral sequence classification, integration site analysis, batch processing.
- **Installation**: `conda install -c bioconda dvorfs`

## Pitfalls

- **Reference Database**: Requires comprehensive viral reference database for accurate identification.
- **Sequence Quality**: Poor quality assemblies may miss EVEs or produce false positives.
- **Evolutionary Divergence**: Highly divergent viral sequences may be missed.
- **Host Contamination**: Must distinguish true EVEs from contaminating viral sequences.
- **Parameter Tuning**: Sensitivity parameters may need adjustment for different organisms.

## Examples

### Basic EVE mining
**Args:** `--input genome.fa --output eves.tsv`
**Explanation:** Mines endogenous viral elements from genome sequence.

### With custom database
**Args:** `--input genome.fa --output eves.tsv --viral-db viral_refs.fa`
**Explanation:** Uses custom viral reference database for EVE identification.

### With filtering
**Args:** `--input genome.fa --output eves.tsv --min-length 200 --min-identity 80`
**Explanation:** Filters EVEs by minimum length and identity threshold.

### Batch processing
**Args:** `--input-dir genomes/ --output results/ --batch`
**Explanation:** Processes multiple genome files in batch mode.

### Generate report
**Args:** `--input genome.fa --output eves.tsv --report report.html`
**Explanation:** Generates HTML report with EVE analysis results.