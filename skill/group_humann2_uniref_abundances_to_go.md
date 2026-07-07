---
name: group_humann2_uniref_abundances_to_go
category: bioinformatics
description: Converts HUMAnN2 UniRef50 gene family abundances to Gene Ontology (GO) slim terms with relative abundances.
tags: [group_humann2_uniref_abundances_to_go, GO, humann2, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ASaiM/group_humann2_uniref_abundances_to_GO"
---

## Concepts

- **GO Term Mapping**: Maps UniRef50 gene families to Gene Ontology terms.

- **Slim Terms**: Uses GO slim terms for simplified functional categorization.

- **Abundance Aggregation**: Aggregates gene family abundances by GO term.

- **Relative Abundance**: Calculates relative abundances for each GO term.

- **Functional Profiling**: Generates functional profiles of metagenomic communities.

- **Integration**: Works seamlessly with HUMAnN2 output files.

## Pitfalls

- **HUMAnN2 Compatibility**: Ensure compatibility with HUMAnN2 version.

- **GO Database**: Use up-to-date GO database for accurate mapping.

- **Annotation Coverage**: Some UniRef50 families may not have GO annotations.

- **Normalization**: Be aware of normalization methods for abundance calculations.

- **Output Interpretation**: Interpret GO term abundances carefully.

## Examples

### Basic conversion
**Args:** `group_humann2_uniref_abundances_to_go -i humann2_output.tsv -o go_abundances.tsv`
**Explanation:** Converts HUMAnN2 output to GO term abundances.

### Specify GO slim
**Args:** `group_humann2_uniref_abundances_to_go -i humann2_output.tsv -s go_slim.obo -o go_abundances.tsv`
**Explanation:** Uses custom GO slim file for mapping.

### Include annotations
**Args:** `group_humann2_uniref_abundances_to_go -i humann2_output.tsv -a -o go_abundances.tsv`
**Explanation:** Includes GO term annotations in output.

### Batch processing
**Args:** `for f in *.tsv; do group_humann2_uniref_abundances_to_go -i $f -o ${f%.tsv}_go.tsv; done`
**Explanation:** Processes multiple HUMAnN2 output files.

### Filter low abundance
**Args:** `group_humann2_uniref_abundances_to_go -i humann2_output.tsv -t 0.01 -o filtered.tsv`
**Explanation:** Filters out GO terms with abundance below threshold.

### Generate statistics
**Args:** `group_humann2_uniref_abundances_to_go -i humann2_output.tsv -s -o stats.txt`
**Explanation:** Generates statistics about GO term distribution.

### Custom mapping
**Args:** `group_humann2_uniref_abundances_to_go -i humann2_output.tsv -m custom_mapping.txt -o go_abundances.tsv`
**Explanation:** Uses custom UniRef50 to GO mapping file.