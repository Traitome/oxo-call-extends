---
name: cmsearch_tblout_deoverlap
category: utility
description: Remove lower scoring overlaps from cmsearch output
tags: [cmsearch_tblout_deoverlap, cmsearch, rna-analysis, bioinformatics, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/nawrockie/cmsearch_tblout_deoverlap"
---

## Concepts

- **Tool Overview**: cmsearch_tblout_deoverlap is a Perl script that removes lower scoring overlapping hits from cmsearch output tables.
- **Core Function**: Filters cmsearch results to retain only the highest scoring non-overlapping matches.
- **Algorithm**: Uses overlap detection and scoring to select the best non-overlapping hits.
- **Input**: cmsearch tblout format output file.
- **Output**: Filtered tblout file with non-overlapping hits.
- **Application**: RNA motif searching, covariance model analysis, and sequence annotation.
- **Installation**: Install via bioconda: `conda install -c bioconda cmsearch_tblout_deoverlap`

## Pitfalls

- **Input Format**: Requires proper cmsearch tblout format.
- **Score Threshold**: Results depend on scoring thresholds used.
- **Overlap Definition**: Overlap criteria may need adjustment.
- **Sorting**: Input must be properly sorted for correct filtering.
- **cmsearch Version**: Compatibility with different cmsearch versions.

## Examples

### Remove overlapping hits
**Args:** `cmsearch_tblout_deoverlap -i cmsearch.tblout -o filtered.tblout`
**Explanation:** Filters cmsearch output to remove lower scoring overlaps.

### With custom overlap threshold
**Args:** `cmsearch_tblout_deoverlap -i cmsearch.tblout -o filtered.tblout -p 0.5`
**Explanation:** Sets minimum overlap percentage to 50%.

### Keep top hits only
**Args:** `cmsearch_tblout_deoverlap -i cmsearch.tblout -o filtered.tblout -n 10`
**Explanation:** Keeps only top 10 non-overlapping hits.

### Display help
**Args:** `cmsearch_tblout_deoverlap --help`
**Explanation:** Shows all available options and usage information.