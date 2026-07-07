---
name: merfin
category: variant-calling
description: Variant filtering and polishing tool using k-mer validation.
tags: [merfin, variant-filtering, polishing]
author: oxo-call-community
source_url: "https://github.com/arangrhie/merfin"
---

## Concepts

- **Tool Overview**: Merfin validates and filters variants using k-mer analysis.
- **Core Function**: k-mer-based variant validation.
- **Variant Filtering**: Filters false positive variants.
- **Polishing**: Improves variant calls.
- **Reference-based**: Uses reference genome for validation.
- **Installation**: `conda install -c bioconda merfin`

## Pitfalls

- **Reference Dependence**: Requires reference genome.
- **k-mer Database**: Needs k-mer database built from reads.
- **Memory Requirements**: High memory for large datasets.
- **Computation Time**: Slow for large variant sets.
- **Parameter Tuning**: Requires careful threshold adjustment.
- **False Negatives**: May filter true variants.

## Examples

### Validate variants
**Args:** `merfin -v variants.vcf -r ref.fasta -k kmer_db -o filtered.vcf`
**Explanation:** Validates variants using k-mers.

### Build k-mer database
**Args:** `merfin build -i reads.fastq -o kmer_db`
**Explanation:** Builds k-mer database from reads.

### Polish variants
**Args:** `merfin polish -v variants.vcf -r ref.fasta -k kmer_db -o polished.vcf`
**Explanation:** Polishes variant calls.

### Verbose mode
**Args:** `merfin -v variants.vcf -r ref.fasta -k kmer_db -V -o filtered.vcf`
**Explanation:** Shows detailed validation process.

### Help documentation
**Args:** `merfin --help`
**Explanation:** Displays available options.
