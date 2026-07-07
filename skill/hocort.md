---
name: hocort
category: preprocessing
description: HoCoRT (Host Contamination Removal Tool) efficiently removes host sequences from sequencing data to improve downstream analysis accuracy.
tags: [hocort, host-contamination, metagenomics, sequencing-preprocessing, microbiome]
author: oxo-call-community
source_url: "https://github.com/ignasrum/hocort"
---

## Concepts

- **Tool Overview**: HoCoRT (v1.2.2) is an open-source command-line tool for removing host contamination from sequencing data. It is designed to be simple to install and use, with built-in genome indexing capabilities.

- **Classification Methods**: HoCoRT integrates multiple alignment and classification methods including Bowtie2, Minimap2, and k-mer based approaches, allowing users to choose the best method for their data type.

- **Short vs Long Read Support**: Optimized for both short-read (Illumina) and long-read (Nanopore/PacBio) sequencing data. Bowtie2 in end-to-end mode is recommended for Illumina, while Minimap2 performs best for Nanopore.

- **Privacy Protection**: Removes human host sequences to comply with privacy regulations when working with human-derived samples.

- **Modular Design**: Built as a modular pipeline that can be integrated into larger bioinformatics workflows. Supports custom reference genomes for host removal.

- **Performance**: Significantly faster than traditional tools like DeconSeq while maintaining high accuracy in host sequence removal.

## Pitfalls

- **Reference Genome Quality**: The effectiveness of host removal depends heavily on the quality and completeness of the host reference genome. Use well-annotated, complete genomes for best results.

- **Memory Requirements**: Building genome indexes can be memory-intensive, especially for large eukaryotic genomes. Ensure sufficient RAM is available.

- **Choice of Algorithm**: Selecting the wrong algorithm for your data type (short vs long reads) can reduce efficiency. Use Bowtie2 for Illumina, Minimap2 for Nanopore.

- **Cross-Contamination**: Ensure no cross-contamination between samples during sequencing, as this cannot be corrected computationally.

- **Sensitivity vs Specificity**: Adjust parameters based on whether you need high sensitivity (remove all potential host) or high specificity (minimize false positives).

- **Paired-End Reads**: For paired-end data, ensure both reads are processed consistently to maintain read pairing information.

## Examples

### Index a host genome
**Args:** `hocort index -i host_genome.fasta -o host_index/ -b bowtie2`
**Explanation:** Creates a Bowtie2 index for the host genome, enabling fast alignment during contamination removal.

### Remove host from paired-end Illumina data
**Args:** `hocort decontaminate -1 reads_1.fastq -2 reads_2.fastq -i host_index/ -o clean_reads_%.fastq`
**Explanation:** Removes host sequences from paired-end Illumina reads, outputting cleaned reads while preserving pairing.

### Remove host from Nanopore long reads
**Args:** `hocort decontaminate -s nanopore_reads.fastq -i host_index/ -o clean_nanopore.fastq -a minimap2`
**Explanation:** Uses Minimap2 algorithm optimized for long reads to remove host contamination from Nanopore data.

### Remove human host for privacy compliance
**Args:** `hocort decontaminate -1 reads_1.fastq -2 reads_2.fastq -i human_index/ -o clean_%.fastq -p`
**Explanation:** Removes human sequences to comply with privacy regulations before sharing or analyzing microbiome data.

### Decontaminate single-end reads
**Args:** `hocort decontaminate -s single_end.fastq -i host_index/ -o clean_single.fastq`
**Explanation:** Processes single-end sequencing data, removing host sequences efficiently.

### Generate decontamination report
**Args:** `hocort decontaminate -1 reads_1.fastq -2 reads_2.fastq -i host_index/ -o clean_%.fastq -r report.txt`
**Explanation:** Outputs a report with statistics including percentage of host sequences removed.

### Use custom sensitivity settings
**Args:** `hocort decontaminate -1 reads_1.fastq -2 reads_2.fastq -i host_index/ -o clean_%.fastq -sensitive`
**Explanation:** Runs in high-sensitivity mode to capture more host sequences, useful for samples with high contamination rates.