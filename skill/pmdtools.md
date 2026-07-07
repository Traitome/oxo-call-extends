---
name: pmdtools
category: utility
description: pmdtools computes postmortem damage patterns in ancient genomes.
tags: [pmdtools, utility, ancient-dna, damage]
author: oxo-call-community
source_url: "https://github.com/pontussk/PMDtools"
---

## Concepts

- **Tool Overview**: pmdtools analyzes ancient DNA damage.
- **Core Function**: Postmortem damage pattern computation.
- **Algorithm**: Uses statistical damage detection methods.
- **Input Format**: Accepts BAM/SAM alignment files.
- **Output**: Produces damage pattern results.
- **Use Case**: Ancient DNA analysis, paleogenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Damage Detection**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pmdtools --help`
**Explanation:** Shows available options and usage instructions.

### Analyze damage patterns
**Args:** `pmdtools -i ancient.bam -o damage.txt`
**Explanation:** Computes postmortem damage patterns.

### With parameters
**Args:** `pmdtools -i ancient.bam -p params.yaml -o damage.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pmdtools -v -i ancient.bam -o damage.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pmdtools -t 4 -i ancient.bam -o damage.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pmdtools -i ancient.bam -o damage.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pmdtools -i ancient.bam -o damage.txt --report report.html`
**Explanation:** Generates HTML report.