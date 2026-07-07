---
name: poplddecay
category: formatting
description: poplddecay analyzes linkage disequilibrium decay from VCF files.
tags: [poplddecay, formatting, ld-decay, population]
author: oxo-call-community
source_url: "https://github.com/BGI-shenzhen/PopLDdecay"
---

## Concepts

- **Tool Overview**: poplddecay analyzes LD decay.
- **Core Function**: Linkage disequilibrium analysis.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts VCF files.
- **Output**: Produces LD decay statistics.
- **Use Case**: Population genetics, genomic selection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on genotype quality.
- **Statistical Power**: May have estimation errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `PopLDdecay --help`
**Explanation:** Shows available options and usage instructions.

### Analyze LD decay
**Args:** `PopLDdecay -InVCF variants.vcf -OutStat ld_decay`
**Explanation:** Analyzes linkage disequilibrium decay.

### With parameters
**Args:** `PopLDdecay -InVCF variants.vcf -OutStat ld_decay -Params params.yaml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `PopLDdecay -v -InVCF variants.vcf -OutStat ld_decay`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `PopLDdecay -T 4 -InVCF variants.vcf -OutStat ld_decay`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `PopLDdecay -InVCF variants.vcf -OutStat ld_decay -OutType csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `PopLDdecay -InVCF variants.vcf -OutStat ld_decay -Report report.html`
**Explanation:** Generates HTML report.