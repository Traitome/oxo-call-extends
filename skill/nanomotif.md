---
name: nanomotif
category: epigenomics
description: NanoMotif - Identifying methylation motifs in Nanopore sequencing data
tags: [nanomotif, epigenomics, nanopore, methylation, motif, dna-methylation]
author: oxo-call-community
source_url: "https://github.com/MicrobialDarkMatter/nanomotif"
---

## Concepts

- **Tool Overview**: NanoMotif v1.1.2 identifies DNA methylation motifs from Oxford Nanopore sequencing data. It discovers sequence motifs associated with methylation patterns.
- **Core Function**: Analyzes modified base calls to identify recurring sequence motifs that are preferentially methylated. Helps understand methylation specificity.
- **Algorithm**: Uses motif discovery algorithms to find overrepresented k-mers associated with modified bases. Can identify both known and novel methylation motifs.
- **Input Format**: Accepts modified base calls in various formats (BED, TSV, or SAM/BAM with modification tags). Requires reference genome in FASTA format.
- **Output**: Produces tabular files with motif sequences, occurrence counts, and methylation frequencies. Includes visualization options.
- **Use Case**: Epigenomics research, understanding DNA methylation specificity, discovering novel methylation motifs, and comparing methylation patterns across samples.

## Pitfalls

- **Modified Base Calls**: Requires high-quality modified base calls. Inaccurate modification detection affects motif discovery.
- **Motif Size**: Default motif sizes may not capture all biologically relevant patterns. Adjust k-mer size as needed.
- **Coverage**: Requires sufficient coverage across genome to identify statistically significant motifs.
- **Background Model**: Motif significance depends on proper background model. Consider using control samples.
- **False Discovery**: Multiple testing correction is essential for genome-wide motif discovery.
- **Reference Bias**: Motif discovery is reference-dependent. Different references may yield different results.

## Examples

### Basic motif discovery
**Args:** `-i modified_bases.tsv -g assembly.fasta -o motifs.tsv`
**Explanation:** Identifies methylation motifs from modified base calls.

### Specify motif size
**Args:** `-i modified_bases.tsv -g ref.fa -o motifs.tsv -k 6`
**Explanation:** Searches for hexamer (6-mer) motifs instead of default size.

### Include visualization
**Args:** `-i modified_bases.tsv -g ref.fa -o output/ --plot`
**Explanation:** Generates visualizations of motif occurrences and methylation patterns.

### Use BAM input
**Args:** `-b aligned.bam -g ref.fa -o motifs.tsv`
**Explanation:** Extracts modification information directly from BAM file with modification tags.

### Display help
**Args:** `nanomotif --help`
**Explanation:** Shows all available options for motif discovery.
