---
name: biobloomtools
category: alignment
description: Build Bloom filters and use them for categorizing sequences
tags: [bloom-filter, sequence-categorization, contamination-screening]
author: oxo-call-community
source_url: "https://github.com/bcgsc/biobloom"
---

## Concepts
- **Tool Overview**: BioBloomTools creates Bloom filters from reference sequences and uses them to rapidly categorize or filter sequencing reads by origin.
- **Bloom Filters**: Probabilistic data structure for efficient set membership testing with minimal memory.
- **Applications**: Contamination screening, read binning by organism, metagenomics sample characterization.
- **Workflow**: Build Bloom filter from references → categorize reads → filter or bin reads.

## Pitfalls
- **False Positives**: Bloom filters have inherent false positive rate; critical applications require validation.
- **Filter Size**: Larger filters have lower false positive rates but use more memory.
- **Reference Dependency**: Can only categorize reads from organisms represented in the Bloom filter.

## Examples
### Create Bloom filter from reference
**Args:** `biobloomtools-maker -p human -i human_ref.fa -o filters/`
**Explanation:** Creates a Bloom filter named "human" from reference sequences.

### Categorize reads
**Args:** `biobloomtools-categorizer -p filters/ -i reads.fq -o categorized/`
**Explanation:** Categorizes reads based on Bloom filter matches.

### Filter reads
**Args:** `biobloomtools-filter -p filters/human.bf -i reads.fq -o human_reads.fq`
**Explanation:** Filters reads matching the human Bloom filter.
