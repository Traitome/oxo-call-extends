---
name: gci
category: assembly
description: A program for assessing genome assembly continuity and completeness at single-base resolution
tags: [gci, assembly, quality-control, telomere-to-telomere, long-reads, t2t]
author: oxo-call-community
source_url: "https://github.com/yeeus/GCI"
---

## Concepts

- **Tool Overview**: GCI (Genome Continuity Inspector) is a tool for assessing genome assembly continuity at single-base resolution, designed specifically for the telomere-to-telomere (T2T) era. It uses long-read sequencing data (PacBio HiFi or Oxford Nanopore) to detect potential assembly gaps and quantify how close an assembly is to the theoretical T2T standard.
- **Core Function**: GCI maps long reads back to the assembly using multiple alignment strategies, then calculates curated coverage depth at each base position. Regions with extremely low coverage are flagged as potential assembly gaps. Unlike N50 which only measures contiguity, GCI provides single-base resolution assessment of assembly completeness.
- **GCI Score**: A quantitative metric (0-100) representing how close the assembly is to T2T quality. A score of 100 means perfect T2T assembly with no gaps. The score incorporates: (1) number of detected gaps, (2) gap sizes and positions, (3) corrected N50 value, (4) deviation from theoretical T2T maximum.
- **Comparison to Traditional Metrics**: Contig N50 and auN reach their theoretical maximums once all contigs are assembled into chromosomes, making them unable to distinguish nearly-T2T from truly T2T assemblies. GCI continues to capture improvements even after N50 plateaus.
- **Input Requirements**: (1) Assembly FASTA file to evaluate, (2) Long-read sequencing data in FASTQ or BAM format (PacBio HiFi or ONT), (3) Index files for the aligner. GCI supports minimap2, pbmm2, and ngmlr aligners.
- **Output Files**: GCI generates multiple output files including: gap locations (BED format), per-chromosome continuity metrics, corrected N50 values, GCI scores by chromosome and genome-wide, and coverage depth plots.
- **Advantages over CRAQ and T2T-polish**: GCI shows lower false positive rates when tested on CHM13 human reference assemblies. It specifically targets assembly continuity issues rather than base-level polishing needs.
- **Installation**: Download precompiled binaries from GitHub releases or install via Bioconda (`conda install -c bioconda gci`). Requires long-read aligners (minimap2, pbmm2) to be installed separately.

## Pitfalls

- **Insufficient Read Depth**: GCI requires sufficient long-read coverage (minimum 10-20x recommended) to reliably estimate coverage depth. Low coverage leads to false positive gap calls due to random sampling.
- **Read Length Requirements**: Short reads may not span assembly gaps properly. PacBio HiFi reads (10-15kb) or ONT reads (10kb+) are recommended. Reads shorter than typical gap sizes will underestimate gap locations.
- **Chimeric Alignments**: Some long reads contain chimeric alignments that can create false low-coverage regions. GCI includes filtering steps to remove these, but highly repetitive assemblies may still have issues.
- **Aligner Selection**: Choose the correct aligner for your read type: pbmm2 for PacBio HiFi, minimap2 for Oxford Nanopore, ngmlr for older PacBio CLR reads. Using the wrong aligner degrades mapping accuracy.
- **Reference Polishing Effects**: Artificially filling gaps (e.g., by manual curation) before running GCI will inflate metrics. GCI is designed to evaluate raw assembly quality, not post-curation results.
- **Memory Requirements**: For large genomes (human-size), GCI requires 16GB+ RAM due to coverage depth calculations across millions of base pairs.

## Examples

### Basic continuity assessment
**Args:** `gci -a assembly.fasta -r pacbio_hifi.fastq.gz -o gci_output -t 16`
**Explanation:** The standard GCI command takes an assembly and PacBio HiFi reads, outputs results to gci_output directory using 16 threads. GCI automatically detects the best aligner for HiFi reads (pbmm2). Output includes GCI scores, gap locations, and corrected N50 metrics.

### Assess ONT data assembly
**Args:** `gci -a assembly.fasta -r ont_fastq.gz -o ont_gci -t 16 --aligner minimap2`
**Explanation:** For Oxford Nanopore reads, explicitly specify minimap2 as the aligner. GCI will use minimap2's ont-specific presets for optimal alignment of nanopore data.

### Chromosome-specific evaluation
**Args:** `gci -a assembly.fasta -r hifi_reads.fastq.gz -o gci_chr -t 16 --region chr1:1-250000000`
**Explanation:** The --region flag limits analysis to a specific chromosome or genomic region. This is useful when you want detailed analysis of problematic chromosomes or when working with very large genomes where full analysis is time-consuming.

### Compare two assemblies
**Args:** `gci -a assembly_v1.fasta -r reads.fastq.gz -o asm1 && gci -a assembly_v2.fasta -r reads.fastq.gz -o asm2 && cat asm1/gci_score.txt asm2/gci_score.txt`
**Explanation:** Run GCI independently on two assemblies (e.g., before and after gap-filling), then compare the GCI scores and corrected N50 values to quantify improvement. The GCI score difference directly reflects continuity improvement.

### Generate gap BED file for visualization
**Args:** `gci -a assembly.fasta -r reads.fastq.gz -o gci_output -t 16 && bedtools genomecov -i gci_output/gaps.bed -g assembly.fasta.fai`
**Explanation:** After GCI identifies gap locations, use bedtools to visualize coverage around gaps or to intersect with other genomic annotations (genes, repeats, centromeres) to understand what sequences are missing.

### Interpret GCI score
**Args:** `cat gci_output/gci_score.txt`
**Explanation:** The GCI score file contains: genome-wide GCI score (0-100), per-chromosome scores, corrected N50, number of gaps detected, and theoretical T2T score. Scores above 95 indicate near-T2T quality. Compare chromosome scores to identify which chromosomes need most improvement.
