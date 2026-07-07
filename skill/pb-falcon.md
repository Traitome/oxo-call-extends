---
name: pb-falcon
category: utility
description: pb-falcon provides the FALCON/Unzip assembly tool-suite.
tags: [pb-falcon, utility, assembly, pacbio]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pb-falcon assembles PacBio sequencing data.
- **Core Function**: Performs de novo assembly of long reads.
- **Algorithm**: Uses FALCON assembly pipeline.
- **Input Format**: Accepts PacBio sequencing reads.
- **Output**: Produces assembled contigs.
- **Use Case**: Genome assembly, long-read sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on input quality.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `falcon --help`
**Explanation:** Shows available options and usage instructions.

### Run assembly
**Args:** `fc_run.py config.ini`
**Explanation:** Runs FALCON assembly pipeline.

### Polish assembly
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