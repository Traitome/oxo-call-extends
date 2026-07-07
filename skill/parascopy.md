---
name: parascopy
category: variant-calling
description: ParaSCaller detects paralog-specific copy number and sequence variants.
tags: [parascopy, variant-calling, paralog, copy-number]
author: oxo-call-community
source_url: "https://github.com/tprodanov/parascopy"
---

## Concepts

- **Tool Overview**: ParaSCaller identifies variants in duplicated gene families.
- **Core Function**: Calls paralog-specific copy number and sequence variants.
- **Algorithm**: Uses short-read WGS data for variant detection.
- **Input Format**: Accepts FASTA, VCF, GFF, and BAM files.
- **Output**: Produces paralog-specific variant calls.
- **Use Case**: Gene family analysis, copy number variation, paralog studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Homology Complexity**: Complex gene families may affect accuracy.
- **Read Depth**: Requires sufficient sequencing depth.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parascopy --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `parascopy -i reads.bam -g genome.fasta -a genes.gff -o variants.vcf`
**Explanation:** Calls paralog-specific variants.

### Copy number only
**Args:** `parascopy -i reads.bam -g genome.fasta -o cnv.txt --cnv-only`
**Explanation:** Detects copy number variants only.

### Verbose mode
**Args:** `parascopy -v -i reads.bam -g genome.fasta -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `parascopy -t 8 -i reads.bam -g genome.fasta -o variants.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum quality
**Args:** `parascopy -q 30 -i reads.bam -g genome.fasta -o variants.vcf`
**Explanation:** Sets minimum base quality threshold.

### Output format
**Args:** `parascopy -i reads.bam -g genome.fasta -o variants.json --json`
**Explanation:** Outputs in JSON format.