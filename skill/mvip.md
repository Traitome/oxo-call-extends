---
name: mvip
category: metagenomics
description: MVP pipeline for standard viromics analyses combining multiple tools for viral genome identification, annotation, and binning
tags: [mvip, metagenomics, viromics, viral, annotation, binning, viral-genome]
author: oxo-call-community
source_url: "https://gitlab.com/ccoclet/mvp"
---

## Concepts

- **Tool Overview**: MVP (Metagenomic Virome Pipeline) v1.1.5 is a comprehensive pipeline for analyzing viral metagenomics data. It integrates multiple tools for viral sequence identification, genome annotation, taxonomic clustering, and genome binning from complex metagenomic samples.
- **Core Function**: Takes assembled metagenomic contigs as input, identifies viral sequences, annotates viral genes, clusters related viral genomes, and produces bins representing distinct viral populations.
- **Workflow**: Combines existing tools (DIAMOND, HMMER, CheckV, and others) into a unified pipeline. Handles the complete viromics workflow from contigs to characterized viral genomes.
- **Input Format**: Expects pre-assembled contigs in FASTA format from metagenomic or virome sequencing. Can also accept direct FASTQ input with built-in assembly options.
- **Output**: Provides identified viral contigs, annotated gene predictions, taxonomic assignments, genome bins with quality scores, and summary statistics in tabular format.
- **Use Case**: Environmental viromics, clinical virome studies, viral surveillance, and discovery of novel viruses in complex biological samples.

## Pitfalls

- **Contig Quality**: MVP works best with high-quality assemblies. Poor assemblies with fragmented contigs reduce viral detection sensitivity.
- **Viral Database**: Relies on reference viral databases for identification. Outdated databases may miss novel viruses. Consider updating databases before running.
- **Computational Time**: Full pipeline runs can take significant time for large datasets. Use checkpoint options if resuming interrupted runs.
- **Memory Requirements**: The pipeline is memory-intensive, especially during clustering steps. Ensure sufficient RAM for your dataset size.
- **Taxonomic Classification**: Viral taxonomy can be ambiguous. MVP uses multiple approaches for classification - review assignments critically.
- **Genome Binning**: Viral genome bins represent populations, not individual genomes. Bin quality and completeness estimates should be interpreted carefully.

## Examples

### Basic viromics analysis
**Args:** `-i contigs.fasta -o output_dir`
**Explanation:** Standard MVP pipeline run. Takes assembled contigs and produces viral identification, annotation, and binning results.

### Specify threads for parallel processing
**Args:** `-i viral_contigs.fa -o results/ -t 16`
**Explanation:** Uses 16 threads to speed up computation. Adjust based on available CPU resources.

### Use custom viral database
**Args:** `-i metagenome.fna -o results/ --db custom_viral_db.dmnd`
**Explanation:** Provides a custom DIAMOND database for viral sequence identification instead of the default database.

### Run only specific steps
**Args:** `-i contigs.fa -o output/ --steps identify,annotate`
**Explanation:** Runs only identification and annotation steps, skipping clustering and binning. Useful for quick surveys.

### Set minimum contig length
**Args:** `-i assembly.fa -o results/ --min-length 1000`
**Explanation:** Filters input contigs to those at least 1000bp before processing. Reduces runtime and focuses on potentially complete viral genomes.

### Generate quality report
**Args:** `-i contigs.fasta -o report/ --report`
**Explanation:** Generates a detailed quality report including statistics on viral identification rates, annotation completeness, and bin quality metrics.
