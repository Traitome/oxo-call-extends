---
name: pisces
category: variant-calling
description: pisces calls somatic and germline variants from amplicon data.
tags: [pisces, variant-calling, somatic, germline]
author: oxo-call-community
source_url: "https://github.com/Illumina/Pisces"
---

## Concepts

- **Tool Overview**: pisces calls variants from amplicon data.
- **Core Function**: Somatic and germline variant calling.
- **Algorithm**: Uses variant detection methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces VCF variant calls.
- **Use Case**: Amplicon sequencing, tumor-only workflows.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequencing Quality**: Results depend on data quality.
- **Variant Calling**: May have false positives/negatives.
- **Runtime**: Calling may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pisces --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `pisces -i alignment.bam -o variants.vcf`
**Explanation:** Calls variants from amplicon data.

### With parameters
**Args:** `pisces -i alignment.bam -p params.yaml -o variants.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pisces -v -i alignment.bam -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pisces -t 4 -i alignment.bam -o variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pisces -i alignment.bam -o variants.vcf --gvcf`
**Explanation:** Outputs in gVCF format.

### Generate report
**Args:** `pisces -i alignment.bam -o variants.vcf --report report.html`
**Explanation:** Generates HTML report.