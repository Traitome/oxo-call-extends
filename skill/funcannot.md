---
name: funcannot
category: variant-calling
description: Annotates cDNA, protein, mutation type, and other functional changes to variants in a VCF file with pre-existing gene annotations.
tags: [funcannot, variant annotation, VCF, functional annotation]
author: oxo-call-community
source_url: "https://github.com/BioTools-Tek/funcannot"
---

## Concepts
- **Variant Annotation**: Adds functional annotations to genetic variants.
- **cDNA Annotation**: Annotates variants at the cDNA level.
- **Protein Effect**: Predicts protein-level effects of variants.
- **Mutation Type**: Classifies mutation types (missense, nonsense, etc.).
- **Gene Annotation**: Integrates with gene annotation databases.

## Pitfalls
- **VCF Dependencies**: Requires properly formatted VCF files.
- **Annotation Files**: Needs pre-existing gene annotations.
- **Format Compatibility**: Output format may need conversion for some tools.
- **Memory Usage**: Large VCF files require significant memory.
- **Interpretation**: Requires understanding of variant effects.

## Examples
### Basic variant annotation
**Args:** `funcannot -i variants.vcf -g genes.gff -o annotated.vcf`
**Explanation:** Annotates variants with gene information.

### With cDNA annotation
**Args:** `funcannot -i variants.vcf -g genes.gff --cdna -o annotated.vcf`
**Explanation:** Adds cDNA-level annotations.

### Protein effect prediction
**Args:** `funcannot -i variants.vcf -g genes.gff --protein -o annotated.vcf`
**Explanation:** Predicts protein effects of variants.

### Full annotation
**Args:** `funcannot -i variants.vcf -g genes.gff --full -o annotated.vcf`
**Explanation:** Adds comprehensive functional annotations.

### Output to CSV
**Args:** `funcannot -i variants.vcf -g genes.gff --csv -o annotations.csv`
**Explanation:** Outputs annotations in CSV format.