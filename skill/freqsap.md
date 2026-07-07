---
name: freqsap
category: utility
description: freqsap can be used to query the frequency of single amino-acid polymorphisms.
tags: [freqsap, amino acid polymorphisms, frequency analysis, protein variation]
author: oxo-call-community
source_url: "https://github.com/RECETOX/freqsap"
---

## Concepts
- **Variant Frequency**: Queries frequencies of single amino acid polymorphisms.
- **Database Query**: Accesses comprehensive databases of protein variants.
- **Population Analysis**: Analyzes variant frequencies across populations.
- **Protein Structure**: Integrates structural information for variant analysis.
- **Annotation Integration**: Combines variant data with functional annotations.

## Pitfalls
- **Database Coverage**: Limited by database coverage and update frequency.
- **Population Bias**: Frequency data may be biased towards certain populations.
- **Data Quality**: Depends on quality of source databases.
- **Ambiguous Variants**: May have issues with ambiguous variant descriptions.
- **Output Interpretation**: Requires understanding of population genetics.

## Examples
### Query variant frequency
**Args:** `freqsap query --gene TP53 --position 72 --wildtype R --variant H`
**Explanation:** Queries frequency of R72H variant in TP53.

### Batch query
**Args:** `freqsap batch --input variants.txt --output frequencies.txt`
**Explanation:** Queries frequencies for multiple variants.

### Population-specific frequency
**Args:** `freqsap query --gene BRCA1 --position 185 --wildtype E --variant Q --population EUR`
**Explanation:** Queries frequency in European population.

### Structural analysis
**Args:** `freqsap structure --gene TP53 --position 72 --output structure.png`
**Explanation:** Analyzes structural impact of variant.

### Export to VCF
**Args:** `freqsap export --input variants.txt --output variants.vcf`
**Explanation:** Exports results in VCF format.