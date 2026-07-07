---
name: rapclust
category: expression
description: RapClust provides accurate, fast and lightweight clustering of de novo transcriptomes using fragment equivalence classes.
tags: [rapclust, expression, clustering, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/RapClust"
---

## Concepts

- **Tool Overview**: rapclust clusters transcripts.
- **Core Function**: Transcriptome clustering.
- **Algorithm**: Uses equivalence classes.
- **Input Format**: Accepts transcript data.
- **Output**: Produces transcript clusters.
- **Use Case**: RNA-seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Coverage**: Affects clustering.
- **Parameters**: Must be configured.
- **Runtime**: Clustering may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rapclust --help`
**Explanation:** Shows available options and usage instructions.

### Cluster transcripts
**Args:** `rapclust cluster -i transcripts.fasta -o clusters.txt`
**Explanation:** Clusters transcriptome.

### With parameters
**Args:** `rapclust cluster -i transcripts.fasta -p params.yaml -o clusters.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rapclust -v cluster -i transcripts.fasta -o clusters.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rapclust -t 4 cluster -i transcripts.fasta -o clusters.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With similarity threshold
**Args:** `rapclust cluster -i transcripts.fasta -s 0.95 -o clusters.txt`
**Explanation:** Uses similarity threshold.

### Generate report
**Args:** `rapclust cluster -i transcripts.fasta -o clusters.txt --report report.html`
**Explanation:** Generates HTML report.