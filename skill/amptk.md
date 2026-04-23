---
name: amptk
category: metagenomics
description: AMPtk - Amplicon ToolKit for processing high-throughput amplicon/metabarcoding sequencing data
tags: [amplicon, metabarcoding, its, 16s, otu, dada2, fungi, bacteria]
author: oxo-call-community
source_url: "https://github.com/nextgenusfs/amptk"
---

## Concepts

- **Tool Overview**: AMPtk is a toolkit for processing NGS amplicon data using VSEARCH/DADA2. Supports fungal ITS, bacterial 16S, insect COI, and other metabarcoding markers. Version 1.6.0.
- **Pipeline Stages**: Pre-processing (demux, quality filtering) → Clustering/Denoising (OTU/ASV) → Taxonomy assignment → Community analysis.
- **Denoising Options**: Supports both OTU clustering (VSEARCH) and ASV denoising (DADA2) approaches. DADA2 provides single-nucleotide resolution.
- **Spike-In Controls**: Integrates synthetic spike-in controls for improved quantitative accuracy in mycobiome studies.
- **Database Support**: Built-in databases for UNITE (fungi), SILVA (bacteria), COI (insects). Custom databases also supported.
- **LULU Integration**: Post-clustering curation using LULU algorithm to reduce spurious OTUs from sequencing errors.
- **Output Formats**: Produces BIOM tables, FASTA files, phyloseq-compatible R objects for downstream statistical analysis.

## Pitfalls

- **VSEARCH Required**: VSEARCH must be installed and in PATH. No longer requires USEARCH (since v1.5.1).
- **Memory Usage**: Large datasets may exceed 4GB RAM limit of 32-bit USEARCH. Use VSEARCH (64-bit) to avoid this limitation.
- **DADA2 Installation**: DADA2 requires R and Bioconductor installation. Complex setup on some systems.
- **Database Downloads**: Built-in taxonomy databases require initial download. First run may be slow.
- **Primer Sequences**: Must provide correct primer sequences for your amplicon panel. Wrong primers cause failed demultiplexing.
- **Quality Thresholds**: Default quality thresholds may need adjustment for different sequencing platforms (Illumina vs Ion Torrent).

## Examples

### Illumina preprocessing workflow
**Args:** `amptk illumina -i demux.fastq.gz -o output -f ITS3 -r ITS4 --rescue_forward --min_len 100`
**Explanation:** Full Illumina preprocessing: quality filtering, primer removal, merging. Uses ITS3/ITS4 primers for fungal ITS. Rescue forward reads for non-overlapping amplicons.

### DADA2 denoising
**Args:** `amptk dada2 -i filtered.fastq.gz -o dada2_output --pool`
**Explanation:** Runs DADA2 denoising algorithm for ASV-level resolution. Pooled mode (--pool) increases sensitivity for rare variants. Produces ASV table and representative sequences.

### OTU clustering with VSEARCH
**Args:** `amptk cluster -i filtered.fastq.gz -o otu_output --otu_method vsearch --identity 0.97`
**Explanation:** OTU clustering at 97% identity using VSEARCH. Standard approach for fungal ITS and bacterial 16S. Produces OTU table and representative sequences.

### Taxonomy assignment with UNITE
**Args:** `amptk taxonomy -i otu_table.txt -f otus.fasta -d UNITE -o taxonomy_results`
**Explanation:** Assigns taxonomy using UNITE database for fungal ITS sequences. Outputs taxonomy table with species-level assignments when possible.

### LULU post-clustering curation
**Args:** `amptk lulu -i otu_table.txt -f otus.fasta -o lulu_output --min_ratio 2`
**Explanation:** Applies LULU algorithm to curate OTU table by merging spurious OTUs with their parent. Minimum ratio of 2 between parent and daughter OTU abundances.

### Community statistics
**Args:** `amptk stats -i final_otu_table.txt -t taxonomy.txt -o stats_output`
**Explanation:** Generates community ecology statistics: alpha diversity, beta diversity, ordination plots. Produces phyloseq-compatible R objects for further analysis.

### Process Ion Torrent data
**Args:** `amptk ion -i input.fastq -o output -f fITS7 -r ITS4 --min_len 150`
**Explanation:** Processes Ion Torrent amplicon data with fITS7/ITS4 primers. Ion Torrent-specific quality filtering applied. Minimum read length 150bp.

### Custom database taxonomy
**Args:** `amptk taxonomy -i otu_table.txt -f otus.fasta -d /path/to/custom_db.fasta -o custom_taxonomy`
**Explanation:** Uses custom taxonomy database instead of built-in databases. Database must be formatted for AMPtk compatibility.