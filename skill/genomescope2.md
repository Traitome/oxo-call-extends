---
name: genomescope2
category: genome-analysis
description: GenomeScope2 - Reference-free profiling of polyploid genomes.
tags: [genomescope2, polyploid-genomics, genome-profiling, reference-free]
author: oxo-call-community
source_url: "https://github.com/tbenavi1/genomescope2.0"
---

## Concepts
- **Polyploid Genome Analysis**: Analyzes polyploid genome structure.
- **Reference-free Profiling**: Profiles genomes without reference.
- **Genome Size Estimation**: Estimates genome size from k-mer data.
- **Repeat Content Analysis**: Analyzes repeat content in genomes.
- **Heterozygosity Estimation**: Estimates heterozygosity levels.

## Pitfalls
- **k-mer Size Selection**: Results depend on k-mer size.
- **Read Quality**: Requires high-quality sequencing data.
- **Genome Complexity**: Complex genomes may be misestimated.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Validation**: Results should be validated with other methods.

## Examples
### Profile genome
**Args:** `genomescope2 -i kmer_histogram.txt -o results/ -k 21`
**Explanation:** Profiles genome using k-mer histogram.

### Estimate genome size
**Args:** `genomescope2 -i kmer_histogram.txt -o results/ --estimate-size`
**Explanation:** Estimates genome size from k-mer data.

### With custom parameters
**Args:** `genomescope2 -i kmer_histogram.txt -o results/ -k 31 -p 4`
**Explanation:** Uses k-mer size 31 and ploidy 4.

### Batch processing
**Args:** `genomescope2 -i ./histograms/ -o ./results/`
**Explanation:** Processes multiple k-mer histograms in batch.

### Generate report
**Args:** `genomescope2 -i kmer_histogram.txt -o results/ -r`
**Explanation:** Generates comprehensive report.