---
name: kneaddata
category: qc
description: Quality control tool for metagenomic sequencing data - removes host contamination
tags: [kneaddata, qc, metagenomics, host-contamination, quality-control]
author: oxo-call-community
source_url: "https://huttenhower.sph.harvard.edu/kneaddata"
---

## Concepts

- **Host Read Removal**: Removes host DNA contamination from metagenomic data
- **Quality Control**: Performs quality control on microbiome sequencing data
- **Reference Database**: Uses host reference genomes for contamination removal
- **Paired-end Support**: Handles both single-end and paired-end reads
- **Multiple Databases**: Can filter against multiple reference databases
- **Standardized Workflow**: Integrates with bioBakery workflows

## Pitfalls

- **Reference Quality**: Incomplete reference genomes miss contamination
- **Database Size**: Large reference databases slow processing
- **Sequence Similarity**: Host genes in microbes cause false positives
- **Memory Usage**: Large databases require significant memory
- **Threading**: Parallelization may cause memory issues
- **Adapter Trimming**: May over-trim if adapter sequences are misidentified

## Examples

### Remove host contamination
**Args:** `kneaddata --input reads_1.fastq --input reads_2.fastq --reference human_genome -o output/`
**Explanation:** Removes human reads from paired-end metagenomic data.

### Single-end mode
**Args:** `kneaddata --input reads.fastq --reference human_genome -o output/`
**Explanation:** Processes single-end reads.

### Multiple databases
**Args:** `kneaddata --input reads.fastq --reference human_db --reference mouse_db -o output/`
**Explanation:** Removes contamination from multiple host species.

### With quality filtering
**Args:** `kneaddata --input reads_1.fastq --input reads_2.fastq --reference hg38 --trimmomatic -o output/`
**Explanation:** Removes host reads and trims adapters.

### Batch processing
**Args:** `kneaddata --input-list samples.txt --reference hg38 -o results/`
**Explanation:** Processes multiple samples from a list.

### Output statistics
**Args:** `kneaddata --input reads_1.fastq --input reads_2.fastq --reference hg38 -o output/ --output-log`
**Explanation:** Generates detailed processing statistics.