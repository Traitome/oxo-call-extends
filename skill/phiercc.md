---
name: phiercc
category: epigenomics
description: phiercc performs hierarchical clustering of cgMLST profiles.
tags: [phiercc, epigenomics, clustering, cgmlst]
author: oxo-call-community
source_url: "https://github.com/zheminzhou/pHierCC"
---

## Concepts

- **Tool Overview**: phiercc clusters cgMLST profiles.
- **Core Function**: Hierarchical clustering analysis.
- **Algorithm**: Uses cgMLST clustering methods.
- **Input Format**: Accepts cgMLST profile files.
- **Output**: Produces hierarchical cluster results.
- **Use Case**: cgMLST analysis, clustering.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Profile Quality**: Results depend on profile quality.
- **Clustering Method**: Requires proper method selection.
- **Runtime**: Clustering may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phiercc --help`
**Explanation:** Shows available options and usage instructions.

### Cluster profiles
**Args:** `phiercc -i profiles.txt -o clusters.txt`
**Explanation:** Clusters cgMLST profiles.

### With parameters
**Args:** `phiercc -i profiles.txt -p params.yaml -o clusters.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phiercc -v -i profiles.txt -o clusters.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phiercc -t 4 -i profiles.txt -o clusters.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phiercc -i profiles.txt -o clusters.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phiercc -i profiles.txt -o clusters.txt --report report.html`
**Explanation:** Generates HTML report.