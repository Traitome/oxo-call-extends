---
name: protmapper
category: alignment
description: protmapper maps protein sites to human reference sequences for annotation.
tags: [protmapper, alignment, proteomics, annotation]
author: oxo-call-community
source_url: "https://protmapper.readthedocs.io"
---

## Concepts

- **Tool Overview**: protmapper maps protein modification sites.
- **Core Function**: Site mapping and annotation.
- **Algorithm**: Uses sequence alignment methods.
- **Input Format**: Accepts protein site data.
- **Output**: Produces mapped annotations.
- **Use Case**: Protein modification analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Reference Version**: Affects mapping accuracy.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `protmapper --help`
**Explanation:** Shows available options and usage instructions.

### Map sites
**Args:** `protmapper -i sites.txt -o mapped_sites.txt`
**Explanation:** Maps protein sites to reference sequences.

### With parameters
**Args:** `protmapper -i sites.txt --params params.yaml -o mapped_sites.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `protmapper -v -i sites.txt -o mapped_sites.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `protmapper -t 4 -i sites.txt -o mapped_sites.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `protmapper -i sites.txt -o mapped_sites.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `protmapper -i sites.txt -o mapped_sites.txt --report report.html`
**Explanation:** Generates HTML report.