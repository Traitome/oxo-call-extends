---
name: rabbittclust
category: hpc
description: RabbitTClust enables fast clustering analysis of millions of bacteria genomes using MinHash sketches.
tags: [rabbittclust, hpc, clustering, genomics]
author: oxo-call-community
source_url: "https://github.com/RabbitBio/RabbitTClust"
---

## Concepts

- **Tool Overview**: rabbittclust clusters genomes.
- **Core Function**: Genome clustering.
- **Algorithm**: Uses MinHash and clustering methods.
- **Input Format**: Accepts genome files.
- **Output**: Produces clusters.
- **Use Case**: Population analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sketch Quality**: Affects clustering.
- **Parameters**: Must be configured.
- **Runtime**: Clustering may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rabbittclust --help`
**Explanation:** Shows available options and usage instructions.

### Run clustering
**Args:** `rabbittclust cluster -i genomes.list -o clusters.txt`
**Explanation:** Clusters genomes.

### With parameters
**Args:** `rabbittclust cluster -i genomes.list -p params.yaml -o clusters.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rabbittclust -v cluster -i genomes.list -o clusters.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rabbittclust -t 4 cluster -i genomes.list -o clusters.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With threshold
**Args:** `rabbittclust cluster -i genomes.list -s 0.95 -o clusters.txt`
**Explanation:** Uses similarity threshold.

### Generate report
**Args:** `rabbittclust cluster -i genomes.list -o clusters.txt --report report.html`
**Explanation:** Generates HTML report.