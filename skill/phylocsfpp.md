---
name: phylocsfpp
category: annotation
description: phylocsfpp provides fast PhyloCSF implementation with annotation tools.
tags: [phylocsfpp, annotation, phylocsf, coding]
author: oxo-call-community
source_url: "https://github.com/cpockrandt/PhyloCSFpp"
---

## Concepts

- **Tool Overview**: phylocsfpp implements PhyloCSF.
- **Core Function**: Fast PhyloCSF annotation tool.
- **Algorithm**: Uses PhyloCSF analysis methods.
- **Input Format**: Accepts genome alignment files.
- **Output**: Produces coding region annotation results.
- **Use Case**: Coding region annotation, PhyloCSF.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Coding Detection**: May miss novel coding regions.
- **Runtime**: Annotation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylocsfpp --help`
**Explanation:** Shows available options and usage instructions.

### Annotate coding regions
**Args:** `phylocsfpp -i genome_alignment.fasta -o coding_regions.gff`
**Explanation:** Annotates protein-coding regions.

### With parameters
**Args:** `phylocsfpp -i genome_alignment.fasta -p params.yaml -o coding_regions.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylocsfpp -v -i genome_alignment.fasta -o coding_regions.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylocsfpp -t 4 -i genome_alignment.fasta -o coding_regions.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylocsfpp -i genome_alignment.fasta -o coding_regions.gtf --gtf`
**Explanation:** Outputs in GTF format.

### Generate report
**Args:** `phylocsfpp -i genome_alignment.fasta -o coding_regions.gff --report report.html`
**Explanation:** Generates HTML report.