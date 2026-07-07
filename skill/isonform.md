---
name: isonform
category: expression
description: De novo construction of isoforms from long-read data.
tags: [isonform, expression, long reads, isoforms, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/aljpetri/isONform"
---

## Concepts

- **De Novo Isoform Construction**: Builds full-length isoform sequences from long-read data without reference genome.
- **Read Alignment**: Aligns long reads to reconstruct complete transcript sequences.
- **Consensus Generation**: Generates consensus sequences representing each isoform.
- **Error Correction**: Incorporates error correction during isoform construction.
- **Isoform Diversity**: Preserves alternative splicing variants and transcript diversity.
- **Output Formats**: Generates FASTA, GTF, and other standard bioinformatics formats.

## Pitfalls

- **Read Quality**: Poor quality reads can introduce errors in isoform sequences.
- **Isoform Complexity**: Highly similar isoforms may be merged incorrectly.
- **Memory Usage**: Processing large datasets requires significant memory.
- **Computational Time**: Constructing isoforms from millions of reads is time-consuming.
- **Coverage Requirements**: Requires sufficient coverage to reconstruct complete isoforms.
- **Chimeric Reads**: Chimeric sequences can create false isoforms.

## Examples

### Basic isoform construction
**Args:** `isonform --reads reads.fastq --output isoforms.fasta`
**Explanation:** Constructs full-length isoforms from long-read transcriptome data.

### With clustering
**Args:** `isonform --reads reads.fastq --cluster --output isoforms.fasta`
**Explanation:** Uses clustering to group similar reads before isoform construction.

### Error correction mode
**Args:** `isonform --reads reads.fastq --correct --output isoforms.fasta`
**Explanation:** Applies error correction during isoform construction.

### Generate GTF output
**Args:** `isonform --reads reads.fastq --gtf --output isoforms/`
**Explanation:** Generates GTF annotation file alongside FASTA sequences.

### Quality filtering
**Args:** `isonform --reads reads.fastq --min-quality 10 --output isoforms.fasta`
**Explanation:** Filters low-quality reads before isoform construction.

### Batch processing
**Args:** `isonform --batch samples.txt --output-dir results/`
**Explanation:** Processes multiple samples listed in a batch file.