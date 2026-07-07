---
name: neodisambiguate
category: alignment
description: NeoDisambiguate disambiguates reads that were mapped to multiple references.
tags: [neodisambiguate, alignment, mapping, reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/clintval/neodisambiguate"
---

## Concepts

- **Tool Overview**: NeoDisambiguate resolves ambiguous read mappings across multiple references.
- **Core Function**: Determines which reference a read originated from when mapped to multiple references.
- **Algorithm**: Uses mapping quality and sequence similarity to disambiguate reads.
- **Input Format**: Accepts BAM files with reads mapped to multiple references.
- **Output**: Produces disambiguated BAM files and statistics.
- **Use Case**: Mixed-sample sequencing, metagenomics, and hybrid genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Mapping Quality**: Results depend on input mapping quality.
- **Reference Similarity**: Struggles with highly similar references.
- **Memory Usage**: Processing large BAM files requires memory.
- **Ambiguity Threshold**: Requires careful threshold setting.
- **Format Compatibility**: Requires properly formatted BAM files.

## Examples

### Display help
**Args:** `neodisambiguate --help`
**Explanation:** Shows available options and usage instructions.

### Basic disambiguation
**Args:** `neodisambiguate -i input.bam -o output.bam`
**Explanation:** Disambiguates reads in BAM file.

### Multiple references
**Args:** `neodisambiguate -i input.bam -r ref1.fasta ref2.fasta -o output.bam`
**Explanation:** Uses multiple reference sequences for disambiguation.

### Quality threshold
**Args:** `neodisambiguate -i input.bam -q 30 -o output.bam`
**Explanation:** Sets minimum mapping quality threshold to 30.

### Output statistics
**Args:** `neodisambiguate -i input.bam -o output.bam -s stats.tsv`
**Explanation:** Outputs disambiguation statistics.

### Filter ambiguous
**Args:** `neodisambiguate -i input.bam --filter-ambiguous -o output.bam`
**Explanation:** Filters out ambiguous reads.

### Paired-end mode
**Args:** `neodisambiguate -i input.bam --paired-end -o output.bam`
**Explanation:** Processes paired-end reads.