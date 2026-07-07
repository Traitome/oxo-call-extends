---
name: paste-bio
category: expression
description: PASTE aligns and integrates spatial transcriptomics experiments.
tags: [paste-bio, expression, spatial-transcriptomics, alignment]
author: oxo-call-community
source_url: "https://github.com/raphael-group/paste"
---

## Concepts

- **Tool Overview**: PASTE integrates multiple spatial transcriptomics datasets.
- **Core Function**: Aligns spatial transcriptomics experiments.
- **Algorithm**: Uses optimal transport for spatial alignment.
- **Input Format**: Accepts spatial transcriptomics data.
- **Output**: Produces aligned spatial maps.
- **Use Case**: Spatial transcriptomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Spatial Resolution**: Results depend on input resolution.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paste --help`
**Explanation:** Shows available options and usage instructions.

### Align datasets
**Args:** `paste -d dataset1.h5ad dataset2.h5ad -o aligned.h5ad`
**Explanation:** Aligns two spatial transcriptomics datasets.

### With multiple datasets
**Args:** `paste -d *.h5ad -o aligned/`
**Explanation:** Aligns multiple datasets.

### Verbose mode
**Args:** `paste -v -d dataset1.h5ad dataset2.h5ad -o aligned.h5ad`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `paste -t 4 -d dataset1.h5ad dataset2.h5ad -o aligned.h5ad`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `paste -d dataset1.h5ad dataset2.h5ad -o aligned.csv --csv`
**Explanation:** Outputs in CSV format.

### Plot results
**Args:** `paste_plot -i aligned.h5ad -o plot.png`
**Explanation:** Generates visualization of aligned data.