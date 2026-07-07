---
name: soapdenovo-trans
category: transcriptomics
description: SOAPdenovo-Trans - De novo transcriptome assembler for RNA-seq data
tags: [soapdenovo-trans, transcriptomics, assembly, rna-seq, transcriptome]
author: oxo-call-community
source_url: "https://github.com/aquaskyline/SOAPdenovo-Trans"
---

## Concepts

- **Tool Overview**: soapdenovo-trans (v1.04) - A de novo transcriptome assembler
- **Core Function**: Assembles transcriptome from RNA-seq reads without reference
- **Input/Output**: Accepts FASTQ reads; outputs assembled transcripts
- **Algorithm**: Based on SOAPdenovo framework, adapted for transcriptome
- **Installation**: `conda install -c bioconda soapdenovo-trans`
- **Key Features**: De novo assembly, alternative splicing, expression adaptation

## Pitfalls

- **Input Requirements**: Requires properly formatted RNA-seq FASTQ files
- **K-mer Size**: K-mer size affects transcript assembly quality
- **Memory Usage**: Large transcriptomes require significant memory
- **Expression Levels**: Different expression levels affect assembly
- **Alternative Splicing**: Complex splicing patterns may be challenging
- **Coverage**: Requires sufficient read coverage for good assembly

## Examples

### Display help
**Args:** `SOAPdenovo-Trans --help`
**Explanation:** Shows available options and usage information.

### Basic transcriptome assembly
**Args:** `SOAPdenovo-Trans all -s config.txt -K 25 -o transcripts`
**Explanation:** Run complete transcriptome assembly.

### With paired-end reads
**Args:** `SOAPdenovo-Trans all -s config.txt -K 31 -o transcripts`
**Explanation:** Assemble from paired-end RNA-seq reads.

### Set k-mer size
**Args:** `SOAPdenovo-Trans all -s config.txt -K 31 -o transcripts`
**Explanation:** Set k-mer size for assembly.

### With threads
**Args:** `SOAPdenovo-Trans all -s config.txt -K 25 -o transcripts -p 8`
**Explanation:** Use multiple threads for assembly.

### Contig assembly only
**Args:** `SOAPdenovo-Trans contig -g transcripts`
**Explanation:** Assemble transcript contigs only.

### Output statistics
**Args:** `SOAPdenovo-Trans all -s config.txt -K 25 -o transcripts --stats`
**Explanation:** Output assembly statistics.

### Generate report
**Args:** `SOAPdenovo-Trans all -s config.txt -K 25 -o transcripts --report`
**Explanation:** Generate assembly report.