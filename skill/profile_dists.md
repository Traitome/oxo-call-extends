---
name: profile_dists
category: population-genomics
description: profile_dists calculates allele profile distances for population genomics analysis.
tags: [profile_dists, population-genomics, distance-calculation, allele-analysis]
author: oxo-call-community
source_url: "https://pypi.org/project/profile-dists"
---

## Concepts

- **Tool Overview**: profile_dists computes genetic distances.
- **Core Function**: Allele profile distance calculation.
- **Algorithm**: Uses distance-based methods.
- **Input Format**: Accepts allele profile files.
- **Output**: Produces distance matrices.
- **Use Case**: Population genetics, strain typing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Distance Metric**: Choice affects results.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `profile_dists --help`
**Explanation:** Shows available options and usage instructions.

### Calculate distances
**Args:** `profile_dists -i profiles.txt -o distances.txt`
**Explanation:** Computes allele profile distances.

### With parameters
**Args:** `profile_dists -i profiles.txt -p params.yaml -o distances.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `profile_dists -v -i profiles.txt -o distances.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `profile_dists -t 4 -i profiles.txt -o distances.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `profile_dists -i profiles.txt -o distances.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `profile_dists -i profiles.txt -o distances.txt --report report.html`
**Explanation:** Generates HTML report.