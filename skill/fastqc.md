---
name: fastqc
category: qc
description: A quality control tool for high throughput sequence data that generates HTML reports with per-base quality scores, GC content, adapter contamination, and other metrics.
tags: [fastqc, qc, quality-control, fastq, sequencing, illumina]
author: oxo-call-community
source_url: "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/"
---

## Concepts

- **Tool Overview**: FastQC performs quality control on raw sequencing data (FASTQ/BAM/SAM). It generates an interactive HTML report and a summary text file with pass/warn/fail indicators for each quality module. Version 0.12.1.
- **Input Formats**: Accepts FASTQ (plain or gzipped), BAM, SAM, and Casava-format FASTQ files. Multiple files can be processed simultaneously. Gzipped FASTQ (.fastq.gz, .fq.gz) is processed directly without decompression.
- **Key Quality Modules**: Per-base sequence quality, per-sequence quality scores, per-base sequence content, GC content distribution, sequence length distribution, sequence duplication levels, overrepresented sequences, adapter content, and kmer content.
- **Output Files**: For each input, FastQC produces `<sample>_fastqc.html` (interactive report) and `<sample>_fastqc.zip` (data files including `fastqc_data.txt` for programmatic parsing). Use `-o` to specify output directory.
- **Batch Processing**: Pass multiple files to process in parallel (`-t` threads for parallel file processing). Combine with MultiQC to aggregate results from multiple samples.
- **Non-default Adapters**: If adapters are not detected automatically, provide a custom adapter file with `--adapters`. FastQC ships with common Illumina adapter sequences and detects them automatically for most modern datasets.
- **Installation**: `conda install -c bioconda fastqc`

## Pitfalls

- **Warnings Are Not Always Problems**: FastQC "FAIL" or "WARN" flags are set for general-purpose thresholds. RNA-seq data legitimately "fails" the per-base sequence content module (due to random priming bias). Interpret results in the context of your library type.
- **Paired-End Processing**: FastQC processes each file independently. Run on both R1 and R2 separately. FastQC does not do paired validation — use fastp or Trimmomatic for paired-end quality filtering.
- **Output Directory Must Exist**: If `-o outdir/` is specified, the directory must already exist. FastQC will not create it automatically.
- **Java Dependency**: FastQC is a Java application. It requires Java 11+ and may need sufficient Java heap space for very large files: set `_JAVA_OPTIONS=-Xmx2g` if it crashes on large inputs.
- **Duplicate Rate for WGS**: High duplication rates (>30%) are expected in PCR-amplified libraries. Low-input libraries often have high duplication — this is not necessarily a problem if you plan to mark/remove duplicates.

## Examples

### Quality check a single FASTQ file
**Args:** sample_R1.fastq.gz -o qc_reports/`
**Explanation:** Generates `sample_R1_fastqc.html` and `sample_R1_fastqc.zip` in the `qc_reports/` directory. The HTML report can be opened in any browser.

### Process multiple files in parallel
**Args:** `-t 4 -o qc_reports/ sample1_R1.fastq.gz sample1_R2.fastq.gz sample2_R1.fastq.gz sample2_R2.fastq.gz`
**Explanation:** `-t 4` processes 4 files simultaneously (one thread per file, not per CPU core). `-o` specifies output directory for all reports. Each file gets its own HTML and ZIP output.

### Run FastQC on a BAM file
**Args:** `-o qc_reports/ aligned.bam`
**Explanation:** FastQC can analyze BAM files directly. Useful to check quality after alignment without converting back to FASTQ. Reports sequencing quality from the BAM's SEQ and QUAL fields.

### Extract summary pass/warn/fail data
**Args:** `-o qc_reports/ -q sample.fastq.gz`
**Explanation:** `-q` (quiet) suppresses progress messages. After running, parse `qc_reports/sample_fastqc.zip/fastqc_data.txt` or use MultiQC to aggregate summary statistics across many samples.

### Use custom adapter list
**Args:** `--adapters /path/to/adapters.txt -o qc_reports/ sample.fastq.gz`
**Explanation:** Provide a tab-separated file with adapter names and sequences if your library uses non-standard adapters. FastQC's built-in adapter list covers most Illumina kits automatically.

### Disable slow modules for large datasets
**Args:** `--nogroup -t 8 -o qc_reports/ *.fastq.gz`
**Explanation:** `--nogroup` disables grouping of bases in per-base quality plots (useful for reads >75 bp to see per-position quality without averaging). Process all FASTQ files in the current directory using 8 parallel threads.
