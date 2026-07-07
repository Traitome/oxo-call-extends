---
name: orfanage
category: annotation
description: ORFanage efficiently identifies open reading frames in spliced genomes guided by reference annotation.
tags: [orfanage, annotation, orf, genomics]
author: oxo-call-community
source_url: "https://github.com/alevar/ORFanage"
---

## Concepts

- **Tool Overview**: ORFanage identifies ORFs in annotated genomes efficiently.
- **Core Function**: Searches for open reading frames in genomic sequences.
- **Algorithm**: Uses annotation-guided ORF prediction.
- **Input Format**: Accepts FASTA sequences and GTF annotation files.
- **Output**: Produces ORF coordinates and protein sequences.
- **Use Case**: Genome annotation, gene prediction, and transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Annotation Quality**: Results depend on annotation quality.
- **Frame Shifts**: May miss frameshift variants.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orfanage --help`
**Explanation:** Shows available options and usage instructions.

### Find ORFs
**Args:** `orfanage -i genome.fasta -a annotation.gtf -o orfs.fasta`
**Explanation:** Identifies ORFs in genome.

### Without annotation
**Args:** `orfanage -i genome.fasta -o orfs.fasta`
**Explanation:** Finds ORFs without annotation guidance.

### Output format
**Args:** `orfanage -i genome.fasta -o orfs.gff --gff`
**Explanation:** Outputs in GFF format.

### Verbose mode
**Args:** `orfanage -i genome.fasta -v -o orfs.fasta`
**Explanation:** Runs with verbose output.

### Minimum length
**Args:** `orfanage -i genome.fasta -m 100 -o orfs.fasta`
**Explanation:** Sets minimum ORF length.

### Batch processing
**Args:** `orfanage batch -d genomes/ -o results/`
**Explanation:** Processes multiple genome files.