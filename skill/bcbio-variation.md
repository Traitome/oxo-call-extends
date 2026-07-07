---
name: bcbio-variation
category: variant-calling
description: bcbio-variation - Toolkit for analyzing genomic variation data, built on GATK with Clojure
tags: [bcbio-variation, variant-calling, GATK, Clojure, variant-analysis]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbio.variation"
---

## Concepts

- **Tool Overview**: bcbio-variation (v0.2.6) is a toolkit for analyzing genomic variation data, built on the GATK framework using Clojure for functional programming.
- **Core Function**: Provides utilities for variant calling, filtering, annotation, and comparison across multiple samples.
- **GATK Integration**: Leverages GATK for variant calling and quality filtering.
- **Clojure Based**: Built using Clojure for functional, concurrent processing.
- **Multi-sample Analysis**: Supports joint variant calling and comparison across cohorts.
- **Input/Output**: Accepts BAM/VCF files; outputs annotated VCF files with variant statistics.
- **Installation**: `conda install -c bioconda bcbio-variation`.

## Pitfalls

- **GATK Dependency**: Requires GATK to be installed and configured.
- **Java Requirements**: Requires Java 8 or higher with sufficient heap memory.
- **Reference Data**: Requires indexed reference genome and associated files.
- **Version Compatibility**: Ensure compatibility with GATK version.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic variant calling
**Args:** `bcbio_variation call -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants from aligned BAM file using GATK.

### Joint calling multiple samples
**Args:** `bcbio_variation call -i sample1.bam sample2.bam -r reference.fasta -o joint.vcf`
**Explanation:** Performs joint variant calling across multiple samples.

### Variant filtering
**Args:** `bcbio_variation filter -i variants.vcf -o filtered.vcf -q 30`
**Explanation:** Filters variants with quality score below 30.

### Variant comparison
**Args:** `bcbio_variation compare -i variants1.vcf variants2.vcf -o comparison.txt`
**Explanation:** Compares variants between two VCF files.

### Annotate variants
**Args:** `bcbio_variation annotate -i variants.vcf -d dbnsfp -o annotated.vcf`
**Explanation:** Annotates variants with functional prediction scores.

### Variant recalibration
**Args:** `bcbio_variation recalibrate -i variants.vcf -r reference.fasta -o recalibrated.vcf`
**Explanation:** Performs variant quality score recalibration (VQSR).

### Display help
**Args:** `bcbio_variation --help`
**Explanation:** Shows all available command-line options and usage information.