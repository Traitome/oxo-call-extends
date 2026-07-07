---
name: idba
category: assembly
description: IDBA is an iterative De Bruijn Graph De Novo Assembler for sequence assembly, with specialized versions for different data types including IDBA-UD for uneven-depth data and IDBA-Tran for RNA-Seq.
tags: [idba, assembly, de novo, De Bruijn Graph]
author: oxo-call-community
source_url: "https://i.cs.hku.hk/~alse/hkubrg/projects/idba_ud"
---

## Concepts

- **IDBA Suite**: IDBA (Iterative De Bruijn Graph Assembler) is a family of de novo assemblers including IDBA-UD for single-cell/metagenomic data, IDBA-Hybrid for reference-guided assembly, and IDBA-Tran for transcriptome assembly.
- **De Bruijn Graph Assembly**: Uses k-mer based graph construction to assemble short sequencing reads into longer contigs and scaffolds.
- **Iterative k-mer Approach**: Progressively increases k-mer size from mink to maxk to handle different sequencing depths and reduce errors.
- **Error Correction**: Includes built-in error correction for high-depth regions and can perform pre-correction before assembly.
- **Multi-level Scaffolding**: Supports up to 5 levels of paired-end read integration for scaffold construction.

## Pitfalls

- **k-mer Size Selection**: Choosing inappropriate mink/maxk values can significantly affect assembly quality; defaults may not suit all datasets.
- **Memory Requirements**: High memory usage for large datasets, especially with large k-mer sizes and deep sequencing coverage.
- **Input Format Limitations**: Requires FASTA format input; FASTQ must be converted first.
- **Read Length Constraints**: Designed for reads ≤128bp by default; longer reads require special handling with `-l` flag.
- **Reference Dependence**: IDBA-Hybrid requires a closely related reference genome for optimal performance.

## Examples

### Basic de novo assembly with IDBA-UD
**Args:** `idba_ud -r reads.fa -o output_dir`
**Explanation:** Runs IDBA-UD with default parameters for de novo assembly of genomic reads with uneven depth coverage.

### Assembly with paired-end reads
**Args:** `idba_ud -r short_reads.fa -l long_reads.fa --read_level_2 pe_reads.fa -o output_dir`
**Explanation:** Combines short and long reads with paired-end reads at level 2 for improved scaffolding.

### Custom k-mer range
**Args:** `idba_ud -r reads.fa -o output_dir --mink 20 --maxk 80 --step 10`
**Explanation:** Specifies k-mer range from 20 to 80 with 10-step increments for more granular assembly.

### With pre-correction enabled
**Args:** `idba_ud -r reads.fa -o output_dir --pre_correction --num_threads 8`
**Explanation:** Performs pre-correction of reads before assembly using 8 threads for parallel processing.

### RNA-Seq assembly with IDBA-Tran
**Args:** `idba_tran -r rna_reads.fa -o transcriptome_output`
**Explanation:** Uses IDBA-Tran specifically designed for transcriptome assembly from RNA-Seq data.