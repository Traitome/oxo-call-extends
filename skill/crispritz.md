---
name: crispritz
category: genome-editing
description: Tool package for CRISPR experiments assessment including off-target search, variant annotation, and report generation
tags: [crispritz, CRISPR, off-target, genome-editing, PAM, mismatch, bulge, Cas9, pinellolab]
author: oxo-call-community
source_url: "https://github.com/pinellolab/CRISPRitz"
---

## Concepts

- **Tool Overview**: CRISPRitz (v2.7.0+) - A software package containing multiple tools for predictive analysis and result assessment on CRISPR/Cas experiments.
- **Core Function**: Performs off-target search on genomes with or without variants, annotates results with functional data, and generates graphical reports for guide evaluation.
- **Tool Suite**: CRISPRitz includes: add-variants (encode genomic variants using IUPAC), index-genome (find candidate targets by PAM), search (off-target search), annotate-results (annotate with functional data), generate-report (graphical reports), process-data (compare reference vs variant results).
- **Input**: Reference genome (FASTA), PAM sequence file, guide sequences (sgRNA), optional VCF for variants.
- **Output**: Target/off-target lists, mismatch profiles, annotated results with functional annotations, graphical reports.
- **Application**: CRISPR guide screening, off-target validation, therapeutic guide selection, population genomics analysis.
- **Installation**: `conda install -c bioconda crispritz` or Docker: `docker pull quay.io/biocontainers/crispritz:<tag>`

## Pitfalls

- **Conda Python Version**: Bioconda recipe requires Python 3.8 specifically; installing in other Python environments may cause conflicts.
- **Reference Genome Index**: Must run index-genome before search; genome index is specific to PAM used.
- **Mismatch/Bulge Thresholds**: Higher mismatch tolerance increases search time significantly.
- **IUPAC Variants**: add-variants uses IUPAC nucleotide codes for heterozygous sites; ensure VCF is properly phased.
- **Threading**: Use -t flag for multi-threaded search; essential for large genomes.
- **External Tools**: Requires bedops, bedtools, bcftools, htslib for full functionality.

## Examples

### Add variants to reference genome
**Args:** `crispritz.py add-variants hg38_1000genomeproject_vcf/ hg38_ref/`
**Explanation:** Encode genomic variants from 1000 Genomes VCF files into the reference genome using IUPAC notation for heterozygous sites.

### Index genome for off-target search
**Args:** `crispritz.py index-genome hg38_ref/ hg38_ref/ 20bp-NGG-SpCas9.txt -bMax 2`
**Explanation:** Create index of candidate target sites using NGG PAM pattern with maximum 2 bulge size for DNA.

### Basic off-target search
**Args:** `crispritz.py search hg38_ref/ 20bp-NGG-SpCas9.txt EMX1.sgRNA.txt emx1.hg38 -mm 4 -t`
**Explanation:** Search for off-target sites allowing up to 4 mismatches using pre-indexed genome.

### Search with DNA/RNA bulges
**Args:** `crispritz.py search genome_library/NGG_hg38_ref/ 20bp-NGG-SpCas9.txt EMX1.sgRNA.txt emx1.hg38.bulges -index -mm 4 -bDNA 1 -bRNA 1 -t`
**Explanation:** Search allowing 1 DNA bulge and 1 RNA bulge in addition to mismatches.

### Annotate results with functional genomics
**Args:** `crispritz.py annotate-results emx1.hg38.targets.txt hg38Annotation.bed emx1.hg38`
**Explanation:** Annotate off-target results with functional data (promoters, chromatin accessibility, insulators, etc.) from BED file.

### Generate graphical report
**Args:** `crispritz.py generate-report emx1.hg38.targets.txt emx1.hg38`
**Explanation:** Create graphical representation of mismatch and bulge profiles for the guide showing on/off-target behavior.

### Process and compare reference vs variant results
**Args:** `crispritz.py process-data reference_results/ variant_results/ output/ --population 1000genomes`
**Explanation:** Compare off-target results between reference and variant genomes, providing population-level insights for each target.
