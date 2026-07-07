---
name: pgdspider
category: population-genomics
description: PGDSpider converts data between population genetics programs.
tags: [pgdspider, population-genomics, conversion, genetics]
author: oxo-call-community
source_url: "http://www.cmpg.unibe.ch/software/PGDSpider/"
---

## Concepts

- **Tool Overview**: PGDSpider converts genetic data.
- **Core Function**: Converts data between programs.
- **Algorithm**: Uses automated format conversion.
- **Input Format**: Accepts various genetic data formats.
- **Output**: Produces converted data files.
- **Use Case**: Population genetics, data conversion.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Format Compatibility**: Requires proper format specification.
- **Data Loss**: Conversion may lose some information.
- **Runtime**: Conversion may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgdspider --help`
**Explanation:** Shows available options and usage instructions.

### Convert data
**Args:** `pgdspider -i input.vcf -o output.gen -f vcf -t gen`
**Explanation:** Converts VCF to GEN format.

### With parameters
**Args:** `pgdspider -i input.vcf -o output.txt -f vcf -t arlequin`
**Explanation:** Converts to Arlequin format.

### Verbose mode
**Args:** `pgdspider -v -i input.vcf -o output.gen -f vcf -t gen`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgdspider -t 4 -i input.vcf -o output.gen -f vcf -t gen`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgdspider -i input.vcf -o output.tsv -f vcf -t tsv`
**Explanation:** Converts to TSV format.

### Generate report
**Args:** `pgdspider -i input.vcf -o output.gen -f vcf -t gen --report report.html`
**Explanation:** Generates HTML report.