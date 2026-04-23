---
name: break-point-inspector
category: variant-calling
description: Re-analyze BAM files to precisely determine break locations from Manta variant calls
tags: [break-point-inspector, sv, structural-variant, manta, breakpoint]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools"
---

## Concepts

- **Tool Overview**: Break Point Inspector (BPI) refines structural variant calls from Manta.
- **Core Function**: Re-analyzes BAM files to precisely determine break locations and filter false positives.
- **Input**: Manta VCF file and aligned BAM file.
- **Output**: Refined SV calls with precise breakpoints and improved filtering.
- **Features**: Increases accuracy of Manta calls by removing false positives.
- **Installation**: Install via bioconda: `conda install -c bioconda break-point-inspector`

## Pitfalls

- **Manta Required**: Requires Manta output as input; not standalone.
- **BAM Index**: Input BAM must be indexed with .bai file.
- **Memory Usage**: Large BAM files require significant memory.
- **Java Required**: Requires Java runtime environment.

## Examples

### Refine Manta SV calls
**Args:** `java -jar break-point-inspector.jar -vcf manta.vcf -bam aligned.bam -ref reference.fa -output refined.vcf`
**Explanation:** Refines Manta structural variant calls with precise breakpoints.

### Specify output directory
**Args:** `java -jar break-point-inspector.jar -vcf manta.vcf -bam aligned.bam -output_dir results/`
**Explanation:** Writes refined SV calls and analysis files to output directory.

### Set threads
**Args:** `java -jar break-point-inspector.jar -vcf manta.vcf -bam aligned.bam -threads 4 -output refined.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Display help
**Args:** `java -jar break-point-inspector.jar --help`
**Explanation:** Shows all available options and usage information.
