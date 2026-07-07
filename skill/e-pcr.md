---
name: e-pcr
category: utility
description: "Electronic PCR tool for primer design and validation"
tags: [e-pcr, utility, primer-design, PCR, sequence-analysis]
author: oxo-call-community
source_url: "ftp://ftp.ncbi.nlm.nih.gov/pub/schuler/e-PCR/e-PCR-2.3.12-1-src.tar.gz"
---

## Concepts

- **Tool Overview**: e-PCR is an electronic PCR tool that simulates PCR amplification in silico, used for primer design validation and amplicon prediction.
- **Core Function**: Tests primer specificity by searching for potential amplification sites in a sequence database.
- **Input/Output**: Input: Primer sequences, target sequence database (FASTA). Output: Predicted amplicons, primer binding sites, amplification statistics.
- **Algorithm**: Uses sequence alignment to identify potential primer binding sites and predict PCR product sizes.
- **Key Features**: Primer specificity testing, amplicon prediction, mismatch tolerance, batch processing, integration with NCBI databases.
- **Installation**: `conda install -c bioconda e-pcr`

## Pitfalls

- **Database Format**: Requires specific database indexing.
- **Primer Quality**: Poorly designed primers may give misleading results.
- **Mismatch Tolerance**: Default parameters may need adjustment.
- **Computation Time**: Large databases can be slow to process.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic electronic PCR
**Args:** `e-PCR -d database.fasta -p forward.primer -P reverse.primer -o results.txt`
**Explanation:** Performs in silico PCR with forward and reverse primers.

### With mismatch tolerance
**Args:** `e-PCR -d database.fasta -p forward.primer -P reverse.primer -m 2 -o results.txt`
**Explanation:** Allows up to 2 mismatches in primer binding.

### Output FASTA format
**Args:** `e-PCR -d database.fasta -p forward.primer -P reverse.primer -f -o amplicons.fasta`
**Explanation:** Outputs predicted amplicons in FASTA format.

### Batch primer testing
**Args:** `e-PCR -d database.fasta -p primers.txt -o results.txt`
**Explanation:** Tests multiple primer pairs from file.

### Quality report
**Args:** `e-PCR -d database.fasta -p forward.primer -P reverse.primer -q -o quality.txt`
**Explanation:** Generates primer quality report.