---
name: oarfish
category: expression
description: oarfish performs fast and accurate transcript quantification from long-read RNA-seq data.
tags: [oarfish, expression, rna-seq, long-reads]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/oarfish"
---

## Concepts

- **Tool Overview**: oarfish quantifies transcript expression from long-read RNA-seq data.
- **Core Function**: Estimates transcript abundances from sequencing reads.
- **Algorithm**: Uses alignment-based approach for transcript quantification.
- **Input Format**: Accepts FASTQ reads and transcriptome references.
- **Output**: Produces expression levels in TPM/RPKM/FPKM.
- **Use Case**: Gene expression analysis, transcriptomics, and RNA-seq studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Long Read Quality**: Results depend on read quality.
- **Memory Usage**: Large datasets require memory.
- **Transcriptome Index**: Requires building index first.
- **Computational Cost**: Quantification can be intensive.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `oarfish --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `oarfish index -t transcriptome.fasta -o index/`
**Explanation:** Builds index for transcriptome.

### Quantify expression
**Args:** `oarfish quantify -i index/ -r reads.fastq -o expression.txt`
**Explanation:** Quantifies transcript expression.

### Paired-end reads
**Args:** `oarfish quantify -i index/ -r reads_1.fastq -r2 reads_2.fastq -o expression.txt`
**Explanation:** Processes paired-end reads.

### Output format
**Args:** `oarfish quantify -i index/ -r reads.fastq -o expression.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Threads
**Args:** `oarfish quantify -i index/ -r reads.fastq -t 8 -o expression.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `oarfish quantify -i index/ -r reads.fastq -v -o expression.txt`
**Explanation:** Runs with verbose output.