---
name: guessmylt
category: bioinformatics
description: GUESSmyLT predicts the RNA-Seq library type (strandedness, orientation) from sequencing data.
tags: [guessmylt, RNA-Seq, library-type, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/NBISweden/GUESSmyLT"
---

## Concepts

- **Library Type Detection**: GUESSmyLT determines RNA-Seq library type automatically.

- **Strandedness Detection**: Identifies whether library is stranded or unstranded.

- **Orientation Detection**: Determines read orientation relative to gene direction.

- **Illumina Adaptors**: Uses adaptor sequences for library type inference.

- **Statistical Prediction**: Applies statistical methods for accurate prediction.

- **Quality Assessment**: Provides confidence scores for predictions.

## Pitfalls

- **Read Quality**: Low-quality reads may affect prediction accuracy.

- **Library Complexity**: Complex libraries may produce ambiguous results.

- **Read Length**: Short reads may reduce prediction confidence.

- **Reference Genome**: Requires good quality reference genome.

- **Transcriptome Annotation**: Incomplete annotations affect accuracy.

## Examples

### Predict library type
**Args:** `guessmylt -i reads.fastq -g genome.fasta -o result.txt`
**Explanation:** Predicts RNA-Seq library type.

### With GTF annotation
**Args:** `guessmylt -i reads.fastq -g genome.fasta -a genes.gtf -o result.txt`
**Explanation:** Uses gene annotation for better prediction.

### Paired-end reads
**Args:** `guessmylt -i reads_1.fastq -i2 reads_2.fastq -g genome.fasta -o result.txt`
**Explanation:** Analyzes paired-end sequencing data.

### Batch processing
**Args:** `for f in *_1.fastq; do guessmylt -i $f -i2 ${f%_1.fastq}_2.fastq -g genome.fasta -o ${f%_1.fastq}_result.txt; done`
**Explanation:** Processes multiple samples.

### Generate report
**Args:** `guessmylt -i reads.fastq -g genome.fasta -r -o report.pdf`
**Explanation:** Generates detailed report with predictions.

### Check confidence
**Args:** `guessmylt -i reads.fastq -g genome.fasta -c -o result.txt`
**Explanation:** Provides confidence scores for predictions.

### Help command
**Args:** `guessmylt --help`
**Explanation:** Shows available options and usage information.