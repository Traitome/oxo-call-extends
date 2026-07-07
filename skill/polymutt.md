---
name: polymutt
category: variant-calling
description: polymutt detects de novo mutations in families using likelihood-based framework.
tags: [polymutt, variant-calling, denovo, families]
author: oxo-call-community
source_url: "https://genome.sph.umich.edu/wiki/Polymutt"
---

## Concepts

- **Tool Overview**: polymutt calls variants in family data.
- **Core Function**: De novo mutation detection.
- **Algorithm**: Uses likelihood-based statistical methods.
- **Input Format**: Accepts VCF/GFF/GTF files.
- **Output**: Produces variant calls with de novo predictions.
- **Use Case**: Family-based variant analysis, genetic studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on genotype quality.
- **Calling Accuracy**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `polymutt --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `polymutt -i variants.vcf -o denovo.txt`
**Explanation:** Detects de novo mutations from family data.

### With parameters
**Args:** `polymutt -i variants.vcf -p params.yaml -o denovo.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `polymutt -v -i variants.vcf -o denovo.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `polymutt -t 4 -i variants.vcf -o denovo.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `polymutt -i variants.vcf -o denovo.vcf --vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `polymutt -i variants.vcf -o denovo.txt --report report.html`
**Explanation:** Generates HTML report.