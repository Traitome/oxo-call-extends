---
name: samtools
category: formatting
description: Suite of utilities for interacting with and post-processing short DNA sequence read alignments in SAM, BAM, and CRAM formats.
tags: [samtools, formatting, bam, sam, cram, alignment, sorting, indexing]
author: oxo-call-community
source_url: "https://www.htslib.org/doc/samtools.html"
---

## Concepts

- **Tool Overview**: SAMtools is the standard toolkit for manipulating high-throughput sequencing alignments stored in SAM/BAM/CRAM format. It is a collection of subcommands, each performing a distinct operation. Version 1.23.1.
- **Subcommand Architecture**: All operations are invoked as `samtools <subcommand> [options]`. Key subcommands: `view`, `sort`, `index`, `flagstat`, `stats`, `idxstats`, `merge`, `markdup`, `depth`, `coverage`, `faidx`, `mpileup`, `collate`, `fixmate`, `reheader`, `addreplacerg`.
- **SAM/BAM/CRAM Formats**: SAM is human-readable text; BAM is binary compressed SAM (enables fast random access); CRAM is reference-based compression (smallest files). Use `-b` for BAM output, `-C` for CRAM output.
- **Mandatory Sort+Index**: Random-access operations (`view` with region, `depth`, `tview`, `mpileup`) require a sorted and indexed BAM/CRAM. Index file (.bai for BAM, .csi for large references >512 Mb, .crai for CRAM) must exist and be newer than the BAM.
- **Threading**: Most subcommands accept `-@ N` to use N additional compression/decompression threads. For sort, `-@ 8 -m 2G` is a common production setting (8 threads, 2 GB RAM per thread for sorting).
- **FLAG Filtering**: SAM FLAGS are bitwise integers. Use `-f` (require bits) and `-F` (exclude bits) with `samtools view`. Common flag values: 4=unmapped, 1024=PCR duplicate, 256=secondary, 2048=supplementary. Use `samtools flags <value>` to decode.
- **Installation**: `conda install -c bioconda samtools`

## Pitfalls

- **CRITICAL - Subcommand First**: Every samtools command requires a subcommand as the FIRST argument. `samtools -b input.sam` is WRONG; `samtools view -b input.sam` is correct.
- **Sort Before Index**: Attempting to index an unsorted BAM fails or produces incorrect results. Always run `samtools sort` then `samtools index`.
- **CRAM Reference Required**: CRAM files require the reference genome to decode. Set `--reference ref.fa` or the `REF_PATH` environment variable.
- **Output Format**: Without `-b`/`-C`, `samtools view` outputs SAM (text) even if the input is BAM. Always specify `-b` for BAM output.
- **Deprecated rmdup**: `samtools rmdup` is deprecated; use `samtools markdup` instead. For paired-end data, run `samtools fixmate -m` before `samtools markdup` to add required mate score tags.
- **Large Reference CSI Index**: For references with contigs >512 Mb (e.g., some plant genomes), use `samtools index -c` to generate CSI (.csi) format index instead of BAI (.bai).

## Examples

### Convert SAM to sorted, indexed BAM
**Args:** `view -@ 8 -bS input.sam | samtools sort -@ 8 -o sorted.bam && samtools index sorted.bam`
**Explanation:** Converts SAM to BAM (`-b` binary, `-S` SAM input), uses 8 threads (`-@`), sorts by coordinate, then creates `.bai` index. Piping avoids writing an intermediate unsorted BAM to disk.

### Extract reads from a genomic region
**Args:** `view -b sorted.bam chr1:1000000-2000000 -o region.bam`
**Explanation:** Requires sorted+indexed BAM. Outputs only reads overlapping chr1:1000000–2000000 as BAM format. The sorted BAM must have a corresponding `.bai` index file in the same directory.

### Generate alignment statistics
**Args:** `flagstat sorted.bam`
**Explanation:** Reports total reads, mapped, properly paired, duplicates, etc. A quick quality check after alignment. For detailed per-flag and per-chromosome breakdowns, use `samtools stats` instead.

### Mark PCR duplicates in paired-end data
**Args:** `collate -o collated.bam input.bam && samtools fixmate -m collated.bam fixmate.bam && samtools sort -o sorted_fm.bam fixmate.bam && samtools markdup sorted_fm.bam markdup.bam`
**Explanation:** Full duplicate-marking pipeline for paired-end data: collate (group by name) → fixmate (add MC/ms tags needed by markdup) → sort (coordinate) → markdup (flag duplicates). Add `-r` to markdup to remove instead of flag duplicates.

### Merge multiple BAMs and re-index
**Args:** `merge -@ 8 -f merged.bam sample1.bam sample2.bam sample3.bam && samtools index merged.bam`
**Explanation:** Merges multiple coordinate-sorted BAMs into one (`-f` overwrites existing output file). All inputs must be sorted by coordinate and have compatible headers. Index the merged output for downstream use.

### Generate per-base depth with quality filters
**Args:** `depth -a -q 20 -Q 30 sorted.bam > depth.txt`
**Explanation:** `-a` includes positions with zero coverage (omit for sparse output); `-q 20` minimum base quality; `-Q 30` minimum mapping quality. Output: tab-separated chromosome, position, depth per line.

### Calculate coverage statistics per chromosome
**Args:** `coverage sorted.bam`
**Explanation:** Reports per-contig coverage metrics including number of reads, bases covered, mean depth, and percentage of bases covered. More informative than flagstat for assessing genome-wide coverage.

### Extract unmapped reads to FASTQ for reassembly
**Args:** `view -@ 4 -f 4 -F 264 -b sorted.bam | samtools fastq - > unmapped.fastq`
**Explanation:** `-f 4` requires the unmapped flag; `-F 264` excludes secondary (256) and supplementary (8) alignments to get only primary unmapped reads. Pipe to `samtools fastq` for FASTQ conversion.

### Index a FASTA reference
**Args:** `faidx reference.fa`
**Explanation:** Creates `reference.fa.fai` index required by GATK, bcftools, and samtools mpileup. Also enables subsequence extraction: `samtools faidx reference.fa chr1:1-1000` outputs that region as FASTA.

### Filter reads by mapping quality and flag
**Args:** `view -@ 4 -b -q 30 -F 1796 sorted.bam -o filtered.bam && samtools index filtered.bam`
**Explanation:** `-q 30` minimum MAPQ 30; `-F 1796` excludes unmapped (4), not primary (256), PCR duplicate (1024), and supplementary (512) reads. This is a standard filter before variant calling.

