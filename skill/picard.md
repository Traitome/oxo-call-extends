---
name: picard
category: formatting
description: A set of Java command-line tools for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.
tags: [picard, formatting, bam, sam, vcf, duplicate-marking, sequencing-metrics]
author: oxo-call-community
source_url: "https://broadinstitute.github.io/picard/"
---

## Concepts

- **Tool Overview**: Picard is a collection of Java-based command-line tools for manipulating HTS data (SAM/BAM/CRAM/VCF). It is essential for GATK variant calling pipelines. Version 3.2.0.
- **CRITICAL - Tool-as-Subcommand Syntax**: Each Picard operation is a subcommand (tool name) passed as the first argument: `picard <ToolName> [options]`. Tool names are CamelCase, e.g., `MarkDuplicates`, `SortSam`, `CollectAlignmentSummaryMetrics`. In older versions: `java -jar picard.jar <ToolName>`.
- **Picard in GATK**: Picard tools are bundled inside GATK4. Invoke them as `gatk <ToolName>` for most tasks when GATK is installed.
- **Key Tools**: `MarkDuplicates` (flag/remove PCR duplicates), `SortSam` (sort by coordinate or name), `AddOrReplaceReadGroups` (fix/add @RG headers), `CollectAlignmentSummaryMetrics`, `CollectInsertSizeMetrics`, `CollectWgsMetrics`, `CreateSequenceDictionary`, `ReorderSam`, `FastqToSam`, `SamToFastq`.
- **Read Group Requirement**: GATK requires read group (@RG) headers with SM (sample), PL (platform), LB (library), and PU (platform unit) fields. Use `AddOrReplaceReadGroups` to add or fix these before GATK variant calling.
- **Java Memory**: For large BAMs, increase Java heap: `picard -Xmx16g MarkDuplicates ...`. The default heap may be insufficient for WGS samples.
- **Installation**: `conda install -c bioconda picard`

## Pitfalls

- **CRITICAL - Tool Name as First Argument**: `picard MarkDuplicates I=input.bam O=output.bam M=metrics.txt`. The tool name is ALWAYS the first positional argument. `picard --markDuplicates` is WRONG.
- **KEY=VALUE Syntax**: Many Picard tools use `KEY=VALUE` syntax instead of `--key value`. Both may work depending on version, but `I=input.bam O=output.bam` is the canonical form.
- **Duplicate Marking vs Removal**: `MarkDuplicates` by default only MARKS duplicates (sets FLAG bit 1024) without removing them. Add `REMOVE_DUPLICATES=true` to also remove them. Downstream tools like GATK can filter on the flag.
- **Coordinate Sort Required for MarkDuplicates**: Input BAM must be coordinate-sorted. `MarkDuplicates` will fail on name-sorted or unsorted BAMs.
- **Dictionary File**: GATK requires a sequence dictionary file (`.dict`) alongside the reference FASTA. Use `picard CreateSequenceDictionary R=ref.fa O=ref.dict` to create it.
- **Out of Memory Errors**: Add `TMP_DIR=/tmp/picard_tmp` and increase `-Xmx` for large samples: `picard -Xmx32g MarkDuplicates ...`.

## Examples

### Mark PCR duplicates
**Args:** `MarkDuplicates I=sorted.bam O=markdup.bam M=markdup_metrics.txt CREATE_INDEX=true`
**Explanation:** `I=` input sorted BAM; `O=` output with duplicates marked (FLAG 1024 set); `M=` metrics file with duplication rates; `CREATE_INDEX=true` automatically creates `.bai` index. Requires coordinate-sorted input.

### Add or replace read groups (required for GATK)
**Args:** `AddOrReplaceReadGroups I=sorted.bam O=rg_added.bam RGID=sample1 RGLB=lib1 RGPL=ILLUMINA RGPU=unit1 RGSM=sample1 CREATE_INDEX=true`
**Explanation:** Adds required read group tags. `RGID` is the read group ID; `RGLB` library name; `RGPL` platform (ILLUMINA/PACBIO/ONT); `RGPU` platform unit; `RGSM` sample name (must match VCF sample names). GATK will fail without proper @RG headers.

### Create sequence dictionary for reference
**Args:** `CreateSequenceDictionary R=reference.fa O=reference.dict`
**Explanation:** Creates the `.dict` file required by GATK alongside the FASTA. Only needed once per reference genome. GATK also requires `samtools faidx reference.fa` to create the `.fai` index.

### Collect alignment summary metrics
**Args:** `CollectAlignmentSummaryMetrics R=reference.fa I=sorted.bam O=alignment_metrics.txt`
**Explanation:** Reports total reads, aligned reads, PF reads, strand balance, chimeric reads, and more. Requires the reference FASTA. Output is tab-delimited; parseable by MultiQC.

### Collect insert size metrics for paired-end libraries
**Args:** `CollectInsertSizeMetrics I=sorted.bam O=insert_size_metrics.txt H=insert_size_histogram.pdf`
**Explanation:** Reports mean, median, and mode insert sizes and generates a histogram PDF. Important for detecting library preparation issues (e.g., over-fragmentation, large fragments). Requires sorted, paired-end BAM.

### Collect WGS coverage metrics
**Args:** `CollectWgsMetrics I=sorted.bam O=wgs_metrics.txt R=reference.fa MINIMUM_MAPPING_QUALITY=20 MINIMUM_BASE_QUALITY=20`
**Explanation:** Calculates genome-wide coverage including mean depth, % bases with ≥10×/30×, and uniformity. Filter by mapping and base quality to get high-confidence coverage estimates.

### Convert FASTQ to unaligned BAM (for GATK best practices)
**Args:** `FastqToSam F1=R1.fastq.gz F2=R2.fastq.gz O=unaligned.bam SM=sample1 PL=ILLUMINA LB=library1 RG=RG001`
**Explanation:** Creates an unaligned BAM (uBAM) from FASTQ files with read group information embedded. Required for the GATK4 best practices pre-processing workflow (FastqToSam → BWA → MergeBamAlignment → MarkDuplicates).
