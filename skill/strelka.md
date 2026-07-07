---
name: strelka
category: variant-calling
description: Strelka calls somatic and germline small variants from mapped sequencing reads.
tags: [strelka, variant-calling, somatic, germline]
author: oxo-call-community
source_url: "https://github.com/Illumina/strelka"
---

## Concepts

- **Tool Overview**: strelka (v2.9.10) is a variant caller for identifying somatic and germline small variants from sequencing data.
- **Core Function**: Calls single nucleotide variants (SNVs) and small insertions/deletions (indels).
- **Algorithm**: Uses statistical modeling and machine learning for accurate variant calling.
- **Input/Output**: Input: BAM file with aligned reads; Output: VCF file with variant calls.
- **Applications**: Cancer genomics, germline variant discovery, clinical diagnostics.
- **Installation**: `conda install -c bioconda strelka` or download from GitHub.

## Pitfalls

- **Alignment Quality**: Poor alignment affects variant calling accuracy.
- **Read Coverage**: Low coverage affects sensitivity.
- **Base Quality**: Poor base quality affects variant confidence.
- **Contamination**: Sample contamination produces false variants.
- **Normal Sample**: For somatic calling, requires matched normal sample.
- **Memory Requirements**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `configureStrelkaSomaticWorkflow.py --help`
**Explanation:** Shows available options for somatic workflow.

### Somatic variant calling
**Args:** `configureStrelkaSomaticWorkflow.py --normalBam normal.bam --tumorBam tumor.bam --referenceFasta ref.fasta --runDir results/`
**Explanation:** Configure and run somatic variant calling.

### Germline variant calling
**Args:** `configureStrelkaGermlineWorkflow.py --bam input.bam --referenceFasta ref.fasta --runDir results/`
**Explanation:** Configure and run germline variant calling.

### Run workflow
**Args:** `python -m snakemake -s results/workflow/Snakefile --cores 8`
**Explanation:** Execute the configured workflow with 8 cores.

### With custom parameters
**Args:** `configureStrelkaSomaticWorkflow.py --normalBam normal.bam --tumorBam tumor.bam --referenceFasta ref.fasta --runDir results/ --minInputDepth 10`
**Explanation:** Set minimum input depth to 10.

### Verbose mode
**Args:** `configureStrelkaSomaticWorkflow.py --normalBam normal.bam --tumorBam tumor.bam --referenceFasta ref.fasta --runDir results/ -v`
**Explanation:** Run with detailed logging.

### Joint calling
**Args:** `configureStrelkaGermlineWorkflow.py --bam sample1.bam sample2.bam --referenceFasta ref.fasta --runDir results/`
**Explanation:** Perform joint variant calling on multiple samples.

### Filter by quality
**Args:** `configureStrelkaSomaticWorkflow.py --normalBam normal.bam --tumorBam tumor.bam --referenceFasta ref.fasta --runDir results/ --minQual 20`
**Explanation:** Set minimum variant quality to 20.

### Generate report
**Args:** `configureStrelkaSomaticWorkflow.py --normalBam normal.bam --tumorBam tumor.bam --referenceFasta ref.fasta --runDir results/ --enableReport`
**Explanation:** Generate comprehensive HTML report.
