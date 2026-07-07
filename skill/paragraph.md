---
name: paragraph
category: variant-calling
description: Paragraph provides graph realignment tools for structural variant analysis.
tags: [paragraph, variant-calling, structural-variants, graph-realignment]
author: oxo-call-community
source_url: "https://github.com/Illumina/paragraph"
---

## Concepts

- **Tool Overview**: Paragraph performs graph-based realignment for SV analysis.
- **Core Function**: Realigns reads to graph representations of variants.
- **Algorithm**: Uses graph alignment for structural variant detection.
- **Input Format**: Accepts BAM files and VCF variants.
- **Output**: Produces realigned BAM and variant calls.
- **Use Case**: Structural variant calling, genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Graph Complexity**: Complex graphs may affect performance.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paragraph --help`
**Explanation:** Shows available options and usage instructions.

### Build graph
**Args:** `paragraph build -r reference.fasta -v variants.vcf -o graph/`
**Explanation:** Builds graph from reference and variants.

### Realign reads
**Args:** `paragraph realign -g graph/ -i reads.bam -o realigned.bam`
**Explanation:** Realigns reads to graph.

### Call variants
**Args:** `paragraph call -g graph/ -i realigned.bam -o sv_calls.vcf`
**Explanation:** Calls structural variants.

### Verbose mode
**Args:** `paragraph realign -v -g graph/ -i reads.bam -o realigned.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `paragraph realign -t 16 -g graph/ -i reads.bam -o realigned.bam`
**Explanation:** Uses 16 threads for parallel processing.

### Output stats
**Args:** `paragraph stats -i realigned.bam -o stats.txt`
**Explanation:** Generates alignment statistics.