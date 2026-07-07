---
name: pb-assembly
category: assembly
description: pb-assembly provides tools for PacBio sequencing assembly using Falcon/Unzip.
tags: [pb-assembly, assembly, pacbio, falcon]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pb-assembly assembles PacBio sequencing data.
- **Core Function**: Performs de novo assembly of long reads.
- **Algorithm**: Uses Falcon/Unzip assembly pipeline.
- **Input Format**: Accepts PacBio sequencing reads.
- **Output**: Produces assembled contigs/scaffolds.
- **Use Case**: Genome assembly, long-read sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on input read quality.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pb-assembly --help`
**Explanation:** Shows available options and usage instructions.

### Run assembly
**Args:** `fc_run.py config.ini`
**Explanation:** Runs Falcon assembly pipeline.

### Unzip assembly
**Args:** `fc_unzip.py -i assembly.fasta -o polished.fasta`
**Explanation:** Polishes assembly with Unzip.

### Verbose mode
**Args:** `fc_run.py -v config.ini`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `fc_run.py -t 16 config.ini`
**Explanation:** Uses 16 threads for parallel processing.

### Output format
**Args:** `fc_run.py -o output.fasta config.ini`
**Explanation:** Specifies output file.

### Generate report
**Args:** `fc_report.py -i assembly.fasta -o report.html`
**Explanation:** Generates assembly report.