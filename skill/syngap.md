---
name: syngap
category: annotation
description: Synteny-based Gene structure Annotation Polisher for improving gene annotations.
tags: [syngap, gene-annotation, synteny, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/yanyew/SynGAP"
---

## Concepts

- **Tool Overview**: syngap (v1.2.5) polishes gene structure annotations using synteny.
- **Core Function**: Improves gene structure predictions using syntenic alignments.
- **Algorithm**: Uses synteny information to refine gene models.
- **Input/Output**: Input: Genome sequence, gene predictions; Output: Polished annotations.
- **Applications**: Gene annotation improvement, comparative genomics.
- **Installation**: `conda install -c bioconda syngap` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large genomes require significant memory.
- **Computational Time**: Processing large genomes can be slow.
- **Parameter Tuning**: Incorrect parameters affect polishing.
- **Reference Quality**: Requires high-quality reference annotation.
- **Synteny Quality**: Relies on good syntenic alignments.
- **Gene Model Quality**: Poor initial predictions affect results.

## Examples

### Display help
**Args:** `syngap --help`
**Explanation:** Shows available options and usage information.

### Basic annotation polishing
**Args:** `syngap -i genome.fasta -a annotations.gff -r reference.gff -o polished.gff`
**Explanation:** Polish gene annotations using reference.

### With synteny
**Args:** `syngap -i genome.fasta -a annotations.gff -s synteny.chain -o polished.gff`
**Explanation:** Use synteny chain file for polishing.

### Verbose mode
**Args:** `syngap -i genome.fasta -a annotations.gff -r reference.gff -o polished.gff -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `syngap -i genome.fasta -a annotations.gff -r reference.gff -o polished.gff --stats`
**Explanation:** Generate statistics about polishing.

### Batch processing
**Args:** `for f in genomes/*.fasta; do syngap -i $f -a ${f%.fasta}.gff -r ref.gff -o polished/${f%.fasta}.gff; done`
**Explanation:** Process multiple genomes.

### Filter by confidence
**Args:** `syngap -i genome.fasta -a annotations.gff -r reference.gff -o polished.gff -c 0.9`
**Explanation:** Filter by confidence threshold.

### Include UTRs
**Args:** `syngap -i genome.fasta -a annotations.gff -r reference.gff -o polished.gff --include-utr`
**Explanation:** Include UTR regions in polishing.

### Generate report
**Args:** `syngap -i genome.fasta -a annotations.gff -r reference.gff -o polished.gff --report`
**Explanation:** Generate comprehensive annotation report.
