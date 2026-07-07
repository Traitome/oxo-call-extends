---
name: pifcosm
category: hpc
description: pifcosm constructs supermatrix trees from GenBank data.
tags: [pifcosm, hpc, supermatrix, genbank]
author: oxo-call-community
source_url: "https://github.com/RybergGroup/PifCoSm"
---

## Concepts

- **Tool Overview**: pifcosm constructs supermatrix trees.
- **Core Function**: Supermatrix tree construction.
- **Algorithm**: Uses phylogenetic tree methods.
- **Input Format**: Accepts GenBank data files.
- **Output**: Produces supermatrix tree results.
- **Use Case**: Phylogenetics, tree construction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Tree Construction**: May have construction errors.
- **Runtime**: Construction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pifcosm --help`
**Explanation:** Shows available options and usage instructions.

### Construct tree
**Args:** `pifcosm -i genbank_data.txt -o supermatrix_tree.txt`
**Explanation:** Constructs supermatrix tree from GenBank data.

### With parameters
**Args:** `pifcosm -i genbank_data.txt -p params.yaml -o supermatrix_tree.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pifcosm -v -i genbank_data.txt -o supermatrix_tree.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pifcosm -t 4 -i genbank_data.txt -o supermatrix_tree.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pifcosm -i genbank_data.txt -o supermatrix_tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `pifcosm -i genbank_data.txt -o supermatrix_tree.txt --report report.html`
**Explanation:** Generates HTML report.