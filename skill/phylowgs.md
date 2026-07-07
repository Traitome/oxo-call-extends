---
name: phylowgs
category: utility
description: phylowgs infers subclonal composition from sequencing data.
tags: [phylowgs, utility, subclonal, evolution]
author: oxo-call-community
source_url: "https://github.com/morrislab/phylowgs"
---

## Concepts

- **Tool Overview**: phylowgs infers subclonal composition.
- **Core Function**: Subclonal evolution inference.
- **Algorithm**: Uses phylogenetic inference methods.
- **Input Format**: Accepts whole-genome sequencing data.
- **Output**: Produces subclonal composition results.
- **Use Case**: Cancer analysis, subclonal evolution.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequencing Quality**: Results depend on sequencing quality.
- **Subclonal Inference**: May have inference errors.
- **Runtime**: Inference may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylowgs --help`
**Explanation:** Shows available options and usage instructions.

### Infer subclonal composition
**Args:** `phylowgs -i sequencing_data.txt -o subclonal_composition.txt`
**Explanation:** Infers subclonal composition.

### With parameters
**Args:** `phylowgs -i sequencing_data.txt -p params.yaml -o subclonal_composition.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylowgs -v -i sequencing_data.txt -o subclonal_composition.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylowgs -t 4 -i sequencing_data.txt -o subclonal_composition.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylowgs -i sequencing_data.txt -o subclonal_composition.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phylowgs -i sequencing_data.txt -o subclonal_composition.txt --report report.html`
**Explanation:** Generates HTML report.