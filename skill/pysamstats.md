---
name: pysamstats
category: alignment
description: PySAMstats calculates read mapping statistics from SAM/BAM/CRAM alignment files.
tags: [pysamstats, alignment, bam, sam, cram]
author: oxo-call-community
source_url: "https://github.com/alimanfoo/pysamstats"
---

## Concepts

- **Tool Overview**: pysamstats computes mapping stats.
- **Core Function**: Statistics calculation.
- **Algorithm**: Uses SAMtools API.
- **Input Format**: Accepts BAM/SAM/CRAM files.
- **Output**: Produces statistics.
- **Use Case**: Alignment QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **BAM Index**: Must be present.
- **Coverage Depth**: Affects statistics.
- **Runtime**: Calculation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pysamstats --help`
**Explanation:** Shows available options and usage instructions.

### Calculate stats
**Args:** `pysamstats stats -i alignment.bam -o stats.txt`
**Explanation:** Computes mapping statistics.

### With parameters
**Args:** `pysamstats stats -i alignment.bam -p params.yaml -o stats.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pysamstats -v stats -i alignment.bam -o stats.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pysamstats -t 4 stats -i alignment.bam -o stats.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Per-base stats
**Args:** `pysamstats per-base -i alignment.bam -o per_base.txt`
**Explanation:** Generates per-base statistics.

### Generate report
**Args:** `pysamstats stats -i alignment.bam -o stats.txt --report report.html`
**Explanation:** Generates HTML report.