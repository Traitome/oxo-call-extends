---
name: methphaser
category: variant-calling
description: "MethPhaser: methylation-based haplotype phasing of human genomes"
tags: [methphaser, variant-calling, haplotype-phasing]
author: oxo-call-community
source_url: "https://github.com/treangenlab/methphaser"
---
## Concepts

- **Tool Overview**: MethPhaser v0.0.3 is a tool for methylation-based haplotype phasing of human genomes.
- **Core Function**: Performs haplotype phasing using DNA methylation information.
- **Methylation-based Phasing**: Uses methylation patterns to phase genetic variants.
- **Single-molecule Resolution**: Leverages single-molecule sequencing data for phasing.
- **Input/Output**: Accepts sequencing reads with methylation calls; outputs phased haplotypes.
- **Phase Integration**: Integrates methylation information with genetic variant data.

## Pitfalls

- **Human Genome Focus**: Designed primarily for human genome analysis.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal phasing.
- **Data Quality**: Phasing accuracy depends on input data quality.
- **Methylation Coverage**: Requires sufficient methylation coverage for accurate phasing.

## Examples

### Phase haplotypes
**Args:** `methphaser -i reads.bam -o haplotypes.txt`
**Explanation:** Performs methylation-based haplotype phasing.

### With variant file
**Args:** `methphaser -i reads.bam -v variants.vcf -o haplotypes.txt`
**Explanation:** Uses known variants for improved phasing.

### With reference genome
**Args:** `methphaser -i reads.bam -r reference.fasta -o haplotypes.txt`
**Explanation:** Uses reference genome for phasing.

### Generate visualization
**Args:** `methphaser -i reads.bam -o haplotypes.txt -p plot.png`
**Explanation:** Generates phasing visualization.

### Detailed output
**Args:** `methphaser -i reads.bam -o haplotypes.txt -v`
**Explanation:** Generates detailed phasing report.