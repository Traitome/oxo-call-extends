---
name: pycov3
category: utility
description: pycov3 generates cov3 files used in DEMIC for coverage analysis.
tags: [pycov3, utility, coverage, demic]
author: oxo-call-community
source_url: "https://github.com/Ulthran/pycov3"
---

## Concepts

- **Tool Overview**: pycov3 generates cov3 files.
- **Core Function**: Coverage file generation.
- **Algorithm**: Uses coverage calculations.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces cov3 files.
- **Use Case**: Coverage analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Format Compatibility**: Must match DEMIC requirements.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pycov3 --help`
**Explanation:** Shows available options and usage instructions.

### Generate cov3 file
**Args:** `pycov3 -i aligned.bam -o coverage.cov3`
**Explanation:** Generates cov3 file from BAM alignment.

### With parameters
**Args:** `pycov3 -i aligned.bam -p params.yaml -o coverage.cov3`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pycov3 -v -i aligned.bam -o coverage.cov3`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pycov3 -t 4 -i aligned.bam -o coverage.cov3`
**Explanation:** Uses 4 threads for parallel processing.

### Bed region
**Args:** `pycov3 -i aligned.bam -b regions.bed -o coverage.cov3`
**Explanation:** Calculates coverage for specific regions.

### Generate report
**Args:** `pycov3 -i aligned.bam -o coverage.cov3 --report report.html`
**Explanation:** Generates HTML report.