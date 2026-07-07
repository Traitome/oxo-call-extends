---
name: phylocsf
category: population-genomics
description: phylocsf identifies conserved protein-coding regions.
tags: [phylocsf, population-genomics, coding, phylogenetic]
author: oxo-call-community
source_url: "https://github.com/mlin/PhyloCSF/wiki"
---

## Concepts

- **Tool Overview**: phylocsf identifies coding regions.
- **Core Function**: Phylogenetic coding region analysis.
- **Algorithm**: Uses phylogenetic analysis methods.
- **Input Format**: Accepts genome alignment files.
- **Output**: Produces coding region identification results.
- **Use Case**: Coding region identification, phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Coding Detection**: May miss novel coding regions.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylocsf --help`
**Explanation:** Shows available options and usage instructions.

### Identify coding regions
**Args:** `phylocsf -i genome_alignment.fasta -o coding_regions.txt`
**Explanation:** Identifies protein-coding regions.

### With parameters
**Args:** `phylocsf -i genome_alignment.fasta -p params.yaml -o coding_regions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylocsf -v -i genome_alignment.fasta -o coding_regions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylocsf -t 4 -i genome_alignment.fasta -o coding_regions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylocsf -i genome_alignment.fasta -o coding_regions.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `phylocsf -i genome_alignment.fasta -o coding_regions.txt --report report.html`
**Explanation:** Generates HTML report.