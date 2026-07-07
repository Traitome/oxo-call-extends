---
name: genomicconsensus
category: variant-calling
description: GenomicConsensus - PacBio genomic consensus and variant caller for RSII and Sequel.
tags: [genomicconsensus, variant-calling, pacbio, long-reads]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts
- **Consensus Calling**: Calls consensus sequences from PacBio data.
- **Variant Calling**: Detects variants from long-read sequencing.
- **PacBio Data**: Processes PacBio RSII and Sequel data.
- **Long-read Analysis**: Analyzes long-read sequencing data.
- **Haplotype Phasing**: Supports haplotype phasing.

## Pitfalls
- **Read Quality**: Requires high-quality long reads.
- **Computational Resources**: Large datasets require resources.
- **Memory Usage**: Significant memory required for analysis.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Validation**: Results should be validated with other methods.

## Examples
### Call consensus
**Args:** `python -m genomicconsensus -i aligned.bam -o consensus.fasta`
**Explanation:** Calls consensus sequence from aligned reads.

### Call variants
**Args:** `python -m genomicconsensus -i aligned.bam -v -o variants.vcf`
**Explanation:** Calls variants from PacBio data.

### Phase haplotypes
**Args:** `python -m genomicconsensus -i aligned.bam -p -o phased.fasta`
**Explanation:** Phases haplotypes from long reads.

### Batch processing
**Args:** `python -m genomicconsensus -i ./bam_files/ -o ./results/`
**Explanation:** Processes multiple BAM files in batch.

### Generate report
**Args:** `python -m genomicconsensus -i aligned.bam -r -o report.html`
**Explanation:** Generates consensus calling report.