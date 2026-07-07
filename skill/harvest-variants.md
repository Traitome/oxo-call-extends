---
name: harvest-variants
category: bioinformatics
description: Harvest Variants is a pipeline for variant calling on SARS-CoV-2 samples.
tags: [harvest-variants, variant-calling, SARS-CoV-2, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/sars-cov-2-harvest-variants"
---

## Concepts

- **SARS-CoV-2 Variant Calling**: Harvest Variants calls variants from SARS-CoV-2 samples.

- **Pipeline Workflow**: Provides complete variant calling pipeline.

- **Viral Genomics**: Specialized for viral genome analysis.

- **Consensus Sequence**: Generates consensus sequences.

- **Mutation Detection**: Detects mutations in viral genomes.

- **Phylogenetic Analysis**: Supports downstream phylogenetic analysis.

## Pitfalls

- **Data Quality**: Results depend on sequencing data quality.

- **Reference Genome**: Ensure using correct reference genome.

- **Sample Contamination**: Account for potential sample contamination.

- **Computational Resources**: May require significant resources.

- **Data Format**: Ensure correct input format.

## Examples

### Call variants
**Args:** `harvest-variants --reads reads.fastq --reference reference.fasta --output variants.vcf`
**Explanation:** Calls variants from SARS-CoV-2 sequencing data.

### Generate consensus
**Args:** `harvest-variants --reads reads.fastq --reference reference.fasta --consensus --output consensus.fasta`
**Explanation:** Generates consensus sequence from reads.

### Batch processing
**Args:** `for f in *.fastq; do harvest-variants --reads $f --reference reference.fasta --output ${f%.fastq}_variants.vcf; done`
**Explanation:** Processes multiple sequencing files.

### Generate report
**Args:** `harvest-variants --reads reads.fastq --reference reference.fasta --report --output report.html`
**Explanation:** Generates comprehensive analysis report.

### Quality filtering
**Args:** `harvest-variants --reads reads.fastq --reference reference.fasta --min-quality 30 --output variants.vcf`
**Explanation:** Filters variants by quality score.

### Phylogenetic tree
**Args:** `harvest-variants --reads reads.fastq --reference reference.fasta --tree --output tree.nwk`
**Explanation:** Generates phylogenetic tree from sequences.

### Help command
**Args:** `harvest-variants --help`
**Explanation:** Shows available options and usage information.