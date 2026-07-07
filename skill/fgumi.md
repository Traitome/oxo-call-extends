---
name: fgumi
category: utility
description: "High-performance tools for UMI-tagged sequencing data."
tags: [fgumi, utility, UMI, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/fgumi"
---

## Concepts

- **Tool Overview**: fgumi is a high-performance toolkit for processing UMI-tagged sequencing data, enabling accurate variant detection and consensus generation.
- **Core Function**: Processes UMI-tagged reads for accurate sequencing analysis.
- **Input/Output**: Input: Tagged sequencing reads. Output: Processed reads, consensus sequences, variants.
- **Algorithm**: Uses UMI patterns for error correction and consensus building.
- **Key Features**: High-performance, UMI processing, error correction, consensus generation, variant calling,分子标签处理。
- **Installation**: `conda install -c bioconda fgumi`

## Pitfalls

- **UMI Quality**: Requires high-quality UMI sequences.
- **Data Format**: Requires proper UMI tagging format.
- **Error Rates**: UMI error rates affect accuracy.
- **Memory Usage**: Large datasets may require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### UMI extraction
**Args:** `fgumi extract -i reads.fastq -o extracted.fastq`
**Explanation:** Extracts UMI sequences from reads.

### Consensus generation
**Args:** `fgumi consensus -i extracted.fastq -o consensus.fastq`
**Explanation:** Generates consensus from UMI groups.

### Error correction
**Args:** `fgumi correct -i extracted.fastq -o corrected.fastq`
**Explanation:** Corrects UMI errors.

### Variant calling
**Args:** `fgumi variants -i corrected.fastq -o variants.vcf`
**Explanation:** Calls variants using UMI data.

### Grouping reads
**Args:** `fgumi group -i reads.fastq -o grouped/`
**Explanation:** Groups reads by UMI.