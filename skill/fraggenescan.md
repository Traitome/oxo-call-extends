---
name: fraggenescan
category: assembly
description: FragGeneScan is an application for finding (fragmented) genes in short reads.
tags: [fraggenescan, gene prediction, short reads, prokaryotic]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/fraggenescan"
---

## Concepts
- **Gene Prediction**: Predicts prokaryotic genes from short reads or incomplete assemblies.
- **Fragmented Gene Detection**: Handles fragmented genes caused by short read sequencing.
- **Error Handling**: Designed to handle sequencing errors in short reads.
- **ORF Identification**: Identifies open reading frames in sequencing data.
- **Annotation Support**: Provides gene annotations including start/stop codons.

## Pitfalls
- **Prokaryotic Specific**: Primarily designed for prokaryotic genomes.
- **Read Length**: Performance may degrade with very short reads.
- **GC Content**: May have bias with extreme GC content.
- **False Positives**: May predict non-functional ORFs.
- **Memory Usage**: Processing large datasets requires significant memory.

## Examples
### Predict genes from short reads
**Args:** `FragGeneScan -s reads.fastq -o genes.faa -w 1`
**Explanation:** Predicts genes from short reads using training mode 1 (Illumina).

### Predict genes from assembly
**Args:** `FragGeneScan -s contigs.fasta -o genes.faa -w 0`
**Explanation:** Predicts genes from assembled contigs using training mode 0 (complete genome).

### With quality scores
**Args:** `FragGeneScan -s reads.fastq -q reads_qual.fastq -o genes.faa -w 1`
**Explanation:** Uses quality scores for improved gene prediction accuracy.

### Output nucleotide sequences
**Args:** `FragGeneScan -s reads.fastq -o genes -n -w 1`
**Explanation:** Outputs both amino acid and nucleotide sequences.

### Batch processing
**Args:** `FragGeneScan -s input_dir/ -o output_dir/ -w 1`
**Explanation:** Processes all files in input directory.