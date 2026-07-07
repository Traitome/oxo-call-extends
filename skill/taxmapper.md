---
name: taxmapper
category: metagenomics
description: Analysis pipeline for metagenomic microeukaryotic sequencing data.
tags: [taxmapper, metagenomics, microeukaryotes, pipeline]
author: oxo-call-community
source_url: "https://bitbucket.org/dbeisser/taxmapper"
---

## Concepts

- **Tool Overview**: taxmapper (v1.0.2) analyzes microeukaryotic metagenomics.
- **Core Function**: Taxonomic and functional analysis pipeline.
- **Algorithm**: Alignment and classification pipeline.
- **Input/Output**: Input: FASTQ reads; Output: Taxonomic profiles.
- **Applications**: Microeukaryote metagenomics, protist analysis.
- **Installation**: `conda install -c bioconda taxmapper` or BitBucket clone.

## Pitfalls

- **Database Coverage**: Limited to microeukaryotes.
- **Computational Time**: Complex pipeline is slow.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Poor quality affects analysis.
- **Contamination**: Requires careful contamination removal.
- **Parameter Tuning**: Multiple parameters need optimization.

## Examples

### Display help
**Args:** `taxmapper --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `taxmapper -i reads.fastq -o results/`
**Explanation:** Run full taxmapper pipeline.

### With reference
**Args:** `taxmapper -i reads.fastq -d database/ -o results/`
**Explanation:** Use custom reference database.

### Verbose mode
**Args:** `taxmapper -i reads.fastq -o results/ -v`
**Explanation:** Run with detailed logging.

### Output statistics
**Args:** `taxmapper -i reads.fastq -o results/ --stats`
**Explanation:** Generate comprehensive statistics.

### Skip QC
**Args:** `taxmapper -i reads.fastq -o results/ --skip-qc`
**Explanation:** Skip quality control step.

### Generate report
**Args:** `taxmapper -i reads.fastq -o results/ --report`
**Explanation:** Generate full analysis report.

### Export results
**Args:** `taxmapper -i reads.fastq -o results/ -f csv`
**Explanation:** Export results in CSV format.

### Paired-end data
**Args:** `taxmapper -i reads_1.fastq -j reads_2.fastq -o results/`
**Explanation:** Process paired-end reads.
