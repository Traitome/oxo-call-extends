---
name: ariba
category: annotation
description: ARIBA - Antimicrobial Resistance Identification By Assembly using targeted local assembly and alignment
tags: [amr, antibiotic-resistance, assembly, genotyping, bacteria, pathogens]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/ariba"
---

## Concepts

- **Tool Overview**: ARIBA (Antimicrobial Resistance Identification By Assembly) identifies antimicrobial resistance genes using combined mapping/alignment and targeted local assembly. Version 2.14.7.
- **Targeted Assembly**: Assembles reads matching known resistance genes rather than whole genome. More accurate than direct mapping for divergent alleles.
- **Database Support**: Works with custom resistance gene databases or curated databases (CARD, ResFinder, etc.). Database preparation required before analysis.
- **Variant Detection**: Identifies both presence/absence of resistance genes and specific variants/mutations within genes. Important for resistance level prediction.
- **Speed**: Faster than whole-genome assembly approaches. Targeted assembly of resistance genes only reduces computational burden.
- **Quality Filtering**: Built-in quality filters for assembly and variant calling. Reports confidence metrics for each detection.
- **Batch Processing**: Can process multiple samples efficiently. Suitable for surveillance and outbreak monitoring.

## Pitfalls

- **Database Preparation**: Requires database preprocessing with `ariba prepareref`. Cannot use raw FASTA databases directly.
- **Coverage Requirements**: Low coverage (<10x) of resistance genes reduces assembly quality and variant detection accuracy.
- **Novel Variants**: Novel resistance mechanisms not in database will be missed. Update database regularly with new resistance genes.
- **Gene Similarity**: Highly similar resistance genes may be misassigned. Verify assignments for gene families with high similarity.
- **Partial Genes**: Partial resistance genes (truncated by assembly boundaries) may be missed or incorrectly reported.
- **Mixed Populations**: Heterogeneous samples with multiple resistance alleles may produce ambiguous results.

## Examples

### Prepare resistance gene database
**Args:** `ariba prepareref --gene_db resistance_genes.fasta --outdir prepared_db/`
**Explanation:** Preprocesses resistance gene database for ARIBA analysis. Required before running genotyping. Creates indexed reference files.

### Run AMR genotyping
**Args:** `ariba run --outdir results/ prepared_db/ reads_1.fastq.gz reads_2.fastq.gz`
**Explanation:** Basic genotyping workflow. Uses prepared database to identify resistance genes in paired-end reads. Outputs presence/absence and variants.

### Use CARD database
**Args:** `ariba prepareref --card CARD.fasta --outdir card_db/; ariba run --outdir results/ card_db/ reads_1.fq.gz reads_2.fq.gz`
**Explanation:** Uses curated CARD (Comprehensive Antibiotic Resistance Database) for genotyping. Recommended for comprehensive resistance profiling.

### Process single-end reads
**Args:** `ariba run --outdir results/ prepared_db/ reads.fastq.gz`
**Explanation:** Single-end read processing. Slightly reduced accuracy compared to paired-end but works for legacy data or single-end sequencing.

### Batch process multiple samples
**Args:** `for s in samples/*_1.fq.gz; do ariba run --outdir "results/${s%_1.fq.gz}" prepared_db/ "$s" "${s%_1.fq.gz}_2.fq.gz"; done`
**Explanation:** Processes multiple samples in directory. Outputs separate result directories for each sample. Useful for surveillance studies.

### Generate summary report
**Args:** `ariba summary --outdir summary_results/ results/sample1 results/sample2 results/sample3`
**Explanation:** Combines results from multiple samples into summary report. Shows resistance gene presence across all samples. Useful for comparative analysis.

### Custom variant thresholds
**Args:** `ariba run --outdir results/ --min_coverage 20 --min_identity 0.95 prepared_db/ reads_1.fq.gz reads_2.fq.gz`
**Explanation:** Sets minimum coverage 20x and identity 95% for gene detection. Stricter thresholds reduce false positives but may miss genuine low-coverage genes.