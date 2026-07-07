---
name: ntm-profiler
category: diagnostics
description: NTM-Profiler detects Non-Tuberculous Mycobacteria species and resistance from WGS data.
tags: [ntm-profiler, diagnostics, mycobacteria, wgs]
author: oxo-call-community
source_url: "https://github.com/jodyphelan/NTM-Profiler"
---

## Concepts

- **Tool Overview**: NTM-Profiler identifies NTM species and predicts drug resistance from sequencing data.
- **Core Function**: Species identification and antibiotic resistance prediction.
- **Algorithm**: Uses database comparison and variant calling for detection.
- **Input Format**: Accepts FASTQ reads or assembled genomes.
- **Output**: Produces species identification and resistance profiles.
- **Use Case**: Clinical diagnostics, mycobacteria identification, and antibiotic susceptibility testing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Database Updates**: Requires regular database updates.
- **Sequencing Depth**: Requires sufficient sequencing depth.
- **False Positives**: May report false resistance calls.
- **Validation**: Results should be experimentally validated.
- **Reference Genome**: Requires appropriate reference database.

## Examples

### Display help
**Args:** `ntm-profiler --help`
**Explanation:** Shows available options and usage instructions.

### Run profiling
**Args:** `ntm-profiler profile -i reads.fastq -o results/`
**Explanation:** Profiles NTM species and resistance from reads.

### With assembly
**Args:** `ntm-profiler profile -a assembly.fasta -o results/`
**Explanation:** Profiles from assembled genome.

### Output JSON
**Args:** `ntm-profiler profile -i reads.fastq -o results.json --json`
**Explanation:** Outputs results in JSON format.

### Update database
**Args:** `ntm-profiler update`
**Explanation:** Updates reference database.

### List databases
**Args:** `ntm-profiler databases`
**Explanation:** Shows available databases.

### Verbose mode
**Args:** `ntm-profiler profile -i reads.fastq -v -o results/`
**Explanation:** Runs with verbose output.

### Force update
**Args:** `ntm-profiler update --force`
**Explanation:** Forces database update.