---
name: batvi
category: utility
description: BATVI - Detection of viral integrations in host genomes
tags: [batvi, utility, viral-integration, bioinformatics]
author: oxo-call-community
source_url: "https://www.comp.nus.edu.sg/~bioinfo/batvi/"
---

## Concepts

- **Tool Overview**: BATVI (v1.04) detects viral integrations in host genomes, identifying sites where viral DNA has integrated into the host chromosome.
- **Core Function**: Identifies viral integration sites in host genome sequencing data.
- **Integration Detection**: Scans sequencing reads for chimeric reads spanning viral-host junctions.
- **Breakpoint Identification**: Pinpoints exact integration breakpoints between viral and host sequences.
- **Validation**: Validates integration sites using paired-end read information.
- **Input/Output**: Accepts BAM/SAM files; outputs integration site coordinates and annotations.
- **Installation**: `conda install -c bioconda batvi`.

## Pitfalls

- **Reference Databases**: Requires viral and host reference sequences for comparison.
- **Read Coverage**: Requires sufficient read coverage at integration sites for detection.
- **False Positives**: May produce false positive calls in repetitive genomic regions.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Detect viral integrations
**Args:** `batvi -b alignments.bam -v viral_ref.fasta -o integrations.txt`
**Explanation:** Detects viral integration sites from aligned sequencing reads.

### Specify host reference
**Args:** `batvi -b alignments.bam -v viral_ref.fasta -h host_ref.fasta -o integrations.txt`
**Explanation:** Uses host reference for more accurate integration site mapping.

### Filter by quality
**Args:** `batvi -b alignments.bam -v viral_ref.fasta -q 30 -o integrations.txt`
**Explanation:** Filters integration sites by mapping quality threshold.

### Annotate integrations
**Args:** `batvi -b alignments.bam -v viral_ref.fasta -a annotations.gff -o integrations.txt`
**Explanation:** Annotates integration sites with genomic features.

### Output in BED format
**Args:** `batvi -b alignments.bam -v viral_ref.fasta --bed -o integrations.bed`
**Explanation:** Outputs integration sites in BED format for genome browsers.

### Verbose mode
**Args:** `batvi -b alignments.bam -v viral_ref.fasta -v -o integrations.txt`
**Explanation:** Provides detailed output including supporting reads.

### Display help
**Args:** `batvi --help`
**Explanation:** Shows all available command-line options and usage information.