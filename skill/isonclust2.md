---
name: isonclust2
category: expression
description: De novo clustering of long transcriptomic reads from Nanopore or Iso-Seq data for isoform discovery.
tags: [isonclust2, transcriptomics, long reads, isoform discovery, clustering]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/isonclust2"
---

## Concepts

- **Long Read Clustering**: Groups long transcriptomic reads into clusters representing distinct isoforms.
- **De Novo Isoform Discovery**: Identifies novel transcript isoforms without relying on a reference genome.
- **Nanopore/Iso-Seq Support**: Optimized for Oxford Nanopore and PacBio Iso-Seq long-read sequencing technologies.
- **Error Correction**: Incorporates error correction for noisy long-read data.
- **Transcript Quantification**: Provides isoform-level expression quantification from clustered reads.
- **Alternative Splicing Analysis**: Enables identification of alternative splicing events from long-read data.

## Pitfalls

- **Read Quality**: Poor quality long reads can lead to incorrect clustering and isoform identification.
- **Computational Complexity**: Clustering large datasets requires significant computational resources.
- **Memory Requirements**: Processing millions of long reads may require substantial memory.
- **Isoform Complexity**: Highly similar isoforms may be merged incorrectly.
- **Coverage Bias**: Uneven sequencing coverage can affect clustering accuracy.
- **Chimeric Reads**: Chimeric sequences can create false clusters representing non-existent isoforms.

## Examples

### Basic clustering
**Args:** `isonclust2 --reads reads.fastq --output clusters/`
**Explanation:** Performs de novo clustering of long transcriptomic reads.

### With quality filtering
**Args:** `isonclust2 --reads reads.fastq --min-quality 10 --output clusters/`
**Explanation:** Filters reads by quality score before clustering.

### Isoform quantification
**Args:** `isonclust2 --reads reads.fastq --quantify --output clusters/`
**Explanation:** Performs clustering with isoform-level expression quantification.

### Reference-guided mode
**Args:** `isonclust2 --reads reads.fastq --reference ref.gtf --output clusters/`
**Explanation:** Uses a reference annotation to guide clustering and isoform discovery.

### Batch processing
**Args:** `isonclust2 --batch samples.txt --output-dir results/`
**Explanation:** Processes multiple samples listed in a batch file.

### Generate visualization
**Args:** `isonclust2 --reads reads.fastq --visualize --output clusters/`
**Explanation:** Generates visualizations of clustering results.