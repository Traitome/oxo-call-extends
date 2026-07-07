---
name: hmnfusion
category: variant-calling
description: HmnFusion performs fusion gene detection from DNA sequencing data, identifying chimeric transcripts and structural rearrangements.
tags: [hmnfusion, fusion-detection, structural-variation, dna-sequencing, cancer, gene-fusion]
author: oxo-call-community
source_url: "https://github.com/guillaume-gricourt/HmnFusion"
---

## Concepts

- **Tool Overview**: HmnFusion (v1.5.1) is a bioinformatics tool for detecting gene fusions from DNA sequencing data. It identifies chimeric transcripts and structural rearrangements that drive cancer development and progression.

- **Fusion Detection Algorithms**: HmnFusion uses split-read and discordant read pair analysis to detect fusion breakpoints. It analyzes aligned sequencing reads to identify reads spanning fusion junctions.

- **Input Requirements**: Accepts BAM files from whole-genome sequencing (WGS), whole-exome sequencing (WES), or targeted sequencing experiments. Requires indexed BAM files for efficient processing.

- **Output Formats**: Generates fusion calls in standard VCF format with detailed annotation including fusion partners, breakpoints, supporting read counts, and confidence scores.

- **Fusion Filtering**: Implements multiple filtering strategies to reduce false positives, including minimum supporting read thresholds, mapping quality filters, and strand bias checks.

- **Integration with Variant Callers**: Works alongside other variant calling tools to provide comprehensive structural variant analysis in cancer genomics pipelines.

## Pitfalls

- **BAM File Requirements**: Input BAM files must be properly aligned and indexed. Mismatched references or incomplete indexing will cause errors.

- **Coverage Limitations**: Low-coverage sequencing may miss low-abundance fusions. Recommended minimum coverage is 30x for reliable detection.

- **False Positives**: Repeat regions and paralogous genes can generate false fusion calls. Always validate predictions with orthogonal methods like RT-PCR.

- **Breakpoint Resolution**: The exact breakpoint position may have some uncertainty depending on read length and mapping quality.

- **RNA vs DNA Detection**: HmnFusion detects DNA-level rearrangements. For transcript-level fusion detection, consider RNA-seq based tools like Arriba or STAR-Fusion.

- **Reference Genome Compatibility**: Ensure the reference genome version matches what was used for alignment (e.g., hg19 vs hg38).

## Examples

### Run HmnFusion on tumor-normal pair
**Args:** `hmnfusion -t tumor.bam -n normal.bam -g hg38 -o fusion_calls.vcf`
**Explanation:** Detects fusions in tumor BAM with normal BAM for background filtering. Uses hg38 reference genome.

### Run with single BAM file
**Args:** `hmnfusion -t tumor.bam -g hg19 -o single_sample_fusions.vcf`
**Explanation:** Analyzes a single tumor sample without normal control. Suitable when no matched normal is available.

### Specify minimum supporting reads
**Args:** `hmnfusion -t tumor.bam -n normal.bam -g hg38 -min-reads 5 -o filtered_fusions.vcf`
**Explanation:** Requires at least 5 supporting reads for a fusion call, reducing false positives from low-coverage regions.

### Output detailed statistics
**Args:** `hmnfusion -t tumor.bam -g hg38 -stats -o fusions.vcf`
**Explanation:** Generates additional statistics file with read counts, mapping qualities, and fusion confidence metrics.

### Filter by fusion type
**Args:** `hmnfusion -t tumor.bam -g hg38 -filter-in-frame -o in_frame_fusions.vcf`
**Explanation:** Filters output to include only in-frame fusions, which are more likely to be functionally relevant.

### Run with custom reference annotations
**Args:** `hmnfusion -t tumor.bam -g hg38 -annotations custom_genes.gtf -o annotated_fusions.vcf`
**Explanation:** Uses custom gene annotation file for fusion partner identification instead of default annotations.

### Convert output to BED format
**Args:** `hmnfusion -t tumor.bam -g hg38 -format bed -o fusion_regions.bed`
**Explanation:** Outputs fusion breakpoints in BED format for visualization in genome browsers like IGV.