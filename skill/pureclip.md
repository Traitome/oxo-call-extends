---
name: pureclip
category: utility
description: PureCLIP detects protein-RNA interaction footprints from CLIP-seq data.
tags: [pureclip, utility, CLIP-seq, RNA-binding]
author: oxo-call-community
source_url: "https://github.com/skrakau/PureCLIP"
---

## Concepts

- **Tool Overview**: pureclip analyzes CLIP-seq data.
- **Core Function**: Footprint detection.
- **Algorithm**: Uses statistical modeling.
- **Input Format**: Accepts BAM/BED files.
- **Output**: Produces binding sites.
- **Use Case**: RNA-protein interactions.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Read Depth**: Affects detection sensitivity.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pureclip --help`
**Explanation:** Shows available options and usage instructions.

### Detect footprints
**Args:** `pureclip -i reads.bam -g genome.fasta -o footprints.bed`
**Explanation:** Detects protein-RNA binding footprints.

### With parameters
**Args:** `pureclip -i reads.bam -g genome.fasta -p params.yaml -o footprints.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pureclip -v -i reads.bam -g genome.fasta -o footprints.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pureclip -t 4 -i reads.bam -g genome.fasta -o footprints.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pureclip -i reads.bam -g genome.fasta -o footprints.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `pureclip -i reads.bam -g genome.fasta -o footprints.bed --report report.html`
**Explanation:** Generates HTML report.