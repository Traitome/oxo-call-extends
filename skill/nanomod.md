---
name: nanomod
category: epigenomics
description: NanoMod - Nanopore signal analysis for DNA/RNA modification detection
tags: [nanomod, epigenomics, nanopore, modification, signal, dna-modification]
author: oxo-call-community
source_url: "https://github.com/WGLab/NanoMod"
---

## Concepts

- **Tool Overview**: NanoMod v0.2.2 is a computational method for detecting DNA and RNA modifications from Oxford Nanopore raw signal data. It analyzes current changes caused by modified nucleotides.
- **Core Function**: Identifies modified bases (m6A, m5C, 5mC, etc.) by comparing raw signal characteristics between modified and unmodified bases.
- **Algorithm**: Uses machine learning models trained on known modification patterns to classify bases as modified or unmodified based on signal features.
- **Input Format**: Requires FAST5 files containing raw signal data and aligned BAM files for genomic coordinates.
- **Output**: Produces VCF or BED files with modification site coordinates, confidence scores, and modification types.
- **Use Case**: Epigenomics research, detecting DNA methylation patterns, identifying RNA modifications, and studying epigenetic regulation.

## Pitfalls

- **FAST5 Format**: Requires proper FAST5 file format with raw signal data. Basecalled-only files won't work.
- **Training Data**: Model performance depends on training data quality. Different sequencing kits may require retraining.
- **Coverage**: Requires sufficient read coverage at potential modification sites. Low coverage reduces detection power.
- **False Positives**: Stringent filtering is recommended to reduce false positive calls.
- **Modification Types**: May not detect all modification types. Check supported modifications before use.
- **Signal Quality**: Poor signal quality affects detection accuracy. Filter low-quality reads first.

## Examples

### Basic modification detection
**Args:** `-f fast5_dir -b aligned.bam -r reference.fasta -o output_dir`
**Explanation:** Detects modifications from Nanopore signal data and alignments.

### Specify modification type
**Args:** `-f fast5_dir -b aligned.bam -r ref.fa -o output/ -m m6A`
**Explanation:** Focuses on detecting m6A modifications specifically.

### Adjust confidence threshold
**Args:** `-f fast5_dir -b aligned.bam -r ref.fa -o output/ -c 0.9`
**Explanation:** Sets confidence threshold to 90% for calling modifications.

### Use GPU acceleration
**Args:** `-f fast5_dir -b aligned.bam -r ref.fa -o output/ --gpu`
**Explanation:** Uses GPU for accelerated signal processing.

### Display help
**Args:** `nanomod --help`
**Explanation:** Shows all available options for modification detection.
