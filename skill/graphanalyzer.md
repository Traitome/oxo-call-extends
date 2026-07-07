---
name: graphanalyzer
category: bioinformatics
description: GraphAnalyzer automatically interprets outputs from vConTACT2 when using the INPHARED database for viral contig clustering.
tags: [graphanalyzer, viral-genomics, vcontact2, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lazzarigioele/graphanalyzer"
---

## Concepts

- **vConTACT2 Integration**: GraphAnalyzer processes and interprets output files from vConTACT2 viral clustering analysis.

- **INPHARED Database**: Works specifically with the INPHARED database for viral taxonomy and clustering.

- **Graph Analysis**: Analyzes clustering graphs to identify viral groups and their relationships.

- **Taxonomic Assignment**: Assigns taxonomic labels to viral contigs based on clustering results.

- **Quality Control**: Provides metrics for assessing clustering quality and confidence.

- **Visualization**: Generates visualizations of viral clusters and their relationships.

## Pitfalls

- **vConTACT2 Compatibility**: Requires specific output format from vConTACT2. Ensure compatibility.

- **Database Version**: Results depend on the version of the INPHARED database used.

- **Input Quality**: Poor quality viral contigs can produce incorrect clustering results.

- **Computational Resources**: Processing large clustering results may require significant memory.

- **Interpretation**: Clustering results require careful biological interpretation. Not all clusters represent true viral groups.

## Examples

### Analyze vConTACT2 output
**Args:** `graphanalyzer -i vcontact2_output/ -o results.txt`
**Explanation:** Analyzes vConTACT2 clustering results and generates summary statistics.

### Generate taxonomic assignments
**Args:** `graphanalyzer -i vcontact2_output/ -t -o taxonomy.txt`
**Explanation:** Assigns taxonomic labels to viral contigs based on clustering.

### Create visualization
**Args:** `graphanalyzer -i vcontact2_output/ -v -o clusters.png`
**Explanation:** Generates a visualization of viral clusters.

### Filter by cluster size
**Args:** `graphanalyzer -i vcontact2_output/ -m 10 -o filtered.txt`
**Explanation:** Only includes clusters with at least 10 members.

### Compare multiple analyses
**Args:** `graphanalyzer compare -d analysis1/ analysis2/ -o comparison.txt`
**Explanation:** Compares clustering results from multiple vConTACT2 runs.

### Generate report
**Args:** `graphanalyzer -i vcontact2_output/ -r -o report.html`
**Explanation:** Generates a comprehensive HTML report with clustering statistics.

### Batch processing
**Args:** `graphanalyzer batch -d analyses/ -o results/`
**Explanation:** Processes multiple vConTACT2 output directories.