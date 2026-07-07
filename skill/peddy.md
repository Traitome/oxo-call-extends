---
name: peddy
category: variant-calling
description: peddy checks genotype-pedigree correspondence, ancestry, and sex from VCF.
tags: [peddy, variant-calling, pedigree, ancestry]
author: oxo-call-community
source_url: "https://github.com/brentp/peddy"
---

## Concepts

- **Tool Overview**: peddy validates pedigree data.
- **Core Function**: Checks genotype-pedigree correspondence.
- **Algorithm**: Uses ancestry and sex inference.
- **Input Format**: Accepts VCF and PED files.
- **Output**: Produces validation reports.
- **Use Case**: Quality control, pedigree validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large VCF files require memory.
- **Sample Quality**: Results depend on genotype quality.
- **Ancestry Accuracy**: Inference may have limitations.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peddy --help`
**Explanation:** Shows available options and usage instructions.

### Check pedigree
**Args:** `peddy -p family.ped -i samples.vcf -o peddy_output/`
**Explanation:** Checks pedigree correspondence.

### With ancestry
**Args:** `peddy -p family.ped -i samples.vcf -o peddy_output/ --ancestry`
**Explanation:** Includes ancestry inference.

### Verbose mode
**Args:** `peddy -v -p family.ped -i samples.vcf -o peddy_output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peddy -t 4 -p family.ped -i samples.vcf -o peddy_output/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peddy -p family.ped -i samples.vcf -o peddy_output/ --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `peddy -p family.ped -i samples.vcf -o peddy_output/ --plot`
**Explanation:** Generates visualization plots.