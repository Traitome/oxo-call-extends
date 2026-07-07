---
name: splitmem
category: comparative-genomics
description: SplitMEM - Graphical pan-genome analysis with suffix skips
tags: [splitmem, comparative-genomics, pan-genome, suffix-skips, graphical]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/splitmem/"
---

## Concepts

- **Tool Overview**: splitmem (v1.0) - A pan-genome analysis tool
- **Core Function**: Performs graphical pan-genome analysis with suffix skips
- **Input/Output**: Accepts multiple genomes; outputs pan-genome graphs
- **Algorithm**: Graphical representation with suffix skips
- **Installation**: `conda install -c bioconda splitmem`
- **Key Features**: Pan-genome, graphical analysis, suffix skips

## Pitfalls

- **Input Requirements**: Requires properly formatted genome sequences
- **Genome Quality**: Genome quality affects pan-genome accuracy
- **Suffix Skips**: Suffix skip parameters affect graph construction
- **Memory Usage**: Large genome sets require significant memory
- **Output Format**: Output format depends on configuration
- **Pan-genome Accuracy**: Accuracy depends on genome quality and parameters

## Examples

### Display help
**Args:** `splitmem --help`
**Explanation:** Shows available options and usage information.

### Basic pan-genome analysis
**Args:** `splitmem -i genomes/ -o pan_genome.gfa`
**Explanation:** Perform pan-genome analysis on genomes.

### With suffix skip parameters
**Args:** `splitmem -i genomes/ -o pan_genome.gfa --skip-length 10`
**Explanation:** Set suffix skip length.

### Multiple genomes
**Args:** `splitmem -i genome1.fasta genome2.fasta genome3.fasta -o pan_genome.gfa`
**Explanation:** Analyze multiple genomes.

### Output detailed results
**Args:** `splitmem -i genomes/ -o pan_genome.gfa --detailed`
**Explanation:** Output detailed pan-genome information.

### Output graph statistics
**Args:** `splitmem -i genomes/ -o pan_genome.gfa --graph-stats`
**Explanation:** Output graph statistics.

### Output statistics
**Args:** `splitmem -i genomes/ -o pan_genome.gfa --stats`
**Explanation:** Output analysis statistics.

### Generate report
**Args:** `splitmem -i genomes/ -o pan_genome.gfa --report`
**Explanation:** Generate analysis report.

### With threads
**Args:** `splitmem -i genomes/ -o pan_genome.gfa -p 8`
**Explanation:** Use multiple threads for analysis.