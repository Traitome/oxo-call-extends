---
name: rjchallis-assembly-stats
category: assembly
description: Assembly-stats provides visualizations for assessing and comparing assembly quality.
tags: [rjchallis-assembly-stats, assembly, quality-control, visualization]
author: oxo-call-community
source_url: "https://github.com/rjchallis/assembly-stats"
---

## Concepts

- **Tool Overview**: rjchallis-assembly-stats visualizes assembly metrics.
- **Core Function**: Assembly quality visualization.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts assembly files.
- **Output**: Produces quality metrics.
- **Use Case**: Assembly evaluation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Assembly Quality**: Affects metrics.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `assembly-stats --help`
**Explanation:** Shows available options and usage instructions.

### Generate stats
**Args:** `assembly-stats stats -i assembly.fasta -o stats.txt`
**Explanation:** Computes assembly statistics.

### With parameters
**Args:** `assembly-stats stats -i assembly.fasta -p params.yaml -o stats.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `assembly-stats -v stats -i assembly.fasta -o stats.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `assembly-stats -t 4 stats -i assembly.fasta -o stats.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `assembly-stats stats -i assembly.fasta -r reference.fasta -o stats.txt`
**Explanation:** Uses reference genome.

### Generate plot
**Args:** `assembly-stats stats -i assembly.fasta -o stats.txt --plot plot.png`
**Explanation:** Generates visualization plot.