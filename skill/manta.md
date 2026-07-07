---
name: manta
category: variant-calling
description: Structural variant and indel caller for mapped sequencing data
tags: [manta, variant-calling, structural-variants, indels]
author: oxo-call-community
source_url: "https://github.com/Illumina/manta"
---

## Concepts

- **Tool Overview**: manta v1.6.0 - Manta is a structural variant and indel caller for mapped sequencing data, optimized for Illumina sequencing data.
- **Core Function**: Detects structural variants (deletions, duplications, inversions, translocations) and indels from aligned sequencing reads.
- **Input/Output**: Input: BAM alignment files, reference genome; Output: VCF file with variant calls.
- **Installation**: `conda install -c bioconda manta`
- **SV Detection**: Uses paired-end and split-read information for SV detection.
- **Illumina Optimization**: Specifically optimized for Illumina sequencing data.

## Pitfalls

- **BAM Quality**: Poor quality alignments affect SV detection accuracy.
- **Read Length**: Short reads may miss complex SVs.
- **Coverage**: Low coverage regions may miss variants.
- **Reference Genome**: Must use the same reference for alignment and variant calling.
- **Memory Usage**: Large datasets require significant memory.
- **False Positives**: May produce false positive calls in repetitive regions.

## Examples

### Configure Manta
**Args:** `configManta.py --bam input.bam --referenceFasta ref.fa --runDir manta_run`
**Explanation:** Configures Manta workflow for SV calling.

### Paired tumor-normal
**Args:** `configManta.py --tumorBam tumor.bam --normalBam normal.bam --referenceFasta ref.fa --runDir manta_run`
**Explanation:** Configures paired tumor-normal analysis.

### Run Manta
**Args:** `python manta_run/runWorkflow.py`
**Explanation:** Executes the configured Manta workflow.

### With exome data
**Args:** `configManta.py --bam input.bam --referenceFasta ref.fa --exome --runDir manta_run`
**Explanation:** Configures for exome sequencing data.

### Quick mode
**Args:** `configManta.py --bam input.bam --referenceFasta ref.fa --runDir manta_run --quick`
**Explanation:** Runs in quick mode for faster analysis.

### Verbose logging
**Args:** `python manta_run/runWorkflow.py -v`
**Explanation:** Provides detailed logging during analysis.