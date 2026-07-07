---
name: pyhoward
category: variant-calling
description: pyhoward is a workflow for annotation and ranking of genomic variants.
tags: [pyhoward, variant-calling, annotation, variant-ranking]
author: oxo-call-community
source_url: "https://github.com/bioinfo-chru-strasbourg/howard"
---

## Concepts

- **Tool Overview**: pyhoward annotates and ranks variants.
- **Core Function**: Variant annotation and ranking.
- **Algorithm**: Uses multiple annotation sources.
- **Input Format**: Accepts VCF files.
- **Output**: Produces annotated variants.
- **Use Case**: Variant prioritization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Annotation Sources**: Requires external databases.
- **Network Access**: May need internet.
- **Runtime**: Annotation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyhoward --help`
**Explanation:** Shows available options and usage instructions.

### Annotate variants
**Args:** `pyhoward annotate -i variants.vcf -o annotated.vcf`
**Explanation:** Annotates and ranks genomic variants.

### With parameters
**Args:** `pyhoward annotate -i variants.vcf -p params.yaml -o annotated.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyhoward -v annotate -i variants.vcf -o annotated.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyhoward -t 4 annotate -i variants.vcf -o annotated.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Rank variants
**Args:** `pyhoward rank -i annotated.vcf -o ranked.vcf`
**Explanation:** Ranks variants by pathogenicity.

### Generate report
**Args:** `pyhoward annotate -i variants.vcf -o annotated.vcf --report report.html`
**Explanation:** Generates HTML report.