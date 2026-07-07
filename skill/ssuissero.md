---
name: ssuissero
category: typing
description: Rapid Streptococcus suis serotyping pipeline for Nanopore Data.
tags: [ssuissero, streptococcus, serotyping, nanopore]
author: oxo-call-community
source_url: "https://github.com/jimmyliu1326/SsuisSero"
---

## Concepts

- **Tool Overview**: ssuissero (v1.0.1) is a bioinformatics pipeline for rapid serotyping of Streptococcus suis from Nanopore sequencing data.
- **Core Function**: Identifies serotype-specific genes and determines the serotype of S. suis isolates.
- **Workflow Components**: Read filtering → mapping → gene detection → serotype prediction → report generation.
- **Input/Output**: Input: FASTQ files from Nanopore sequencing; Output: Serotype prediction report with confidence scores.
- **Serotype Database**: Uses curated database of S. suis serotype-specific genes for identification.
- **Installation**: `conda install -c bioconda ssuissero` or download from GitHub repository.

## Pitfalls

- **Sequencing Quality**: Low-quality Nanopore reads affect serotype calling accuracy.
- **Coverage Depth**: Insufficient coverage may miss serotype-specific genes.
- **Mixed Infections**: Multiple serotypes in sample produce ambiguous results.
- **Database Updates**: Outdated serotype database may miss newly discovered serotypes.
- **Contamination**: Host DNA contamination affects mapping and calling.
- **Assembly Required**: May require prior assembly for accurate serotyping.

## Examples

### Display help
**Args:** `ssuissero --help`
**Explanation:** Shows available options and usage information.

### Basic serotyping
**Args:** `ssuissero -i reads.fastq -o results/`
**Explanation:** Perform serotyping on Nanopore sequencing data.

### With assembly
**Args:** `ssuissero -i assembly.fasta -o results/ --assembly`
**Explanation:** Use pre-assembled genome for serotyping.

### Specify database
**Args:** `ssuissero -i reads.fastq -o results/ -d custom_db/`
**Explanation:** Use custom serotype database.

### Quality filtering
**Args:** `ssuissero -i reads.fastq -o results/ -q 10`
**Explanation:** Apply quality filter with minimum Phred score.

### Verbose mode
**Args:** `ssuissero -i reads.fastq -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Generate report
**Args:** `ssuissero -i reads.fastq -o results/ --report`
**Explanation:** Generate comprehensive HTML report.

### Multiple samples
**Args:** `ssuissero -i sample1.fastq sample2.fastq -o results/`
**Explanation:** Process multiple samples together.
