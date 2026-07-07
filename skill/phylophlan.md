---
name: phylophlan
category: population-genomics
description: phylophlan performs phylogenetic profiling of microbial genomes.
tags: [phylophlan, population-genomics, microbial, phylogeny]
author: oxo-call-community
source_url: "https://github.com/biobakery/phylophlan"
---

## Concepts

- **Tool Overview**: phylophlan profiles microbial genomes.
- **Core Function**: Phylogenetic profiling pipeline.
- **Algorithm**: Uses phylogenetic marker analysis.
- **Input Format**: Accepts microbial genome files.
- **Output**: Produces phylogenetic profiling results.
- **Use Case**: Microbial analysis, phylogenetic profiling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Genome Quality**: Results depend on genome quality.
- **Marker Selection**: Requires proper marker selection.
- **Runtime**: Profiling may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylophlan --help`
**Explanation:** Shows available options and usage instructions.

### Profile genomes
**Args:** `phylophlan -i microbial_genomes.fasta -o phylogenetic_profile.txt`
**Explanation:** Profiles microbial genomes.

### With config
**Args:** `phylophlan -i microbial_genomes.fasta -c config.yaml -o phylogenetic_profile.txt`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `phylophlan -v -i microbial_genomes.fasta -o phylogenetic_profile.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylophlan -t 4 -i microbial_genomes.fasta -o phylogenetic_profile.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylophlan -i microbial_genomes.fasta -o phylogenetic_profile.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phylophlan -i microbial_genomes.fasta -o phylogenetic_profile.txt --report report.html`
**Explanation:** Generates HTML report.