---
name: nanoblaster
category: alignment
description: NanoBLASTer - BLAST-like alignment tool for Oxford Nanopore long reads
tags: [nanoblaster, alignment, nanopore, blast, long-reads, local-alignment]
author: oxo-call-community
source_url: "https://github.com/ruhulsbu/NanoBLASTer"
---

## Concepts

- **Tool Overview**: NanoBLASTer v0.16 is a BLAST-like local alignment tool specifically optimized for noisy Oxford Nanopore long sequencing reads. It provides rapid similarity searches for long, error-prone sequences.
- **Core Function**: Performs local alignment searches between Nanopore reads and reference sequences. Designed to handle the higher error rates of Nanopore data compared to Illumina sequencing.
- **Algorithm**: Implements a modified BLAST algorithm with adaptive scoring matrices that account for Nanopore-specific error patterns (higher indel rates, strand-specific errors).
- **Input Format**: Accepts query reads in FASTQ/FASTA format (gzipped or uncompressed) and reference sequences in FASTA format. Optimized for long reads (1kbp and longer).
- **Output**: Produces tabular alignments similar to BLAST output format, including alignment statistics, E-values, and bit scores. Supports multiple output formats.
- **Use Case**: Rapid species identification from Nanopore reads, finding homologous sequences in databases, quality control for Nanopore sequencing runs, and targeted sequence detection.

## Pitfalls

- **Error Rate Handling**: While optimized for Nanopore errors, very high error rates (>15%) may still produce spurious matches. Filter low-quality reads first.
- **Memory Usage**: Large reference databases require significant memory. Consider splitting large references or using pre-filtering.
- **Query Length**: Designed for long reads (>1kbp). Short reads may produce poor results compared to traditional BLAST.
- **Sensitivity vs Speed**: Higher sensitivity settings increase runtime. Balance based on your needs.
- **Database Format**: References must be formatted correctly. Large databases may require indexing for better performance.
- **Strand Bias**: Nanopore reads may have strand-specific error patterns. Consider searching both strands.

## Examples

### Basic alignment search
**Args:** `-q reads.fastq -r reference.fasta -o results.tsv`
**Explanation:** Standard NanoBLASTer workflow. Searches Nanopore reads against reference database.

### Increase sensitivity
**Args:** `-q long_reads.fastq -r genome.fa -o sensitive_results.tsv -s high`
**Explanation:** Uses high sensitivity mode for finding more distant homologs.

### Output in BLAST format
**Args:** `-q nanopore.fastq -r ref.fasta -o blast_output.txt -f blast`
**Explanation:** Outputs results in traditional BLAST format for compatibility with downstream tools.

### Limit number of hits
**Args:** `-q reads.fastq -r database.fasta -o top_hits.tsv -max_hits 5`
**Explanation:** Returns only top 5 hits per query sequence to reduce output size.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.
