---
name: cpc2
category: annotation
description: Coding Potential Calculator 2 - fast and accurate tool for distinguishing coding and noncoding RNA transcripts
tags: [cpc2, coding-potential, lncrna, noncoding-rna, rna, annotation, svm]
author: oxo-call-community
source_url: "https://github.com/gao-lab/CPC2_standalone"
---

## Concepts

- **Tool Overview**: CPC2 (Coding Potential Calculator 2) is a fast and accurate tool for assessing the coding potential of RNA transcripts, distinguishing protein-coding from non-coding RNAs using sequence intrinsic features.
- **Core Function**: Classifies RNA transcripts as coding or noncoding based on longest ORF detection, Fickett score, isoelectric point (pI), and SVM-based coding probability.
- **Algorithm**: Uses SVM (Support Vector Machine) with features including ORF length, peptide length, Fickett TESTCODE score, and isoelectric point. The model is species-neutral, enabling use across diverse organisms.
- **Input**: FASTA format transcript sequences, or BED/GTF/GFF format with reference genome.
- **Output**: Tab-delimited table with transcript length, peptide length, Fickett score, pI, ORF integrity, coding probability, and classification label (coding/noncoding).
- **Application**: lncRNA discovery, transcriptome annotation, coding potential assessment for novel transcripts.
- **Installation**: Install via bioconda: `conda install -c bioconda cpc2` or via pip: `pip install cpc2-standalone`

## Pitfalls

- **Input Format**: FASTA sequences must contain only valid DNA/RNA characters (A, T, G, C, U, N).
- **Sequence Names**: Characters after a blank space in sequence IDs are discarded.
- **Biopython Dependency**: Requires Biopython for sequence parsing.
- **libsvm Compilation**: Standalone version requires compiling libsvm library.
- **ORF Detection**: Uses longest ORF as proxy; may miss alternative start codons.

## Examples

### Basic coding potential prediction
**Args:** `cpc2 -i transcripts.fa -o cpc2_results.txt`
**Explanation:** Assesses coding potential for all transcripts in FASTA file using default settings.

### Check reverse strand
**Args:** `cpc2 -i transcripts.fa -o cpc2_results.txt -r`
**Explanation:** Also searches for ORFs on the reverse complement strand, useful for anti-sense transcripts.

### Output ORF start position
**Args:** `cpc2 -i transcripts.fa -o cpc2_results.txt --ORF`
**Explanation:** Adds the start position of the longest ORF to the output table.

### Custom output filename
**Args:** `cpc2 -i input.fasta -o custom_output.txt`
**Explanation:** Specifies a custom output filename instead of the default.

### Filter noncoding transcripts
**Args:** `cpc2 -i transcriptome.fa -o results.txt && grep noncoding results.txt`
**Explanation:** Runs CPC2 and filters for noncoding transcripts using shell grep.
