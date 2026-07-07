---
name: phertilizer
category: population-genomics
description: phertilizer builds clonal trees from single-cell DNA sequencing data.
tags: [phertilizer, population-genomics, clonal, single-cell]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/phertilizer"
---

## Concepts

- **Tool Overview**: phertilizer builds clonal trees.
- **Core Function**: Grows trees from ultra-low coverage data.
- **Algorithm**: Uses clonal tree reconstruction.
- **Input Format**: Accepts single-cell DNA data.
- **Output**: Produces clonal tree structures.
- **Use Case**: Clonal analysis, single-cell genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Coverage Quality**: Results depend on coverage quality.
- **Tree Reconstruction**: May have reconstruction errors.
- **Runtime**: Building may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phertilizer --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `phertilizer -i sc_data.fasta -o clonal_tree.txt`
**Explanation:** Builds clonal tree from data.

### With parameters
**Args:** `phertilizer -i sc_data.fasta -p params.yaml -o clonal_tree.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phertilizer -v -i sc_data.fasta -o clonal_tree.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phertilizer -t 4 -i sc_data.fasta -o clonal_tree.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phertilizer -i sc_data.fasta -o clonal_tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phertilizer -i sc_data.fasta -o clonal_tree.txt --report report.html`
**Explanation:** Generates HTML report.