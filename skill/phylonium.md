---
name: phylonium
category: utility
description: phylonium estimates evolutionary distances from genomes.
tags: [phylonium, utility, evolutionary, distance]
author: oxo-call-community
source_url: "https://github.com/evolbioinf/phylonium"
---

## Concepts

- **Tool Overview**: phylonium estimates evolutionary distances.
- **Core Function**: Fast distance estimation tool.
- **Algorithm**: Uses genome comparison methods.
- **Input Format**: Accepts genome sequence files.
- **Output**: Produces evolutionary distance results.
- **Use Case**: Evolutionary analysis, distance estimation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Genome Quality**: Results depend on genome quality.
- **Distance Estimation**: May have estimation errors.
- **Runtime**: Estimation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylonium --help`
**Explanation:** Shows available options and usage instructions.

### Estimate distances
**Args:** `phylonium -i genome1.fasta genome2.fasta -o evolutionary_distances.txt`
**Explanation:** Estimates evolutionary distances.

### With parameters
**Args:** `phylonium -i genome1.fasta genome2.fasta -p params.yaml -o evolutionary_distances.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylonium -v -i genome1.fasta genome2.fasta -o evolutionary_distances.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylonium -t 4 -i genome1.fasta genome2.fasta -o evolutionary_distances.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylonium -i genome1.fasta genome2.fasta -o evolutionary_distances.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phylonium -i genome1.fasta genome2.fasta -o evolutionary_distances.txt --report report.html`
**Explanation:** Generates HTML report.