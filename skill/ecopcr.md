---
name: ecopcr
category: qc
description: "ecoPCR is an electronic PCR software that helps you estimate Barcode primers quality."
tags: [ecopcr, qc, primer-design, metabarcoding, PCR]
author: oxo-call-community
source_url: "https://git.metabarcoding.org/obitools/ecopcr/wikis/home"
---

## Concepts

- **Tool Overview**: ecoPCR is a bioinformatics tool for in silico PCR primer testing and validation, primarily used in metabarcoding studies.
- **Core Function**: Simulates PCR amplification using primer sequences against reference databases to evaluate primer specificity and coverage.
- **Input/Output**: Input: Primer sequences, reference sequence database (FASTA). Output: Amplification results, primer quality metrics.
- **Algorithm**: Performs sequence alignment of primers against reference sequences, simulating PCR conditions.
- **Key Features**: Primer specificity testing, in silico PCR simulation, barcode primer evaluation, coverage estimation, mismatch tolerance.
- **Installation**: `conda install -c bioconda ecopcr`

## Pitfalls

- **Database Format**: Requires specific database format (must be indexed).
- **Primer Design**: Poorly designed primers may give misleading results.
- **Mismatch Tolerance**: Default parameters may need adjustment for specific applications.
- **Computation Time**: Large databases can be slow to process.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic electronic PCR
**Args:** `ecopcr -d ref_db.fasta -p forward_primer.fa -P reverse_primer.fa -o results.txt`
**Explanation:** Performs in silico PCR using forward and reverse primers.

### With mismatch tolerance
**Args:** `ecopcr -d ref_db.fasta -p forward.fa -P reverse.fa -m 2 -o results.txt`
**Explanation:** Allows up to 2 mismatches in primer binding.

### Output FASTA format
**Args:** `ecopcr -d ref_db.fasta -p forward.fa -P reverse.fa -f -o amplicons.fasta`
**Explanation:** Outputs amplified sequences in FASTA format.

### Batch primer testing
**Args:** `ecopcr -d ref_db.fasta -p primers.txt -o results.txt`
**Explanation:** Tests multiple primer pairs from file.

### Quality report
**Args:** `ecopcr -d ref_db.fasta -p forward.fa -P reverse.fa -q -o quality.txt`
**Explanation:** Generates primer quality report with statistics.