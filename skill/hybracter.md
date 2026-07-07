---
name: hybracter
category: assembly
description: An automated long-read first bacterial genome assembly pipeline
tags: [hybracter, genome assembly, long-read, hybrid assembly]
author: oxo-call-community
source_url: "https://hybracter.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: Hybracter is an automated pipeline for complete bacterial genome assembly using long-read sequencing data.
- **Long-read First Approach**: Uses long reads (Nanopore/PacBio) as primary input with optional short-read polishing.
- **Hybrid Assembly**: Supports both hybrid (long + short reads) and long-read only assembly modes.
- **Plasmid Recovery**: Specialized in recovering small plasmids that are often missed by other assemblers.
- **Multiple Polishing Steps**: Includes Medaka for long-read polishing and POLCA for short-read polishing.
- **Installation**: `conda install -c bioconda hybracter`

## Pitfalls

- **Database Installation**: Requires prior database installation with `hybracter install`.
- **Read Quality**: Low-quality long reads can affect assembly accuracy; consider filtering with Filtlong.
- **Memory Requirements**: Assembly of large bacterial genomes requires significant memory resources.
- **Input Format**: Requires properly formatted CSV input file for multiple samples.
- **Medaka Model Selection**: Choose appropriate Medaka model based on sequencing chemistry (R9 vs R10).
- **Contaminant Removal**: Consider removing contaminants (e.g., lambda phage) before assembly.

## Examples

### Install databases
**Args:** `hybracter install`
**Explanation:** Installs required databases for assembly.

### Hybrid assembly with short and long reads
**Args:** `hybracter hybrid -i samples.csv -o output_dir -t 16`
**Explanation:** Runs hybrid assembly on multiple samples with 16 threads.

### Long-read only assembly
**Args:** `hybracter long -i samples.csv -o output_dir -t 16`
**Explanation:** Runs long-read only assembly without short-read polishing.

### Single sample hybrid assembly
**Args:** `hybracter hybrid-single -l long_reads.fastq.gz -s short_reads_R1.fastq.gz -s2 short_reads_R2.fastq.gz -o output_dir`
**Explanation:** Runs hybrid assembly on a single sample with explicit read files.

### Skip polishing steps
**Args:** `hybracter hybrid -i samples.csv -o output_dir --no_medaka --no_pypolca`
**Explanation:** Runs assembly without Medaka and POLCA polishing steps.