---
name: treemix
category: analysis
description: TreeMix - Tool for inferring population splits and admixture.
tags: [treemix, population-genetics, admixture, phylogenetics, evolution]
author: oxo-call-community
source_url: "https://github.com/joepickrell/treemix"
---

## Concepts

- **Tool Overview**: TreeMix - A tool for inferring population splits and admixture events from genetic data.
- **Core Function**: Constructs phylogenetic trees with migration edges to model gene flow between populations.
- **Input**: Allele frequency data, population genotypes.
- **Output**: Population tree with migration edges, admixture proportions, likelihood scores.
- **Installation**: `conda install -c bioconda treemix`
- **Use Case**: Population genetics, evolutionary biology, admixture analysis.

## Pitfalls

- **Sample Size**: Requires sufficient sample size for reliable inference.
- **Migration Events**: Number of migration events may need careful selection.

## Examples

### Run TreeMix
**Args:** `treemix -i genotypes.txt -o treemix_output -m 3`
**Explanation:** Run TreeMix with 3 migration events.

### With bootstrap
**Args:** `treemix -i data.txt -o output -m 2 -bootstrap`
**Explanation:** Run TreeMix with bootstrap support.
