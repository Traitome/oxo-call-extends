---
name: flaimapper
category: alignment
description: "FlaiMapper is a tool for detecting small non-coding RNA derived fragments in small RNA-Seq data, identifying tRNA and rRNA derived fragments."
tags: [flaimapper, alignment, small-rna, trna, rrna, fragments, bioinformatics, sequencing]
author: oxo-call-community
source_url: "https://github.com/yhoogstrate/flaimapper/"
---

## Concepts
- **Tool Overview**: FlaiMapper detects small ncRNA derived fragments in small RNA-Seq data, specifically identifying tRNA-derived fragments (tRFs), rRNA-derived fragments (rRFs), and other small RNA fragments.
- **Core Function**: Maps small RNA sequencing reads to reference tRNA and rRNA sequences to identify fragment origins and characteristics.
- **Input/Output**: Input: FASTQ files from small RNA sequencing, reference tRNA/rRNA databases. Output: Fragment annotations, abundance counts, genomic locations.
- **Fragment Types**: Identifies tRF-5, tRF-3, tRF-1, and tiRNA (tRNA halves) based on cleavage sites and fragment lengths.
- **Mapping Strategy**: Uses Bowtie/Bowtie2 for sensitive alignment with configurable mismatch tolerance.
- **Quantification**: Provides per-fragment abundance counts normalized by library size for differential expression analysis.
- **Installation**: `conda install -c bioconda flaimapper` or clone from GitHub. Requires Python 3.x, Bowtie/Bowtie2, SAMtools.

## Pitfalls
- **Reference Database Selection**: Must use appropriate tRNA/rRNA reference databases. Incomplete references miss novel fragments.
- **Adapter Trimming**: Raw reads must have adapters trimmed before mapping. Adapter sequences cause mapping failures.
- **Multi-mapping Reads**: Reads mapping to multiple locations require careful handling to avoid double-counting.
- **Fragment Size Thresholds**: Default size filters may exclude biologically relevant fragments. Adjust based on experimental design.
- **rRNA Contamination**: High rRNA contamination can overwhelm true small RNA signals. rRNA depletion recommended during library prep.
- **Strand Specificity**: Strand-specific protocols require proper strand handling during mapping and quantification.

## Examples
### Basic FlaiMapper analysis
**Args:** `flaimapper -i sample.fastq -o results/ -r trna_ref.fasta -a bowtie_index`
**Explanation:** Runs FlaiMapper on small RNA-Seq reads, mapping against tRNA reference and generating fragment annotations.

### Include rRNA reference
**Args:** `flaimapper -i sample.fastq -o results/ -r trna_ref.fasta -rrna rrna_ref.fasta -a bowtie_index`
**Explanation:** Adds rRNA reference to detect both tRNA and rRNA derived fragments.

### Custom fragment size range
**Args:** `flaimapper -i sample.fastq -o results/ -r trna_ref.fasta -a bowtie_index --min-size 18 --max-size 50`
**Explanation:** Sets custom fragment size range (18-50 nt) to focus on specific fragment populations.

### Strand-specific analysis
**Args:** `flaimapper -i sample.fastq -o results/ -r trna_ref.fasta -a bowtie_index --strand-specific`
**Explanation:** Enables strand-specific mapping for strand-specific library preparation protocols.

### Generate visualization
**Args:** `flaimapper -i sample.fastq -o results/ -r trna_ref.fasta -a bowtie_index --plot`
**Explanation:** Generates visualization plots showing fragment size distributions and genomic origins.
