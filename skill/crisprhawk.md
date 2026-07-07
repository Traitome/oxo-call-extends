---
name: crisprhawk
category: genome-editing
description: Haplotype and variant-aware guide RNA design tool for CRISPR-Cas systems considering population genetic variation
tags: [crisprhawk, CRISPR, guide-RNA, haplotype, variant, PAM, genome-editing, gRNA, Cas9, Cpf1]
author: oxo-call-community
source_url: "https://github.com/pinellolab/CRISPR-HAWK"
---

## Concepts

- **Tool Overview**: CRISPR-HAWK (v0.2.2) - Haplotype and vAriant-aWare guide design toolKit for CRISPR-Cas systems.
- **Core Function**: Designs, scores, and annotates CRISPR guide RNAs while accounting for real human genetic variation using population databases (1000 Genomes, HGDP, gnomAD). Integrates variant-aware search, functional annotation, and haplotype reconstruction.
- **Algorithm**: (1) Extracts target regions from reference genome. (2) Rebuilds haplotypes using variant data (phased variants produce distinct sequences, unphased use IUPAC codes). (3) Binary-encodes haplotype sequences for efficient scanning. (4) Identifies candidate guides with variant-aware PAM detection. (5) Scores guides for efficiency and off-target potential.
- **Input**: Reference genome (FASTA), target regions (BED), PAM motif, spacer length, optional VCF for variants, optional BED annotation files.
- **Output**: Ranked guide tables, annotated sequences, graphical reports showing variant effects on guide efficiency.
- **Application**: Therapeutic guide selection, clinical trial off-target safety, population genomics in gene editing, personalized CRISPR design.
- **Installation**: `conda install -c bioconda crisprhawk` or `pip install crisprhawk`

## Pitfalls

- **Reference Only Off-Target**: Off-target estimation currently only works against the reference genome, not variant/haplotype-aware.
- **External Dependencies**: CRISPRitz for off-target analysis must be installed separately.
- **Memory Requirements**: Large genome-scale operations may need high memory/compute resources.
- **VCF Filter**: By default only includes FILTER=PASS variants; use `--no-filter` to include all variants.
- **PAM Compatibility**: Different Cas systems require different PAM sequences (SpCas9=NGG, SaCas9=NNGRRT, Cpf1=TTTN).

## Examples

### Basic guide search
**Args:** `crisprhawk search -r GRCh38.fa -b targets.bed -p NGG -l 20 -o output/`
**Explanation:** Search for Cas9 guides in target regions using standard NGG PAM and 20bp spacer length.

### Variant-aware search with population data
**Args:** `crisprhawk search -r GRCh38.fa -b targets.bed -p NGG -l 20 -v variants.vcf -o output/`
**Explanation:** Include variant information to identify guides that work across different haplotypes.

### Haplotype-aware processing
**Args:** `crisprhawk search -r GRCh38.fa -b targets.bed -p NGG -l 20 --haplotype-table -o output/`
**Explanation:** Generate TSV files reporting haplotype-aware variants and associated guide matches per haplotype.

### Multi-threaded search
**Args:** `crisprhawk search -r GRCh38.fa -b targets.bed -p NGG -l 20 -t 8 -o output/`
**Explanation:** Use 8 threads for parallel processing; use `-t 0` for all available cores.

### Annotate guides with genomic features
**Args:** `crisprhawk search -r GRCh38.fa -b targets.bed -p NGG -l 20 --annotation features.bed --annotation-colnames chrom,start,end,name -o output/`
**Explanation:** Add functional annotations to guide results using custom BED file with column names.

### Generate graphical reports
**Args:** `crisprhawk search -r GRCh38.fa -b targets.bed -p NGG -l 20 --graphical-reports -o output/`
**Explanation:** Create pie charts of guide-type distribution and delta plots showing effect of genetic diversity on guide efficiency.

### Compute elevation score
**Args:** `crisprhawk search -r GRCh38.fa -b targets.bed -p NGG -l 20 --compute-elevation-score -o output/`
**Explanation:** Calculate Elevation and Elevation-On scores for guide efficiency when combined guide + PAM = 23bp and guide is downstream of PAM.
