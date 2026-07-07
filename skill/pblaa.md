---
name: pblaa
category: qc
description: pbLAA deconvolutes mixtures of alleles and loci into phased consensus sequences.
tags: [pblaa, qc, pacbio, allele, phasing]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbLAA deconvolutes allele mixtures.
- **Core Function**: Separates alleles into phased sequences.
- **Algorithm**: Uses clustering and phasing algorithms.
- **Input Format**: Accepts PacBio sequencing reads.
- **Output**: Produces phased consensus sequences.
- **Use Case**: Allele separation, locus analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Coverage**: Requires sufficient coverage for separation.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `laa --help`
**Explanation:** Shows available options and usage instructions.

### Deconvolute alleles
**Args:** `laa -i reads.bam -o consensus.fasta`
**Explanation:** Deconvolutes alleles into consensus.

### With clustering
**Args:** `laa -i reads.bam -c -o consensus.fasta`
**Explanation:** Uses clustering for allele separation.

### Verbose mode
**Args:** `laa -v -i reads.bam -o consensus.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `laa -t 8 -i reads.bam -o consensus.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `laa -i reads.bam -o consensus.fastq --fastq`
**Explanation:** Outputs in FASTQ format.

### Generate report
**Args:** `laa -i reads.bam -o consensus.fasta --report report.html`
**Explanation:** Generates HTML report.