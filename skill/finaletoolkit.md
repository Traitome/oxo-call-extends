---
name: finaletoolkit
category: epigenomics
description: "FinaleToolkit (FragmentatIoN AnaLysis of cEll-free DNA Toolkit) extracts fragmentation features from cell-free DNA paired-end sequencing data."
tags: [finaletoolkit, epigenomics, cfDNA, fragmentation, cell-free DNA, bioinformatics, genomics, Python, WGS]
author: oxo-call-community
source_url: "https://github.com/epifluidlab/FinaleToolkit"
---

## Concepts

- **Tool Overview**: FinaleToolkit (FragmentatIoN AnaLysis of cEll-free DNA Toolkit) is a Python package and command-line program to extract fragmentation features of cell-free DNA (cfDNA) from paired-end sequencing data. It is designed for liquid biopsy and non-invasive prenatal testing (NIPT) research.
- **Core Function**: Computes genome-wide fragmentation patterns including end motifs, window protection score (WPS), DELFI (DNA evaluation of fragments for enrichment), fragment length distribution, coverage, and cleavage profiles from cfDNA sequencing data.
- **Input/Output**: Input: BAM/SAM/CRAM files (aligned paired-end sequencing), or pre-processed frag.gz files. Output: Tab-separated values (TSV) files containing feature values per genomic region, or genome-wide aggregations.
- **Algorithm**: Efficient Cython-based implementation that processes alignment records to compute fragmentation features. Handles genome-wide analysis of billions of fragments in hours (reported ~50x speedup over original implementations).
- **Key Features**: Supports BAM/SAM/CRAM/frag.gz formats, fragment length analysis, end motif extraction (4-mer, 6-mer), window protection score (WPS), DELFI computation, cleavage profile, coverage analysis, and Python API for integration into pipelines.
- **Installation**: `pip install finaletoolkit` or `conda install -c bioconda finaletoolkit`. Requires Python >=3.9.

## Pitfalls

- **Index Requirement**: BAM/CRAM files require corresponding index files (.bai/.crai). Ensure the index is present in the same directory as the alignment file.
- **Paired-End Only**: FinaleToolkit is designed for paired-end sequencing data. Single-end data will not produce meaningful fragmentation features.
- **MapQ Filtering**: Low mapping quality reads can introduce artifacts. Consider filtering reads with mapq < 30 for high-quality cfDNA analysis.
- **Reference Genome Compatibility**: Ensure the reference genome used for alignment matches the genome version specified in the analysis (e.g., hg19 vs hg38).
- **Memory for Large Datasets**: While efficient, processing 100X WGS with billions of fragments still requires substantial RAM. For genome-wide analysis, ensure adequate memory (16GB+ recommended).

## Examples

### Compute fragment lengths
**Args:** `finaletoolkit fraglen -i sample.bam -o fraglengths.tsv`
**Explanation:** Extracts fragment length distribution from a BAM file. Outputs a histogram of fragment lengths which is a fundamental cfDNA metric (cfDNA typically shows nucleosomal patterns around 147bp, 167bp, etc.).

### Calculate end motifs
**Args:** `finaletoolkit endmotifs -i sample.bam -o endmotifs.tsv --motif-size 4`
**Explanation:** Computes the frequency of 4-base end motifs (the 4 nucleotides at fragment ends). cfDNA shows characteristic end motif patterns that differ between healthy donors and cancer patients.

### Compute Window Protection Score (WPS)
**Args:** `finaletoolkit wps -i sample.bam -o wps.tsv -r hg38.fa --window-size 120`
**Explanation:** Calculates the Window Protection Score, which measures nucleosomal protection patterns. The --window-size of 120bp approximates the nucleosome length. WPS shows depletion at nucleosome-depleted regions (NDRs).

### Compute DELFI scores
**Args:** `finaletoolkit delfi -i sample.bam -o delfi.tsv --regions promoters.bed`
**Explanation:** Calculates DELFI (DNA Evaluation of fragments for enrichment) scores for genomic regions specified in a BED file. DELFI detects cancer-derived cfDNA by identifying changes in fragment length distributions at regulatory regions.

### Extract coverage profile
**Args:** `finaletoolkit coverage -i sample.bam -o coverage.tsv -r hg38.fa --bin-size 10000`
**Explanation:** Computes coverage in 10kb bins across the genome. Coverage normalization reveals copy number alterations and GC bias in cfDNA samples.

### Process a frag.gz file
**Args:** `finaletoolkit endmotifs -i sample.frag.gz -o endmotifs.tsv --frag`
**Explanation:** When using pre-processed fragment files (.frag.gz), add the --frag flag. These files are block-gzipped BED3+2 format (chrom, start, stop, mapq, strand) and are used with FinaleDB for efficient downstream analysis.

### Use Python API for custom analysis
**Args:**
```python
from finaletoolkit import FinaleToolkit

ft = FinaleToolkit('sample.bam', reference='hg38')
for fragment in ft.get_fragments():
    length = fragment.end - fragment.start
    print(f"Fragment length: {length}")
```
**Explanation:** Import FinaleToolkit in Python for programmatic access

### Filter low-quality fragments
**Args:** `finaletoolkit fraglen -i sample.bam -o filtered_frags.tsv --mapq 30 --length-min 100 --length-max 500`
**Explanation:** Applies quality filters: minimum mapping quality of 30, and fragment length between 100-500bp. This removes alignment artifacts and extreme fragment sizes common in cfDNA analysis.

### Batch process multiple samples
**Args:**
```bash
ls *.bam | parallel -j 4 'finaletoolkit wps -i {} -o {}.wps.tsv -r hg38.fa'
```
**Explanation:** Use GNU parallel for parallel processing of multiple BAM files
