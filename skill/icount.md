---
name: icount
category: bioinformatics
description: Computational pipeline for analysis of iCLIP (individual-nucleotide resolution CrossLinking and ImmunoPrecipitation) data.
tags: [icount, bioinformatics, iCLIP, RNA-binding, protein-RNA-interaction]
author: oxo-call-community
source_url: "https://github.com/tomazc/iCount"
---

## Concepts

- **Tool Overview**: iCount (v2.0.0) is a comprehensive pipeline for processing iCLIP sequencing data to identify RNA-protein interaction sites at nucleotide resolution.
- **iCLIP Analysis**: Identifies cross-linked sites between RNA-binding proteins (RBPs) and their target RNAs.
- **STAR Integration**: Uses STAR aligner for mapping reads to reference genomes.
- **Quantification**: Counts unique cDNA molecules using randomer barcodes to measure interaction strength.
- **Peak Calling**: Identifies significantly cross-linked sites and clusters.
- **Installation**: `conda install -c bioconda icount`

## Pitfalls

- **Genome Index Requirements**: Requires pre-built STAR index for mapping.
- **Memory Intensive**: Whole-genome analysis requires significant RAM.
- **Barcode Handling**: Proper barcode design is critical for accurate deduplication.
- **Sequencing Depth**: Requires sufficient sequencing depth for reliable peak detection.
- **Reference Genome Quality**: Results depend on the completeness and annotation quality of the reference genome.
- **Cross-link Site Identification**: UV-induced mutations can affect mapping accuracy.

## Examples

### Download genome and annotation
**Args:** `iCount genome --source ensembl homo_sapiens -r 88 --chromosomes 21 MT`
**Explanation:** Downloads human genome sequence for specified chromosomes from Ensembl.

### Build STAR index
**Args:** `iCount indexstar genome.fa.gz star_index --annotation genes.gtf`
**Explanation:** Creates a STAR genome index for read mapping.

### Map iCLIP reads
**Args:** `iCount mapstar reads.fastq star_index --out mapping_results/`
**Explanation:** Maps sequencing reads to the genome using STAR.

### Quantify cross-link sites
**Args:** `iCount xlsites mapping_results/ crosslinks.bed --quant cDNA`
**Explanation:** Quantifies cross-linked sites using unique cDNA molecules.

### Identify significant peaks
**Args:** `iCount peaks crosslinks.bed peaks.bed --threshold 0.05`
**Explanation:** Identifies significantly cross-linked sites with FDR threshold of 0.05.