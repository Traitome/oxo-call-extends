---
name: neoloop
category: utility
description: NeoLoop predicts neo-loops induced by structural variations in the genome.
tags: [neoloop, utility, structural-variation, chromatin, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/XiaoTaoWang/NeoLoopFinder"
---

## Concepts

- **Tool Overview**: NeoLoop predicts novel chromatin loops formed due to structural variations.
- **Core Function**: Identifies potential neo-loops created by genomic rearrangements.
- **Algorithm**: Uses Hi-C data and structural variant calls to predict loop formation.
- **Input Format**: Accepts Hi-C contact maps and VCF files with structural variants.
- **Output**: Produces predicted neo-loop coordinates and confidence scores.
- **Use Case**: 3D genome analysis, cancer genomics, and regulatory element studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Hi-C Quality**: Results depend on Hi-C data quality.
- **Variant Quality**: Requires high-quality structural variant calls.
- **Memory Usage**: Processing large Hi-C datasets requires memory.
- **Resolution**: Results depend on Hi-C resolution.
- **False Positives**: May predict false positive neo-loops.

## Examples

### Display help
**Args:** `neoloop --help`
**Explanation:** Shows available options and usage instructions.

### Basic prediction
**Args:** `neoloop -i hic.matrix -v variants.vcf -o neo-loops.bedpe`
**Explanation:** Predicts neo-loops from Hi-C and variants.

### Hi-C resolution
**Args:** `neoloop -i hic.matrix -v variants.vcf -r 10000 -o neo-loops.bedpe`
**Explanation:** Uses 10kb resolution for Hi-C data.

### Confidence threshold
**Args:** `neoloop -i hic.matrix -v variants.vcf -c 0.9 -o neo-loops.bedpe`
**Explanation:** Sets confidence threshold to 0.9.

### Output statistics
**Args:** `neoloop -i hic.matrix -v variants.vcf -s stats.tsv -o neo-loops.bedpe`
**Explanation:** Outputs prediction statistics.

### Visualization
**Args:** `neoloop -i hic.matrix -v variants.vcf --plot -o plot.pdf`
**Explanation:** Generates visualization of predicted neo-loops.

### Reference genome
**Args:** `neoloop -i hic.matrix -v variants.vcf -g genome.fasta -o neo-loops.bedpe`
**Explanation:** Uses reference genome for annotation.