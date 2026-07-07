---
name: rapgreen
category: annotation
description: RapGreen manipulates and annotates phylogenetic trees for evolutionary analysis.
tags: [rapgreen, annotation, phylogenetics, trees]
author: oxo-call-community
source_url: "http://southgreenplatform.github.io/rap-green/"
---

## Concepts

- **Tool Overview**: rapgreen annotates trees.
- **Core Function**: Tree annotation.
- **Algorithm**: Uses annotation methods.
- **Input Format**: Accepts tree files.
- **Output**: Produces annotated trees.
- **Use Case**: Phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large trees require memory.
- **Tree Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Annotation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rapgreen --help`
**Explanation:** Shows available options and usage instructions.

### Annotate tree
**Args:** `rapgreen annotate -i tree.newick -a annotations.txt -o annotated_tree.newick`
**Explanation:** Annotates phylogenetic tree.

### With parameters
**Args:** `rapgreen annotate -i tree.newick -p params.yaml -o annotated_tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rapgreen -v annotate -i tree.newick -o annotated_tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rapgreen -t 4 annotate -i tree.newick -o annotated_tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### With colors
**Args:** `rapgreen annotate -i tree.newick -c colors.txt -o annotated_tree.newick`
**Explanation:** Uses color scheme.

### Generate report
**Args:** `rapgreen annotate -i tree.newick -o annotated_tree.newick --report report.html`
**Explanation:** Generates HTML report.