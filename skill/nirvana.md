---
name: nirvana
category: variant-calling
description: Nirvana provides clinical-grade annotation of genomic variants including SNVs, MNVs, indels, and SVs.
tags: [nirvana, variant-calling, annotation, clinical]
author: oxo-call-community
source_url: "https://github.com/Illumina/Nirvana"
---

## Concepts

- **Tool Overview**: Nirvana annotates genomic variants with clinical-grade precision.
- **Core Function**: Provides comprehensive variant annotation including functional impact.
- **Algorithm**: Integrates multiple annotation sources for accurate variant classification.
- **Input Format**: Accepts VCF files with variant calls.
- **Output**: Produces JSON or VCF with annotated variants.
- **Use Case**: Clinical genomics, variant interpretation, and precision medicine.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Data**: Requires up-to-date annotation databases.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Annotation can be computationally intensive.
- **Database Updates**: Requires regular database updates.
- **License**: Check licensing for commercial use.

## Examples

### Display help
**Args:** `Nirvana --help`
**Explanation:** Shows available options and usage instructions.

### Annotate VCF
**Args:** `Nirvana -i variants.vcf -r reference.fasta -d data/ -o annotated.json`
**Explanation:** Annotates variants in VCF file.

### VCF output
**Args:** `Nirvana -i variants.vcf -r reference.fasta -d data/ -o annotated.vcf --vcf`
**Explanation:** Outputs annotated variants in VCF format.

### Full annotation
**Args:** `Nirvana -i variants.vcf -r reference.fasta -d data/ -o annotated.json --full`
**Explanation:** Includes all available annotations.

### Threads
**Args:** `Nirvana -i variants.vcf -r reference.fasta -d data/ -t 8 -o annotated.json`
**Explanation:** Uses 8 threads for parallel processing.

### Cache mode
**Args:** `Nirvana -i variants.vcf -r reference.fasta -d data/ -c -o annotated.json`
**Explanation:** Uses cache for faster processing.

### Quiet mode
**Args:** `Nirvana -i variants.vcf -r reference.fasta -d data/ -q -o annotated.json`
**Explanation:** Runs in quiet mode with minimal output.