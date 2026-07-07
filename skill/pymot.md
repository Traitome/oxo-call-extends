---
name: pymot
category: programming
description: pyMot computes MOTP and MOTA metrics for evaluating multiple object tracking algorithms.
tags: [pymot, programming, tracking, evaluation]
author: oxo-call-community
source_url: "https://github.com/Videmo/pymot"
---

## Concepts

- **Tool Overview**: pymot evaluates tracking algorithms.
- **Core Function**: MOT metrics calculation.
- **Algorithm**: Uses tracking evaluation metrics.
- **Input Format**: Accepts track data.
- **Output**: Produces metrics.
- **Use Case**: Tracking evaluation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Ground Truth**: Must be accurate.
- **Track Format**: Must match expected.
- **Runtime**: Evaluation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pymot --help`
**Explanation:** Shows available options and usage instructions.

### Evaluate tracking
**Args:** `pymot evaluate -g ground_truth.txt -h hypothesis.txt -o metrics.txt`
**Explanation:** Computes MOT metrics.

### With parameters
**Args:** `pymot evaluate -g ground_truth.txt -p params.yaml -o metrics.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pymot -v evaluate -g ground_truth.txt -h hypothesis.txt -o metrics.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pymot -t 4 evaluate -g ground_truth.txt -h hypothesis.txt -o metrics.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Compare trackers
**Args:** `pymot compare -g ground_truth.txt -h tracker1.txt tracker2.txt -o comparison.txt`
**Explanation:** Compares multiple trackers.

### Generate report
**Args:** `pymot evaluate -g ground_truth.txt -h hypothesis.txt -o metrics.txt --report report.html`
**Explanation:** Generates HTML report.