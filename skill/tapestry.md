---
name: tapestry
category: assembly
description: Validates and edits small eukaryotic genome assemblies.
tags: [tapestry, assembly, validation, eukaryotic]
author: oxo-call-community
source_url: "https://github.com/johnomics/tapestry"
---

## Concepts

- **Tool Overview**: tapestry (v1.0.1) validates and edits genome assemblies.
- **Core Function**: Assembly validation and curation.
- **Algorithm**: Uses read mapping and variant calling for validation.
- **Input/Output**: Input: Assembly FASTA; Output: Curated assembly.
- **Applications**: Genome assembly curation, quality improvement.
- **Installation**: `conda install -c bioconda tapestry` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large assemblies require significant memory.
- **Read Coverage**: Requires sufficient sequencing coverage.
- **Computational Time**: Processing large genomes can be slow.
- **Assembly Quality**: Poor input assemblies affect results.
- **False Positives**: May incorrectly flag regions.
- **Performance**: Slow on large datasets.

## Examples

### Display help
**Args:** `tapestry --help`
**Explanation:** Shows available options and usage information.

### Basic validation
**Args:** `tapestry -i assembly.fasta -r reads.fastq -o curated.fasta`
**Explanation:** Validate and curate assembly.

### With alignment
**Args:** `tapestry -i assembly.fasta -b alignments.bam -o curated.fasta`
**Explanation:** Use existing BAM alignment.

### Verbose mode
**Args:** `tapestry -i assembly.fasta -r reads.fastq -o curated.fasta -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tapestry -i assembly.fasta -r reads.fastq -o curated.fasta --stats`
**Explanation:** Generate statistics about assembly.

### Batch processing
**Args:** `for f in assemblies/*.fasta; do tapestry -i $f -r reads.fastq -o curated/${f%.fasta}_curated.fasta; done`
**Explanation:** Process multiple assemblies.

### Include polishing
**Args:** `tapestry -i assembly.fasta -r reads.fastq -o curated.fasta --polish`
**Explanation:** Include assembly polishing step.

### Filter by quality
**Args:** `tapestry -i assembly.fasta -r reads.fastq -o curated.fasta -q 20`
**Explanation:** Minimum quality threshold.

### Generate report
**Args:** `tapestry -i assembly.fasta -r reads.fastq -o curated.fasta --report`
**Explanation:** Generate comprehensive assembly report.
