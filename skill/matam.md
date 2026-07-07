---
name: matam
category: assembly
description: MATAM is a software for fast and accurate targeted assembly of short reads, particularly for 16S rRNA sequences.
tags: [matam, targeted-assembly, 16S, rRNA]
author: oxo-call-community
source_url: "https://github.com/bonsai-team/matam"
---

## Concepts

- **Tool Overview**: MATAM is a targeted assembly tool optimized for amplicon sequencing data like 16S rRNA.
- **Core Function**: Assembles short reads into target-specific sequences efficiently.
- **Reference-guided Assembly**: Uses reference databases to guide assembly of specific regions.
- **16S rRNA Focus**: Specifically designed for assembling 16S ribosomal RNA sequences.
- **Input/Output**: Accepts FASTQ reads, produces assembled contigs and OTU tables.
- **Installation**: `conda install -c bioconda matam`

## Pitfalls

- **Reference Database**: Requires appropriate reference database for target sequences.
- **Primer Design**: Primer sequences must be compatible with target amplification.
- **Sequence Quality**: Low-quality reads affect assembly accuracy.
- **Memory Requirements**: Large datasets may require significant memory.
- **Computation Time**: Can be slow for very large datasets.
- **Output Interpretation**: OTU clustering requires downstream analysis.

## Examples

### Assemble 16S reads
**Args:** `matam_assemble.py -i reads.fastq -o output/`
**Explanation:** Assembles 16S rRNA sequences from input reads.

### With reference database
**Args:** `matam_assemble.py -i reads.fastq -r ref_db.fasta -o output/`
**Explanation:** Uses custom reference database for guided assembly.

### Paired-end reads
**Args:** `matam_assemble.py -i reads_1.fastq -i2 reads_2.fastq -o output/`
**Explanation:** Processes paired-end sequencing data.

### Custom k-mer size
**Args:** `matam_assemble.py -i reads.fastq -k 31 -o output/`
**Explanation:** Sets k-mer size to 31 for assembly.

### Quality filtering
**Args:** `matam_assemble.py -i reads.fastq -q 20 -o output/`
**Explanation:** Filters reads with quality score below 20.

### Help documentation
**Args:** `matam_assemble.py --help`
**Explanation:** Displays available commands and options.
