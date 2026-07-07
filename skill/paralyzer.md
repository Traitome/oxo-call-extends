---
name: paralyzer
category: alignment
description: PARalyzer identifies protein-RNA interaction sites from PAR-CLIP data.
tags: [paralyzer, alignment, par-clip, rna-binding]
author: oxo-call-community
source_url: "https://ohlerlab.mdc-berlin.de/software/PARalyzer_85/"
---

## Concepts

- **Tool Overview**: PARalyzer maps RNA-binding protein interaction sites.
- **Core Function**: Identifies protein-RNA binding sites at single-nucleotide resolution.
- **Algorithm**: Uses kernel density estimation with PAR-CLIP substitution signature.
- **Input Format**: Accepts PAR-CLIP sequencing reads and annotations.
- **Output**: Produces binding site coordinates and scores.
- **Use Case**: RNA-binding protein analysis, CLIP-seq data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Crosslink Quality**: Results depend on crosslink efficiency.
- **Substitution Rate**: Requires sufficient T-to-C substitutions.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `PARalyzer --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `PARalyzer -i reads.bam -g genome.fasta -o binding_sites.gff`
**Explanation:** Identifies protein-RNA binding sites.

### With annotation
**Args:** `PARalyzer -i reads.bam -g genome.fasta -a genes.gtf -o binding_sites.gff`
**Explanation:** Uses gene annotations.

### Verbose mode
**Args:** `PARalyzer -v -i reads.bam -g genome.fasta -o binding_sites.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `PARalyzer -t 4 -i reads.bam -g genome.fasta -o binding_sites.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Score threshold
**Args:** `PARalyzer -s 0.8 -i reads.bam -g genome.fasta -o binding_sites.gff`
**Explanation:** Sets confidence threshold to 0.8.

### Peak calling
**Args:** `PARalyzer -p -i reads.bam -g genome.fasta -o peaks.bed`
**Explanation:** Calls binding peaks.