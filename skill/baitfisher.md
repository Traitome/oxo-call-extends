---
name: baitfisher
category: utility
description: BaitFisher - Software package for designing hybrid enrichment probes
tags: [probe-design, hybrid-enrichment, bait-design, targeted-sequencing]
author: oxo-call-community
source_url: "https://github.com/cmayer/BaitFisher-package"
---

## Concepts

- **Tool Overview**: BaitFisher designs hybrid enrichment probes (baits) for targeted sequencing, optimizing probe placement across multiple species.

- **Cross-Species Design**: Designs baits that work across multiple related species by considering sequence conservation and variability.

- **Probe Optimization**: Optimizes probe length, melting temperature, and specificity for effective target capture.

- **Multiple Input Formats**: Accepts multiple sequence alignments or separate sequences as input.

## Pitfalls

- **Alignment Quality**: Requires high-quality multiple sequence alignment. Poor alignments lead to poor probe designs.

- **Specificity**: Baits may capture off-target sequences in complex genomes. Check specificity carefully.

- **Tm Optimization**: Melting temperature must be appropriate for capture conditions. Verify Tm calculations.

- **Coverage**: Ensure designed baits provide adequate coverage of target regions.

## Examples

### Basic bait design
**Args:** `BaitFisher --alignment targets.maf --output baits/`
**Explanation:** Designs hybrid enrichment probes from multiple alignment of target regions.

### Custom probe length
**Args:** `BaitFisher --alignment targets.maf --probe-length 120 --output baits/`
**Explanation:** Designs 120bp probes instead of default length.

### Specify target regions
**Args:** `BaitFisher --alignment targets.maf --regions regions.bed --output baits/`
**Explanation:** Designs baits only for specified genomic regions.

### Adjust melting temperature
**Args:** `BaitFisher --alignment targets.maf --min-tm 65 --max-tm 75 --output baits/`
**Explanation:** Designs probes with melting temperatures between 65-75°C.
