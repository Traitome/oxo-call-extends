---
name: mehari
category: variant-calling
description: VEP-like variant annotation tool for sequence ontology and HGVS annotation written in Rust.
tags: [mehari, variant-annotation, HGVS]
author: oxo-call-community
source_url: "https://github.com/varfish-org/mehari"
---

## Concepts

- **Tool Overview**: Mehari annotates VCF files with sequence ontology and HGVS.
- **Core Function**: Fast variant annotation using Rust.
- **HGVS Annotation**: Generates HGVS variant descriptions.
- **Sequence Ontology**: Annotates with SO terms.
- **VEP Compatibility**: Similar output to Ensembl VEP.
- **Installation**: `conda install -c bioconda mehari`

## Pitfalls

- **Reference Requirements**: Requires reference genome.
- **Database Updates**: Needs updated annotation databases.
- **Memory Requirements**: High memory for large databases.
- **Complex Variants**: May struggle with complex variants.
- **Format Compatibility**: Only supports VCF format.
- **Rust Dependencies**: Requires Rust runtime.

## Examples

### Annotate VCF
**Args:** `mehari -i variants.vcf -r ref.fasta -o annotated.vcf`
**Explanation:** Annotates VCF with SO and HGVS.

### HGVS only
**Args:** `mehari -i variants.vcf -r ref.fasta --hgvs-only -o annotated.vcf`
**Explanation:** Only generates HGVS annotations.

### Verbose mode
**Args:** `mehari -i variants.vcf -r ref.fasta -v -o annotated.vcf`
**Explanation:** Shows detailed annotation progress.

### Offline mode
**Args:** `mehari -i variants.vcf -r ref.fasta --offline -o annotated.vcf`
**Explanation:** Uses local databases only.

### Help documentation
**Args:** `mehari --help`
**Explanation:** Displays available options.
