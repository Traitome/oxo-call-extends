---
name: ac-diamond
category: alignment
description: AC-DIAMOND is a DNA-protein alignment tool.
tags: [ac-diamond, alignment, dna-protein, blast, translated-search]
author: oxo-call-community
source_url: "https://github.com/Maihj/AC-DIAMOND"
---

## Concepts

- **Tool Overview**: A DNA-protein alignment tool for translated sequence search, similar to BLASTX but optimized for speed. Version 1.0.
- **Core Function**: Aligns DNA sequences against protein databases using translated search, identifying homologous proteins.
- **Input/Output**: Input is DNA sequences (FASTA/FASTQ) and protein database; output is alignment results in various formats (TAB, BLAST, SAM).
- **Installation**: Install via bioconda: `conda install -c bioconda ac-diamond`
- **Platform Support**: Linux (x86_64)
- **Speed Optimization**: Designed for high-speed DNA-protein alignment, faster than traditional BLASTX.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Database Format**: Requires properly formatted DIAMOND database. Use `diamond makedb` to create databases.
- **Frame Selection**: DNA sequences are translated in 6 frames. Consider strand specificity for RNA-seq data.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and parameters.

### Basic DNA-protein alignment
**Args:** `blastx -q dna_reads.fa -d protein_db.dmnd -o alignments.m8`
**Explanation:** Aligns DNA sequences against a protein database using translated search (blastx mode). Output is in BLAST tabular format.

### Run with e-value threshold
**Args:** `blastx -q reads.fa -d proteins.dmnd -e 1e-5 -o results.m8`
**Explanation:** Filters alignments by e-value threshold of 1e-5. More stringent threshold reduces false positives.

### Output in SAM format
**Args:** `blastx -q dna.fa -d proteins.dmnd --outfmt 101 -o alignments.sam`
**Explanation:** Outputs alignments in SAM format for compatibility with downstream tools.
