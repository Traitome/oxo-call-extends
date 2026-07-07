---
name: phispy
category: metagenomics
description: phispy finds prophages using multiple metrics.
tags: [phispy, metagenomics, prophage, detection]
author: oxo-call-community
source_url: "https://github.com/linsalrob/PhiSpy"
---

## Concepts

- **Tool Overview**: phispy detects prophages.
- **Core Function**: Prophage finder tool.
- **Algorithm**: Uses multiple detection metrics.
- **Input Format**: Accepts bacterial genome files.
- **Output**: Produces prophage detection results.
- **Use Case**: Prophage detection, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Prophage Detection**: May miss novel prophages.
- **Genome Quality**: Results depend on genome quality.
- **Runtime**: Detection may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phispy --help`
**Explanation:** Shows available options and usage instructions.

### Find prophages
**Args:** `phispy -i bacteria.fasta -o prophage_regions.txt`
**Explanation:** Finds prophage regions.

### With parameters
**Args:** `phispy -i bacteria.fasta -p params.yaml -o prophage_regions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phispy -v -i bacteria.fasta -o prophage_regions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phispy -t 4 -i bacteria.fasta -o prophage_regions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phispy -i bacteria.fasta -o prophage_regions.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `phispy -i bacteria.fasta -o prophage_regions.txt --report report.html`
**Explanation:** Generates HTML report.