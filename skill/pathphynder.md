---
name: pathphynder
category: population-genomics
description: PathPhynder places ancient DNA sequences into reference phylogenies.
tags: [pathphynder, population-genomics, ancient-dna, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/ruidlpm/pathPhynder"
---

## Concepts

- **Tool Overview**: PathPhynder integrates ancient DNA into phylogenetic trees.
- **Core Function**: Places ancient samples into reference phylogenies.
- **Algorithm**: Uses marker identification and tree traversal.
- **Input Format**: Accepts ancient DNA sequences and reference trees.
- **Output**: Produces placement results on phylogeny.
- **Use Case**: Ancient DNA analysis, population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **DNA Damage**: Ancient DNA has high error rates.
- **Coverage**: Low coverage affects results.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathphynder --help`
**Explanation:** Shows available options and usage instructions.

### Place ancient DNA
**Args:** `pathphynder -i ancient.fasta -t tree.nwk -o results/`
**Explanation:** Places ancient DNA into phylogeny.

### With markers
**Args:** `pathphynder -i ancient.fasta -m markers.txt -t tree.nwk -o results/`
**Explanation:** Uses custom SNP markers.

### Verbose mode
**Args:** `pathphynder -v -i ancient.fasta -t tree.nwk -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pathphynder -t 4 -i ancient.fasta -t tree.nwk -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pathphynder -i ancient.fasta -t tree.nwk -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate visualization
**Args:** `pathphynder_plot -i results/ -o plot.png`
**Explanation:** Generates phylogenetic placement plot.