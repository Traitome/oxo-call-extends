---
name: stringtie
category: expression
description: StringTie employs efficient algorithms for transcript structure recovery and abundance estimation from bulk RNA-Seq reads aligned to a reference genome.
tags: [stringtie, expression, rna-seq, transcriptome, assembly]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/stringtie/index.shtml?t=manual"
---

## Concepts

- **Tool Overview**: StringTie (v3.0.3+) is a fast and efficient tool for transcript assembly and quantification from RNA-seq reads aligned to a reference genome. It assembles transcripts and estimates their abundances using a network flow algorithm.
- **Core Function**: Assembles aligned RNA-seq reads into transcripts and estimates gene/transcript expression levels. Can also merge assemblies from multiple samples.
- **Input/Output**: Input: BAM file with aligned reads, optional GTF annotation. Output: Assembled transcripts (GTF), abundance estimates (FPKM, TPM), and optional coverage files.
- **Algorithm**: Uses a network flow algorithm to assemble transcripts, considering both splice junctions and read coverage. Performs isoform-level quantification.
- **Key Features**: Supports both reference-guided and de novo assembly, can merge assemblies across multiple samples, outputs FPKM and TPM values, and generates Ballgown-compatible output for differential expression analysis.
- **Installation**: `conda install -c bioconda stringtie`

## Pitfalls

- **Input BAM Requirements**: Requires coordinate-sorted BAM file. Use `samtools sort` before running StringTie if BAM is not sorted.
- **Annotation File**: Providing a reference GTF (`-G`) improves transcript assembly accuracy but is not required.
- **Strand-Specific Data**: For strand-specific libraries, use `-rf` (reverse-stranded) or `-fr` (forward-stranded) to ensure correct strand assignment.
- **Memory Usage**: For large datasets, consider increasing memory with `-M` flag or processing samples individually.
- **Output Format**: Default output is GTF. Use `-B` flag to generate Ballgown-compatible output for differential expression analysis.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic transcript assembly and quantification
**Args:** `-o transcripts.gtf -G reference.gtf -p 8 aligned.bam`
**Explanation:** Assembles transcripts from aligned reads, using reference annotation as guide, with 8 threads. Outputs GTF file with assembled transcripts and abundance estimates.

### De novo transcript assembly
**Args:** `-o transcripts.gtf -p 8 aligned.bam`
**Explanation:** Performs de novo transcript assembly without reference annotation. Useful for discovering novel transcripts.

### Strand-specific assembly
**Args:** `-o transcripts.gtf -G reference.gtf -rf -p 8 aligned.bam`
**Explanation:** Assembles strand-specific (reverse-stranded) RNA-seq data. Use `-fr` for forward-stranded libraries.

### Generate Ballgown-compatible output
**Args:** `-o transcripts.gtf -G reference.gtf -B -p 8 aligned.bam`
**Explanation:** Generates Ballgown-compatible output files for differential expression analysis in R/Ballgown.

### Merge assemblies from multiple samples
**Args:** `--merge -o merged.gtf -G reference.gtf sample1.gtf sample2.gtf sample3.gtf`
**Explanation:** Merges transcript assemblies from multiple samples into a single consensus transcriptome.

### Quantify only (no assembly)
**Args:** `-e -o transcripts.gtf -G reference.gtf -p 8 aligned.bam`
**Explanation:** Performs quantification only using reference annotation, without assembling new transcripts.

### Assembly with coverage threshold
**Args:** `-o transcripts.gtf -G reference.gtf -c 1 -p 8 aligned.bam`
**Explanation:** Sets minimum coverage threshold to 1 for transcript assembly. Filters out low-coverage transcripts.

### Output abundance estimates only
**Args:** `-A gene_abundances.tsv -o transcripts.gtf -G reference.gtf -p 8 aligned.bam`
**Explanation:** Outputs gene-level abundance estimates to gene_abundances.tsv in addition to transcript-level estimates in GTF.