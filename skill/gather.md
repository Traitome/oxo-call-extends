---
name: gather
category: immunology
description: Python toolkit for assembling B-cell receptor (BCR) heavy and light chains from single-cell or bulk sequencing data using De Bruijn graphs.
tags: [gather, bcr, immune-repertoire, antibody, de-bruijn-graph, scrna-seq, vdj]
author: oxo-call-community
source_url: "https://github.com/Neuroimmunology-UiO/gather"
---

## Concepts

- **Tool Overview**: Gather is a specialized tool for reconstructing full-length B-cell receptor (BCR) sequences from immune repertoire sequencing data.
- **Core Function**: Assembles immunoglobulin heavy and light chain sequences from NGS reads using De Bruijn graph algorithms optimized for immune repertoire data.
- **Algorithm**: Builds targeted de-Bruijn graphs focused on V(D)J recombination regions, then extracts consensus sequences for each BCR chain.
- **Input Formats**: Supports 10X Genomics V(D)J libraries, bulk RNA-seq, and custom amplicon sequencing data.
- **Paired-Chain Assembly**: Can assemble both heavy (IGH) and light (IGK/IGL) chains, preserving natural pairings from single-cell data.
- **Output**: Full-length variable region sequences with germline V, D, J gene assignments and CDR3 sequences.
- **Installation**: `pip install gather` or `conda install -c bioconda gather`
- **Dependencies**: Python 3.6+, networkx, Biopython, pandas, numpy, pysam
- **Use Cases**: Antibody discovery, hybridoma sequencing validation, immune repertoire profiling, monoclonal antibody sequence extraction.
- **Somatic Hypermutation**: Tracks SHM patterns to understand affinity maturation.

## Pitfalls

- **Read Depth**: Low sequencing depth leads to incomplete assemblies. Minimum 10,000 reads per cell recommended for single-cell data.
- **Primer Bias**: Amplicon-based libraries with biased primers may miss certain V gene families. Validate primer coverage.
- **Paired-End Orientation**: Ensure correct mate pairing in FASTQ files. Improper pairing causes assembly failure.
- **Contig Filtering**: Default quality thresholds may filter valid low-abundance clones. Adjust based on biological expectations.
- **Multi-Cell Contamination**: Single-cell data may contain cross-cell contamination. Consider ambient RNA correction.
- **Memory Requirements**: Large repertoire datasets ( >100K cells) require significant RAM. Process in batches.
- **Species Annotation**: Pre-built V(D)J references exist for human and mouse. Other species require custom reference preparation.

## Examples

### Assemble BCRs from 10X data
**Args:** `gather assemble -i filtered_contig.fasta -o assembled_bcrs.fasta`
**Explanation:** Assembles full-length BCR sequences from 10X Cell Ranger V(D)J output.

### Process single-cell sample
**Args:** `gather singlecell --barcode barcodes.tsv --reads reads.fastq --output results/`
**Explanation:** Processes single-cell BCR data preserving cell barcode associations.

### Assign V(D)J genes
**Args:** `gather assign -i contigs.fasta -s human -o assigned.tsv`
**Explanation:** Annotates assembled contigs with V, D, J gene assignments using IMGT reference database.

### Extract CDR3 sequences
**Args:** `gather cdr3 -i assembled.fasta -o cdr3_sequences.csv`
**Explanation:** Extracts and reports CDR3 amino acid sequences from assembled BCRs.

### Filter low-quality contigs
**Args:** `gather filter -i raw_contigs.fasta --min-length 300 --min-reads 5 -o filtered.fasta`
**Explanation:** Removes contigs failing quality thresholds before downstream analysis.

### Analyze clonotypes
**Args:** `gather clonotype -i assigned.fasta --threshold 0.85 -o clonotypes.csv`
**Explanation:** Groups BCRs into clonotypes based on CDR3 sequence similarity.

### Generate report
**Args:** `gather report -i results/ -o repertoire_summary.html`
**Explanation:** Creates interactive HTML report of immune repertoire statistics.
