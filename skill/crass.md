---
name: crass
category: assembly
description: CRISPR Assembler for identifying and reconstructing CRISPR loci from raw metagenomic data without assembly
tags: [crass, CRISPR, metagenomics, assembly, direct-repeats, spacers, phage-defense, microbial-immunity]
author: oxo-call-community
source_url: "https://github.com/ctSkennerton/crass"
---

## Concepts

- **Tool Overview**: crass (v1.0.1) - The CRISPR Assembler - a tool for identifying and reconstructing CRISPR loci from raw metagenomic data without the need for assembly or prior knowledge of CRISPR in the dataset.
- **Core Function**: Searches through genomic and metagenomic datasets to identify reads containing Clustered Regularly Interspersed Short Palindromic Repeats (CRISPR). Uses K-mer analysis to find repeated sequences of specific length separated by spacer sequences, then curates these to remove false positives.
- **Algorithm**: Identifies reads with repeated K-mers that are separated by spacer sequences at consistent lengths. These candidate direct repeats are curated to remove bad matches, then reads containing direct repeats are output for further analysis. Does not use assembly - works directly on unassembled reads.
- **Input**: FASTA or FASTQ files (can be gzipped). Read length must be between 76-2000 bp (supports Sanger, 454, Ion Torrent, and Illumina). Multiple input files can be processed simultaneously.
- **Output**: Group FASTA files (reads per CRISPR), Spacer Graphviz files (.gv), crass.crispr (XML with all CRISPR info), log files.
- **Application**: Metagenomic CRISPR identification, phage-host interaction analysis, microbial community adaptive immunity study, reconstructing CRISPR locus structure without assembly.
- **Installation**: `conda install -c bioconda crass` or `git clone https://github.com/ctSkennerton/crass.git`

## Pitfalls

- **Read Length Requirement**: Input reads must be between 76-2000 bp. Reads shorter than 76bp or longer than 2000bp will be ignored.
- **Paired-End Treatment**: Crass treats paired-end reads as unpaired - pairing information is not used. Both reads in a pair are processed independently.
- **Graph Visualization**: Crass outputs Graphviz (.gv) files which require external visualization tools like Gephi or graphviz to render as images.
- **crass-assembler Deprecated**: The crass-assembler wrapper for Velvet is no longer recommended. Use SPAdes or other modern assemblers instead, then use minced for CRISPR detection.
- **Output Interpretation**: Understanding spacer arrangement graphs requires knowledge of CRISPR locus structure (leader sequence, repeat direction, spacer ordering).
- **Log Verbosity**: Default logging is minimal. Use `-l` option to increase verbosity for debugging.

## Examples

### Basic usage with single file
**Args:** `SRX117744.fastq`
**Explanation:** Run crass on a single FASTQ file with default settings. Outputs files to current directory including Group FASTA files and spacer graph files.

### Run with multiple input files
**Args:** `SRX117744.1.fastq SRX117744.2.fastq`
**Explanation:** Process multiple FASTQ files simultaneously. All files are treated as unpaired and from the same source.

### Specify output directory and logging
**Args:** `-o crass_out -l 4 SRX117744.fastq`
**Explanation:** Output all results to directory `crass_out` (created automatically if not exists) and set log level to 4 for detailed logging information.

### Adjust direct repeat length range
**Args:** `-d 25 -D 50 reads.fastq`
**Explanation:** Set minimum direct repeat length to 25bp (-d) and maximum to 50bp (-D). Default range is 23-47bp. Adjust based on expected CRISPR repeat size in your sample.

### Adjust spacer length range
**Args:** `-s 30 -S 60 reads.fastq`
**Explanation:** Set minimum spacer length to 30bp (-s) and maximum to 60bp (-S). Default range is 26-50bp. Spacer length varies between organisms.

### Set minimum repeat count filter
**Args:** `-n 5 reads.fastq`
**Explanation:** Only consider CRISPR loci with at least 5 repeats (-n). Default is 3. Higher values reduce false positives but may miss real CRISPR arrays.

### Set minimum reads per CRISPR
**Args:** `-f 15 reads.fastq`
**Explanation:** Require at least 15 reads (-f) supporting a putative CRISPR to consider it real. Default is 10. Adjust based on sequencing depth.

### Remove homopolymer errors
**Args:** `-H reads.fastq`
**Explanation:** Enable homopolymer error correction (-H). Useful for Ion Torrent or 454 data where homopolymer indels are common. Applies scaling factors to spacer and repeat lengths.

### Adjust K-mer size for clustering
**Args:** `-k 15 reads.fastq`
**Explanation:** Set the number of K-mers two direct repeats must share to be considered part of the same cluster (-k). Default is 12. Higher values are more stringent.

### Adjust graph node length
**Args:** `-K 10 reads.fastq`
**Explanation:** Set K-mer length for defining graph nodes (-K). Default is 7. Lower values create more connected graphs but increase false positive edges.

### Custom graph coloring by coverage
**Args:** `-c green-red-blue reads.fastq`
**Explanation:** Use three-tone graph coloring where low coverage spacers are green and high coverage are blue (-c). Options include red-blue, blue-red, green-red-blue, red-blue-green.

### Show singletons in graph output
**Args:** `-G reads.fastq`
**Explanation:** Include unattached spacers in the graph output (-G). By default these are excluded.

### Display version
**Args:** `-V`
**Explanation:** Print version and copyright information and exit.

### Extract spacer sequences using crisprtools
**Args:** `crisprtools extract -s -g 111 crass_out/crass.crispr`
**Explanation:** After crass completes, use crisprtools to extract spacer sequences from group 111. Requires installation of crisprtools package separately.

### Assemble CRISPR with SPAdes
**Args:** `spades.py -o spades_out crass_out/Group_111*.fa`
**Explanation:** Take Group FASTA files from crass and assemble with SPAdes for more complete CRISPR reconstruction. Then use minced to identify CRISPR on assembled contigs.
