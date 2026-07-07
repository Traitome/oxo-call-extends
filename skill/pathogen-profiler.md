---
name: pathogen-profiler
category: metagenomics
description: Pathogen-Profiler identifies mutations and profiles pathogens from NGS data.
tags: [pathogen-profiler, metagenomics, variant-calling, pathogen-analysis]
author: oxo-call-community
source_url: "https://github.com/jodyphelan/pathogen-profiler"
---

## Concepts

- **Tool Overview**: Pathogen-Profiler analyzes pathogen sequences.
- **Core Function**: Identifies mutations and drug resistance markers.
- **Algorithm**: Uses variant calling and database matching.
- **Input Format**: Accepts sequencing reads or assemblies.
- **Output**: Produces mutation profiles and reports.
- **Use Case**: Clinical microbiology, drug resistance analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Database Updates**: Requires updated pathogen databases.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathogen-profiler --help`
**Explanation:** Shows available options and usage instructions.

### Profile pathogen
**Args:** `pathogen-profiler profile -i reads.fastq -o profile/`
**Explanation:** Profiles pathogen from sequencing reads.

### With assembly
**Args:** `pathogen-profiler profile -i assembly.fasta -o profile/`
**Explanation:** Profiles assembled genome.

### Verbose mode
**Args:** `pathogen-profiler -v profile -i reads.fastq -o profile/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pathogen-profiler -t 8 profile -i reads.fastq -o profile/`
**Explanation:** Uses 8 threads for parallel processing.

### Species detection
**Args:** `pathogen-profiler detect -i reads.fastq -o species.txt`
**Explanation:** Detects pathogen species.

### Update databases
**Args:** `pathogen-profiler update`
**Explanation:** Updates reference databases.