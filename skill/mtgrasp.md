---
name: mtgrasp
category: assembly
description: reference-grade de novo animal mitochondrial genome assembly and standardization
tags: [mtgrasp, assembly, mitochondrial, mitogenome, metazoan]
author: oxo-call-community
source_url: "https://github.com/BirolLab/mtGrasp"
---

## Concepts

- **Tool Overview**: mtGrasp v1.1.9 is a streamlined Snakemake pipeline for assembling complete mitochondrial genomes from short-read data.
- **Core Function**: Performs read subsampling, de novo assembly, filtering, gap-filling, polishing, circularization, and standardization.
- **Performance**: Runs 2-7x faster and uses 3-4x less memory than GetOrganelle and MitoZ.
- **Multi-Step Pipeline**: Integrates abyss, bwa, blast, pilon, samtools, and mitos for complete workflow.
- **Output**: Produces reference-grade, standardized mitogenome annotations.
- **Applications**: Comparative genomics, phylogenetics, eDNA assay design, museum specimen analysis.

## Pitfalls

- **Short Reads Only**: Optimized for short-read libraries; long-read assemblers may be needed for challenging taxa.
- **Memory Requirements**: Moderate memory footprint but requires sufficient disk space for intermediate files.
- **Reference Dependencies**: May benefit from close reference for annotation guidance.
- **Complex Dependencies**: Requires many external tools (abyss, bwa, blast, mitos, etc.).
- **Species Coverage**: Primarily validated on metazoan taxa; performance may vary for other eukaryotes.
- **Completeness**: Assembled mitogenome completeness depends on sequencing depth and library quality.

## Examples

### Basic mitochondrial assembly
**Args:** `mtgrasp -i reads.fastq -o output_dir -s species_name`
**Explanation:** Assembles mitochondrial genome from short reads with species name for annotation.

### Specify thread count
**Args:** `mtgrasp -i lib1.fastq lib2.fastq -o results -t 16`
**Explanation:** Uses 16 threads for parallel processing steps.

### Run with existing config
**Args:** `mtgrasp --configfile config.yaml --until circularize`
**Explanation:** Runs pipeline up to circularization step using configuration file.

### Dry run to test
**Args:** `mtgrasp -i reads.fq -o test_out -n`
**Explanation:** Performs dry run without executing actual commands.

### View help
**Args:** `mtgrasp --help`
**Explanation:** Displays all available options and parameters.
