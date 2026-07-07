---
name: find_circ
category: expression
description: "Detect head-to-tail spliced (back-spliced) sequencing reads indicative of circular RNA (circRNA) from RNA-seq data."
tags: [find_circ, expression, circRNA, circularRNA, RNA-seq, back-splicing, bioinformatics, splicing]
author: oxo-call-community
source_url: "https://github.com/marvin-jens/find_circ"
---

## Concepts

- **Tool Overview**: find_circ detects circular RNA (circRNA) in RNA-seq data by identifying back-spliced reads—junction reads where the sequencing read spans a head-to-tail splice (backbone junction) characteristic of circular RNAs.
- **Core Function**: Processes aligned BAM files to find circular RNA junction signatures characterized by non-canonical alignment patterns at circRNA backbones.
- **Input/Output**: Input: Genome-aligned BAM files from RNA-seq. Output: BED file with circRNA candidates, along with statistics and scoring metrics.
- **Algorithm**: IdentifiescircRNA by finding alignment signatures where reads span back-splice junctions. Requires unmapped reads to be re-aligned to identify circular junction spanning reads.
- **Key Features**: Back-splice junction detection, circRNA scoring, biological replicates support, visualization of circRNA candidates.
- **Installation**: `conda install -c bioconda find_circ` or clone from GitHub

## Pitfalls

- **Preprocessing Requirements**: find_circ requires specific preprocessing: unmapped reads must be extracted and re-aligned to a genome index using Bowtie2 with special flags (`--max multimap 20 --score-min C,-15,0`).
- **Paired-End vs Single-End**: Originally designed for paired-end RNA-seq; single-end data may have lower detection accuracy.
- **Multi-mapping Reads**: Using `--max multimap 20` allows reads to map to multiple locations, which is important for circRNAs that may share sequence with linear transcripts.
- **Annotation File**: The GTF/GFF annotation file with `-G` flag is used to filter candidate circRNAs against known splicing events, not to detect them.
- **False Positives**: Many circRNA callers including find_circ can have high false positive rates; validation with RT-PCR or Northern blot is recommended for important candidates.

## Examples

### Basic circRNA detection
**Args:** `find_circ.py -G annotation.gtf -f sample.bam -o circRNA_results.txt`
**Explanation:** Runs find_circ on a BAM file aligned with Bowtie2. The annotation file helps filter candidates but is not required for detection.

### With visualization
**Args:** `find_circ.py -G annotation.gtf -f sample.bam -v circRNA_candidates.bed -o circRNA_results.txt`
**Explanation:** The -v flag enables visualization of circRNA candidates in the specified BED file for downstream analysis.

### Complete workflow from BAM
**Args:** `find_circ.py -g hg38 -p sample_name -o results.txt alignments.bam`
**Explanation:** Full detection pipeline with reference genome (hg38), sample name prefix, and output file specification.

### With custom parameters
**Args:** `find_circ.py -G annotation.gtf -f sample.bam -m 20 -s C,-15,0 -o circRNA_results.txt`
**Explanation:** Custom minimum score (-m) and scoring function (-s) for Bowtie2 alignment during circRNA detection.

### Filtering high-confidence candidates
**Args:** `grep -P "^[^#].+	2	" circRNA_results.txt | awk '$5>=2'`
**Explanation:** After initial detection, filter results by: (1) circRNA backed by 2+ unique junction reads, (2) not in annotation, (3) expressed in biological replicates. This reduces false positives significantly.
