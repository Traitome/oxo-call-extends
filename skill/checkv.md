---
name: checkv
category: qc
description: Assess the quality of metagenome-assembled viral genomes
tags: [checkv, viral-genome, quality, completeness, contamination, provirus, metagenomics]
author: oxo-call-community
source_url: "https://bitbucket.org/berkeleylab/checkv"
---

## Concepts

- **Tool Overview**: CheckV is a fully automated pipeline for assessing the quality of single-contig viral genomes from metagenomes, including completeness estimation and host contamination removal.
- **Core Function**: Evaluates viral genome completeness, identifies closed genomes, removes host contamination from proviruses, and classifies genome quality tiers.
- **Input/Output**: Input: FASTA file of viral contigs. Output: Quality summary TSV, filtered genomes, and completeness estimates.
- **Quality Tiers**: Classifies genomes into 4 tiers: Complete (>90% completeness), High-quality (~50-90%), Medium-quality (~20-50%), Low-quality (<20%).
- **Three Modules**: `end_to_end` (full pipeline), `contamination` (host removal), `completeness` (genome completeness estimation).
- **Database**: Requires reference database with viral and microbial genomes. Download with `checkv download_db`.

## Pitfalls

- **Database Required**: Must download reference database before use. Can be large (~10GB).
- **Provirus Detection**: CheckV identifies and trims host regions from integrated proviruses, which may alter contig boundaries.
- **Completeness Estimation**: Based on comparison to complete viral genomes; novel viruses without close references may have unreliable estimates.
- **Single-Contig Only**: Designed for viral contigs, not fragmented genome bins. Use CheckM2 for cellular genome bins.
- **Amino Acid Genes**: Uses gene prediction (Prodigal) internally. Ensure input is nucleotide FASTA.

## Examples

### Full end-to-end pipeline
**Args:** `end_to_end input_viruses.fna output_dir/ -d /path/to/checkv_db -t 8`
**Explanation:** Runs the complete CheckV pipeline: contamination removal, completeness estimation, and quality classification using 8 threads.

### Estimate completeness only
**Args:** `completeness input_viruses.fna output_dir/ -d /path/to/checkv_db -t 8`
**Explanation:** Only estimates genome completeness without removing host contamination.

### Remove host contamination
**Args:** `contamination input_viruses.fna output_dir/ -d /path/to/checkv_db -t 8`
**Explanation:** Identifies and removes host regions from proviruses, producing cleaned viral sequences.

### Download database
**Args:** `download_db /path/to/checkv_db`
**Explanation:** Downloads the CheckV reference database to the specified directory.

### Assess quality with custom gene predictions
**Args:** `end_to_end input_viruses.fna output_dir/ -d /path/to/checkv_db --genes gene_predictions.gff`
**Explanation:** Uses pre-computed gene predictions instead of running Prodigal internally.

### Filter low-quality genomes
**Args:** `end_to_end input_viruses.fna output_dir/ -d /path/to/checkv_db --min_completeness 50`
**Explanation:** Only retains genomes with at least 50% estimated completeness in the filtered output.

### Run with reduced memory
**Args:** `end_to_end input_viruses.fna output_dir/ -d /path/to/checkv_db --lowmem`
**Explanation:** Reduces memory usage for DIAMOND searches, useful on memory-constrained systems.
