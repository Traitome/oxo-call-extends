---
name: quicksnp
category: variant-calling
description: QuickSNP builds Neighbor Joining trees using SNP distance matrices for phylogenetic analysis.
tags: [quicksnp, variant-calling, phylogenetics, tree-building]
author: oxo-call-community
source_url: "https://github.com/k-florek/QuickSNP"
---

## Concepts

- **Tool Overview**: quicksnp builds SNP-based trees.
- **Core Function**: Phylogenetic tree construction.
- **Algorithm**: Uses Neighbor-Joining.
- **Input Format**: Accepts SNP matrices.
- **Output**: Produces phylogenetic trees.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **SNP Quality**: Affects tree topology.
- **Parameters**: Must be configured.
- **Runtime**: Tree building may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quicksnp --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `quicksnp build -i snp_matrix.txt -o tree.newick`
**Explanation:** Builds Neighbor-Joining tree.

### With parameters
**Args:** `quicksnp build -i snp_matrix.txt -p params.yaml -o tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quicksnp -v build -i snp_matrix.txt -o tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quicksnp -t 4 build -i snp_matrix.txt -o tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### Bootstrap support
**Args:** `quicksnp build -i snp_matrix.txt -b 100 -o tree.newick`
**Explanation:** Performs bootstrap analysis.

### Generate report
**Args:** `quicksnp build -i snp_matrix.txt -o tree.newick --report report.html`
**Explanation:** Generates HTML report.