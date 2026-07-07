---
name: fg-sra
category: formatting
description: "High-performance SRA-to-SAM/BAM/FASTQ converter."
tags: [fg-sra, formatting, SRA, SAM, BAM, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/fg-sra"
---

## Concepts

- **Tool Overview**: fg-sra is a high-performance tool that converts SRA data to SAM, BAM, FASTA, and FASTQ formats with multi-threaded processing.
- **Core Function**: Converts SRA archive data to various sequencing formats.
- **Input/Output**: Input: SRA accession or file. Output: SAM/BAM/FASTA/FASTQ.
- **Algorithm**: Uses efficient multi-threaded parsing for fast conversion.
- **Key Features**: High-performance, multi-threaded, format conversion, region filtering, quality quantization, reference caching.
- **Installation**: `conda install -c bioconda fg-sra`

## Pitfalls

- **Network Access**: Requires internet for SRA access.
- **Disk Space**: Large files require significant storage.
- **Access Limits**: NCBI may have access rate limits.
- **Format Compatibility**: Requires proper output format selection.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Convert to SAM
**Args:** `fg-sra SRR1234567 --output sam > reads.sam`
**Explanation:** Converts SRA to SAM format.

### Convert to FASTQ
**Args:** `fg-sra SRR1234567 --output fastq -o reads.fastq`
**Explanation:** Converts SRA to FASTQ format.

### Region filtering
**Args:** `fg-sra SRR1234567 --region chr1:1000000-2000000 --output bam > region.bam`
**Explanation:** Extracts specific genomic region.

### Multi-threaded
**Args:** `fg-sra SRR1234567 --output fastq -t 8 -o reads.fastq`
**Explanation:** Uses 8 threads for conversion.

### Quality quantization
**Args:** `fg-sra SRR1234567 --output fastq -q 2 -o reads.fastq`
**Explanation:** Quantizes quality scores to specified level.