---
name: extracthifi
category: utility
description: "PacBio utility to extract HiFi reads from CCS reads"
tags: [extracthifi, utility, PacBio, HiFi, long-reads]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/extracthifi"
---

## Concepts

- **Tool Overview**: extracthifi is a PacBio utility for extracting HiFi (High-Fidelity) reads from Circular Consensus Sequence (CCS) reads.
- **Core Function**: Filters CCS reads to identify and extract high-quality HiFi reads based on quality thresholds.
- **Input/Output**: Input: CCS reads (FASTQ/BAM). Output: HiFi reads (FASTQ/BAM), quality reports.
- **Algorithm**: Uses quality scores and read statistics to filter and extract HiFi reads from CCS data.
- **Key Features**: HiFi read extraction, quality filtering, support for multiple formats, batch processing, quality reporting.
- **Installation**: `conda install -c bioconda extracthifi`

## Pitfalls

- **Quality Thresholds**: Default thresholds may need adjustment for specific datasets.
- **Read Coverage**: Requires sufficient coverage for reliable HiFi extraction.
- **Format Compatibility**: Requires specific input formats from PacBio sequencing.
- **Computation Resources**: Large datasets require significant computational resources.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic HiFi extraction
**Args:** `extracthifi -i ccs_reads.fastq -o hifi_reads.fastq`
**Explanation:** Extracts HiFi reads from CCS reads.

### From BAM file
**Args:** `extracthifi -i ccs_reads.bam -o hifi_reads.bam --bam`
**Explanation:** Processes CCS reads from BAM file.

### With quality threshold
**Args:** `extracthifi -i ccs_reads.fastq -o hifi_reads.fastq --min-quality 99`
**Explanation:** Extracts HiFi reads with minimum quality score of 99.

### Generate report
**Args:** `extracthifi -i ccs_reads.fastq -o hifi_reads.fastq --report report.txt`
**Explanation:** Generates quality report for extracted reads.

### Batch processing
**Args:** `extracthifi -i ccs_reads/ -o hifi_reads/ --batch`
**Explanation:** Processes multiple CCS files in batch mode.