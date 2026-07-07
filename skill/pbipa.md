---
name: pbipa
category: assembly
description: pbIPA provides Improved Phased Assembly for PacBio sequencing data.
tags: [pbipa, assembly, pacbio, phased]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbIPA performs phased assembly.
- **Core Function**: Generates phased haplotype assemblies.
- **Algorithm**: Uses haplotype-aware assembly algorithms.
- **Input Format**: Accepts PacBio sequencing reads.
- **Output**: Produces phased contigs.
- **Use Case**: Haplotype assembly, diploid genomes.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on input quality.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ipa --help`
**Explanation:** Shows available options and usage instructions.

### Run assembly
**Args:** `ipa -i reads.bam -o assembly/`
**Explanation:** Runs phased assembly pipeline.

### With reference
**Args:** `ipa -i reads.bam -r reference.fasta -o assembly/`
**Explanation:** Uses reference for assembly.

### Verbose mode
**Args:** `ipa -v -i reads.bam -o assembly/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ipa -t 16 -i reads.bam -o assembly/`
**Explanation:** Uses 16 threads for parallel processing.

### Output format
**Args:** `ipa -i reads.bam -o assembly.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `ipa -i reads.bam -o assembly/ --report report.html`
**Explanation:** Generates assembly report.