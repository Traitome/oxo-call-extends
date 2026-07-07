---
name: spaln
category: alignment
description: Spaln - Map and align cDNA/EST or protein sequences onto genome
tags: [spaln, alignment, cdna, est, protein, genome-alignment]
author: oxo-call-community
source_url: "https://github.com/ogotoh/spaln"
---

## Concepts

- **Tool Overview**: spaln (v3.0.8) - A cDNA/EST/protein genome alignment tool
- **Core Function**: Maps and aligns sequences to genome with splice awareness
- **Input/Output**: Accepts cDNA/EST/protein sequences; outputs genome alignments
- **Algorithm**: Splice-aware alignment algorithm
- **Installation**: `conda install -c bioconda spaln`
- **Key Features**: Splice-aware alignment, cDNA mapping, protein alignment

## Pitfalls

- **Input Requirements**: Requires properly formatted cDNA/EST/protein sequences
- **Reference Genome**: Requires reference genome for alignment
- **Splice Sites**: Splice site prediction affects alignment accuracy
- **Memory Usage**: Large genomes require significant memory
- **Output Format**: Output format depends on configuration
- **Alignment Quality**: Quality of alignment depends on sequence similarity

## Examples

### Display help
**Args:** `spaln --help`
**Explanation:** Shows available options and usage information.

### Basic cDNA alignment
**Args:** `spaln -i cdna.fasta -r reference.fasta -o aligned.sam`
**Explanation:** Align cDNA sequences to genome.

### Protein alignment
**Args:** `spaln -i protein.fasta -r reference.fasta -o aligned.sam --protein`
**Explanation:** Align protein sequences to genome.

### With splice prediction
**Args:** `spaln -i cdna.fasta -r reference.fasta -o aligned.sam --splice`
**Explanation:** Enable splice site prediction.

### With intron length
**Args:** `spaln -i cdna.fasta -r reference.fasta -o aligned.sam --max-intron 100000`
**Explanation:** Set maximum intron length.

### Output GFF format
**Args:** `spaln -i cdna.fasta -r reference.fasta -o aligned.gff --gff`
**Explanation:** Output alignments in GFF format.

### Output statistics
**Args:** `spaln -i cdna.fasta -r reference.fasta -o aligned.sam --stats`
**Explanation:** Output alignment statistics.

### Generate report
**Args:** `spaln -i cdna.fasta -r reference.fasta -o aligned.sam --report`
**Explanation:** Generate alignment report.

### With threads
**Args:** `spaln -i cdna.fasta -r reference.fasta -o aligned.sam -p 8`
**Explanation:** Use multiple threads for alignment.