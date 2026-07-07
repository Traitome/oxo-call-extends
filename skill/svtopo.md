---
name: svtopo
category: visualization
description: Complex structural variant visualization extraction tool for HiFi sequencing data.
tags: [svtopo, structural-variants, visualization, pacbio]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/HiFi-SVTopo"
---

## Concepts

- **Tool Overview**: svtopo (v0.3.0) extracts complex SV information from HiFi sequencing data.
- **Core Function**: Extracts structural variant signatures for visualization.
- **Algorithm**: Analyzes HiFi reads to identify complex SV patterns.
- **Input/Output**: Input: BAM file, SV VCF; Output: Extracted SV information.
- **Applications**: Complex SV analysis, visualization preparation.
- **Installation**: `conda install -c bioconda svtopo` or download from GitHub.

## Pitfalls

- **Input Quality**: Requires high-quality HiFi sequencing data.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing complex SVs can be slow.
- **Parameter Tuning**: Incorrect parameters affect extraction.
- **Alignment Quality**: Requires well-aligned BAM files.
- **SV Complexity**: Very complex SVs may be difficult to extract.

## Examples

### Display help
**Args:** `svtopo --help`
**Explanation:** Shows available options and usage information.

### Basic SV extraction
**Args:** `svtopo extract -i sample.bam -v sv.vcf -o sv_info.txt`
**Explanation:** Extract SV information from HiFi BAM.

### With reference
**Args:** `svtopo extract -i sample.bam -v sv.vcf -r reference.fasta -o sv_info.txt`
**Explanation:** Use reference genome for extraction.

### Verbose mode
**Args:** `svtopo extract -i sample.bam -v sv.vcf -o sv_info.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svtopo extract -i sample.bam -v sv.vcf -o sv_info.txt --stats`
**Explanation:** Generate statistics about extraction.

### Batch processing
**Args:** `svtopo extract -i bams/ -v sv.vcf -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `svtopo extract -i sample.bam -v sv.vcf -o sv_info.txt -q 20`
**Explanation:** Filter SVs by quality score.

### Include all SV types
**Args:** `svtopo extract -i sample.bam -v sv.vcf -o sv_info.txt --all-types`
**Explanation:** Extract all types of structural variants.

### Generate report
**Args:** `svtopo extract -i sample.bam -v sv.vcf -o sv_info.txt --report`
**Explanation:** Generate comprehensive extraction report.
