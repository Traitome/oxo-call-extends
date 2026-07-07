---
name: spine
category: microbiology
description: Spine - Identification of conserved nucleotide core genome of bacteria
tags: [spine, microbiology, core-genome, comparative-genomics, bacteria]
author: oxo-call-community
source_url: "https://github.com/egonozer/Spine"
---

## Concepts

- **Tool Overview**: spine (v0.3.2) - A core genome identification tool
- **Core Function**: Identifies conserved nucleotide core genome of bacteria and small genome organisms
- **Input/Output**: Accepts bacterial genomes; outputs core genome sequences
- **Algorithm**: Comparative genomics and conservation analysis
- **Installation**: `conda install -c bioconda spine`
- **Key Features**: Core genome, conservation analysis, comparative genomics

## Pitfalls

- **Input Requirements**: Requires properly formatted bacterial genomes
- **Genome Quality**: Genome quality affects core genome accuracy
- **Conservation Threshold**: Threshold affects core genome definition
- **Memory Usage**: Large genome sets require significant memory
- **Output Format**: Output format depends on configuration
- **Core Genome Accuracy**: Accuracy depends on genome quality and threshold

## Examples

### Display help
**Args:** `spine --help`
**Explanation:** Shows available options and usage information.

### Basic core genome identification
**Args:** `spine -i genomes/ -o core_genome.fasta`
**Explanation:** Identify core genome from bacterial genomes.

### With conservation threshold
**Args:** `spine -i genomes/ -o core_genome.fasta --threshold 0.9`
**Explanation:** Set conservation threshold for core genome.

### Multiple genomes
**Args:** `spine -i genome1.fasta genome2.fasta genome3.fasta -o core_genome.fasta`
**Explanation:** Identify core genome from multiple genomes.

### With alignment
**Args:** `spine -i genomes/ -o core_genome.fasta --align`
**Explanation:** Align genomes before core genome identification.

### Output detailed results
**Args:** `spine -i genomes/ -o core_genome.fasta --detailed`
**Explanation:** Output detailed core genome information.

### Output conservation scores
**Args:** `spine -i genomes/ -o core_genome.fasta --conservation`
**Explanation:** Output conservation scores.

### Output statistics
**Args:** `spine -i genomes/ -o core_genome.fasta --stats`
**Explanation:** Output core genome statistics.

### Generate report
**Args:** `spine -i genomes/ -o core_genome.fasta --report`
**Explanation:** Generate core genome report.

### With threads
**Args:** `spine -i genomes/ -o core_genome.fasta -p 8`
**Explanation:** Use multiple threads for analysis.