---
name: physlr
category: utility
description: physlr generates next-generation physical maps.
tags: [physlr, utility, physical-maps, mapping]
author: oxo-call-community
source_url: "https://github.com/BirolLab/physlr"
---

## Concepts

- **Tool Overview**: physlr generates physical maps.
- **Core Function**: Next-generation physical mapping.
- **Algorithm**: Uses mapping algorithms.
- **Input Format**: Accepts sequencing data files.
- **Output**: Produces physical map results.
- **Use Case**: Genome mapping, physical mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Mapping Accuracy**: May have mapping errors.
- **Runtime**: Mapping may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `physlr --help`
**Explanation:** Shows available options and usage instructions.

### Generate physical map
**Args:** `physlr -i sequencing_data.txt -o physical_map.txt`
**Explanation:** Generates next-generation physical map.

### With parameters
**Args:** `physlr -i sequencing_data.txt -p params.yaml -o physical_map.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `physlr -v -i sequencing_data.txt -o physical_map.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `physlr -t 4 -i sequencing_data.txt -o physical_map.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `physlr -i sequencing_data.txt -o physical_map.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `physlr -i sequencing_data.txt -o physical_map.txt --report report.html`
**Explanation:** Generates HTML report.