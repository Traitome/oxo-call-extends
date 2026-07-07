---
name: nerpa
category: annotation
description: Nerpa discovers biosynthetic gene clusters of nonribosomal peptides and links them to known NRPs.
tags: [nerpa, annotation, bgc, nrp, bioinformatics]
author: oxo-call-community
source_url: "https://cab.spbu.ru/software/nerpa"
---

## Concepts

- **Tool Overview**: Nerpa links biosynthetic gene clusters (BGCs) to known nonribosomal peptides (NRPs).
- **Core Function**: Identifies BGCs in genome sequences and connects them to known NRP structures.
- **Algorithm**: Uses antiSMASH for BGC prediction and rBAN for NRP processing.
- **Input Format**: Accepts genome sequences (FASTA/GBK) and NRP structures in SMILES format.
- **Output**: Produces BGC-NRP linkage predictions and annotations.
- **Use Case**: Natural product discovery, drug development, and microbial genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **AntiSMASH Dependency**: Requires antiSMASH installation.
- **Input Quality**: Results depend on genome sequence quality.
- **SMILES Format**: Requires properly formatted SMILES strings.
- **Memory Usage**: Processing large genomes requires memory.
- **False Positives**: May report false positive BGC-NRP links.

## Examples

### Display help
**Args:** `nerpa --help`
**Explanation:** Shows available options and usage instructions.

### Basic analysis
**Args:** `nerpa -i genome.fasta -s nrps.smiles -o results/`
**Explanation:** Analyzes genome for NRP BGCs.

### GBK input
**Args:** `nerpa -i genome.gbk -s nrps.smiles -o results/`
**Explanation:** Uses GenBank format input.

### Multiple SMILES
**Args:** `nerpa -i genome.fasta -s nrps_list.txt -o results/`
**Explanation:** Processes multiple NRP structures.

### AntiSMASH integration
**Args:** `nerpa -i genome.fasta -s nrps.smiles --antismash results/ -o output/`
**Explanation:** Uses pre-computed antiSMASH results.

### Verbose output
**Args:** `nerpa -i genome.fasta -s nrps.smiles -v -o results/`
**Explanation:** Produces verbose output.

### Output JSON
**Args:** `nerpa -i genome.fasta -s nrps.smiles --json -o results.json`
**Explanation:** Outputs results in JSON format.