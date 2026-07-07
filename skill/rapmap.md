---
name: rapmap
category: alignment
description: RapMap provides rapid, sensitive, and accurate read mapping via quasi-mapping for transcript quantification.
tags: [rapmap, alignment, quasi-mapping, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/RapMap"
---

## Concepts

- **Tool Overview**: rapmap maps reads.
- **Core Function**: Read quasi-mapping.
- **Algorithm**: Uses quasi-mapping methods.
- **Input Format**: Accepts RNA-seq reads.
- **Output**: Produces alignment results.
- **Use Case**: RNA-seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Index Quality**: Affects mapping.
- **Parameters**: Must be configured.
- **Runtime**: Mapping may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rapmap --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `rapmap build -i transcripts.fasta -o index/`
**Explanation:** Builds quasi-mapping index.

### Map reads
**Args:** `rapmap map -i index/ -r reads.fastq -o alignments.sam`
**Explanation:** Maps reads using quasi-mapping.

### With parameters
**Args:** `rapmap map -i index/ -r reads.fastq -p params.yaml -o alignments.sam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rapmap -v map -i index/ -r reads.fastq -o alignments.sam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rapmap -t 4 map -i index/ -r reads.fastq -o alignments.sam`
**Explanation:** Uses 4 threads for parallel processing.

### Generate report
**Args:** `rapmap map -i index/ -r reads.fastq -o alignments.sam --report report.html`
**Explanation:** Generates HTML report.