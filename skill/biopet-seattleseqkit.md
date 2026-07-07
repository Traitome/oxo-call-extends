---
name: biopet-seattleseqkit
category: variant-calling
description: Tools for processing SeattleSeq annotation files
tags: [seattleseq, variant-annotation, filtering, BED]
author: oxo-call-community
source_url: "https://github.com/biopet/seattleseqkit"
---

## Concepts

- **Tool Overview**: BioPet SeattleSeqKit provides tools for processing and filtering SeattleSeq annotation files, which contain variant annotation information.
- **Filtering**: Filters variants based on genomic regions (BED intervals) or specific annotation fields.
- **Annotation Processing**: Handles SeattleSeq-formatted variant annotation outputs.
- **Applications**: Variant filtering, annotation subsetting, region-based variant selection.

## Pitfalls

- **SeattleSeq Format**: Input must be in SeattleSeq annotation format.
- **BED Requirements**: BED files for region filtering must be properly formatted.

## Examples

### Filter by region
**Args:** `java -jar SeattleSeqKit.jar filter -i seattleseq.tsv -b regions.bed -o filtered.tsv`
**Explanation:** Filters SeattleSeq file to include only variants within specified BED regions.

### Filter by field
**Args:** `java -jar SeattleSeqKit.jar filter -i seattleseq.tsv -f "SIFT<0.05" -o filtered.tsv`
**Explanation:** Filters variants based on specific annotation field criteria.

### Merge annotations
**Args:** `java -jar SeattleSeqKit.jar merge -i file1.tsv -i file2.tsv -o merged.tsv`
**Explanation:** Merges multiple SeattleSeq annotation files.