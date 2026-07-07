---
name: radtk
category: utility
description: RADTK is a collection of tools for working with RAD (Random Amplified Polymorphic DNA) files and data.
tags: [radtk, utility, rad-seq, genotyping]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/radtk"
---

## Concepts

- **Tool Overview**: radtk processes RAD data.
- **Core Function**: RAD data analysis.
- **Algorithm**: Uses genotyping methods.
- **Input Format**: Accepts RAD files.
- **Output**: Produces genotypes.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **File Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `radtk --help`
**Explanation:** Shows available options and usage instructions.

### Process RAD data
**Args:** `radtk process -i rad_data.txt -o genotypes.txt`
**Explanation:** Processes RAD data.

### With parameters
**Args:** `radtk process -i rad_data.txt -p params.yaml -o genotypes.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `radtk -v process -i rad_data.txt -o genotypes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `radtk -t 4 process -i rad_data.txt -o genotypes.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Filter loci
**Args:** `radtk filter -i rad_data.txt -m 10 -o filtered.txt`
**Explanation:** Filters loci by minimum count.

### Generate report
**Args:** `radtk process -i rad_data.txt -o genotypes.txt --report report.html`
**Explanation:** Generates HTML report.