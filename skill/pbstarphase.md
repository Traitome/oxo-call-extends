---
name: pbstarphase
category: qc
description: pbStarPhase performs phase-aware pharmacogenomic diplotype calling.
tags: [pbstarphase, qc, pacbio, pharmacogenomics]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pb-StarPhase"
---

## Concepts

- **Tool Overview**: pbStarPhase calls pharmacogenomic diplotypes.
- **Core Function**: Identifies phased pharmacogenomic alleles.
- **Algorithm**: Uses phase-aware diplotype calling.
- **Input Format**: Accepts PacBio alignments.
- **Output**: Produces diplotype assignments.
- **Use Case**: Pharmacogenomics, personalized medicine.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Gene Coverage**: Requires sufficient coverage for calling.
- **Database Quality**: Results depend on reference database.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `starphase --help`
**Explanation:** Shows available options and usage instructions.

### Call diplotypes
**Args:** `starphase -i alignments.bam -o diplotypes.txt`
**Explanation:** Calls pharmacogenomic diplotypes.

### With reference
**Args:** `starphase -i alignments.bam -r reference.fasta -o diplotypes.txt`
**Explanation:** Uses reference genome for calling.

### Verbose mode
**Args:** `starphase -v -i alignments.bam -o diplotypes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `starphase -t 8 -i alignments.bam -o diplotypes.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `starphase -i alignments.bam -o diplotypes.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `starphase -i alignments.bam -o diplotypes.txt --report report.html`
**Explanation:** Generates HTML report.