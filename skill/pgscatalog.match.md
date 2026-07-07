---
name: pgscatalog.match
category: variant-calling
description: pgscatalog.match matches variants in PGS scoring files.
tags: [pgscatalog.match, variant-calling, matching, pgs]
author: oxo-call-community
source_url: "https://github.com/PGScatalog/pygscatalog"
---

## Concepts

- **Tool Overview**: pgscatalog.match matches variants.
- **Core Function**: Matches PGS scoring file variants.
- **Algorithm**: Uses variant matching algorithms.
- **Input Format**: Accepts VCF and PGS files.
- **Output**: Produces matched variant results.
- **Use Case**: Variant matching, PGS application.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large variant sets require memory.
- **Variant Quality**: Results depend on variant quality.
- **Reference Genome**: Requires proper reference genome.
- **Runtime**: Matching may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgscatalog.match --help`
**Explanation:** Shows available options and usage instructions.

### Match variants
**Args:** `pgscatalog.match -i target.vcf -p pgs.txt -o matched.txt`
**Explanation:** Matches variants in PGS file.

### With reference
**Args:** `pgscatalog.match -i target.vcf -p pgs.txt -r ref.fa -o matched.txt`
**Explanation:** Uses specific reference genome.

### Verbose mode
**Args:** `pgscatalog.match -v -i target.vcf -p pgs.txt -o matched.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgscatalog.match -t 4 -i target.vcf -p pgs.txt -o matched.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgscatalog.match -i target.vcf -p pgs.txt -o matched.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pgscatalog.match -i target.vcf -p pgs.txt -o matched.txt --report report.html`
**Explanation:** Generates HTML report.