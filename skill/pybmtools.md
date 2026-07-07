---
name: pybmtools
category: epigenomics
description: pybmtools is a Python extension written in C for quick access to DNA methylation BM files.
tags: [pybmtools, epigenomics, methylation, c-extension]
author: oxo-call-community
source_url: "https://github.com/ZhouQiangwei/pybmtools"
---

## Concepts

- **Tool Overview**: pybmtools reads methylation files.
- **Core Function**: Methylation data access.
- **Algorithm**: Uses C-based parsing.
- **Input Format**: Accepts BM files.
- **Output**: Produces methylation values.
- **Use Case**: Epigenomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on file integrity.
- **Format Compatibility**: May have version issues.
- **Runtime**: Access may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pybmtools --help`
**Explanation:** Shows available options and usage instructions.

### Extract methylation
**Args:** `pybmtools extract -i methyl.bm -c chr1:1-1000 -o values.txt`
**Explanation:** Extracts methylation values from region.

### With parameters
**Args:** `pybmtools extract -i methyl.bm -p params.yaml -o values.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pybmtools -v extract -i methyl.bm -o values.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pybmtools -t 4 extract -i methyl.bm -o values.txt`
**Explanation:** Uses 4 threads for parallel processing.

### List chromosomes
**Args:** `pybmtools list -i methyl.bm`
**Explanation:** Lists available chromosomes.

### Generate report
**Args:** `pybmtools extract -i methyl.bm -o values.txt --report report.html`
**Explanation:** Generates HTML report.