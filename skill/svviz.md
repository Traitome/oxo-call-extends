---
name: svviz
category: visualization
description: Interactive read visualizer for structural variants to validate and interpret SV calls.
tags: [svviz, structural-variants, visualization, validation]
author: oxo-call-community
source_url: "https://github.com/svviz/svviz"
---

## Concepts

- **Tool Overview**: svviz (v1.6.2) is an interactive visualizer for structural variants.
- **Core Function**: Visualizes reads supporting structural variant calls.
- **Algorithm**: Aligns reads to both reference and alternative alleles for comparison.
- **Input/Output**: Input: BAM file, SV VCF, reference genome; Output: Visualization.
- **Applications**: SV validation, variant interpretation, publication figures.
- **Installation**: `conda install -c bioconda svviz` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Performance**: Complex SVs may be slow to visualize.
- **Parameter Tuning**: Incorrect parameters affect visualization quality.
- **Alignment Quality**: Requires well-aligned BAM files.
- **Output Format**: Limited output formats may require conversion.
- **SV Complexity**: Very complex SVs may be hard to visualize.

## Examples

### Display help
**Args:** `svviz --help`
**Explanation:** Shows available options and usage information.

### Basic SV visualization
**Args:** `svviz -i sample.bam -v sv.vcf -r reference.fasta -o visualization/`
**Explanation:** Visualize SV calls from BAM and VCF.

### Interactive mode
**Args:** `svviz -i sample.bam -v sv.vcf -r reference.fasta`
**Explanation:** Launch interactive visualization.

### Verbose mode
**Args:** `svviz -i sample.bam -v sv.vcf -r reference.fasta -o visualization/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svviz -i sample.bam -v sv.vcf -r reference.fasta -o visualization/ --stats`
**Explanation:** Generate statistics about visualization.

### Batch processing
**Args:** `svviz -i bams/ -v sv.vcf -r reference.fasta -o visualizations/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `svviz -i sample.bam -v sv.vcf -r reference.fasta -o visualization/ -q 20`
**Explanation:** Filter SVs by quality score.

### Include all SV types
**Args:** `svviz -i sample.bam -v sv.vcf -r reference.fasta -o visualization/ --all-types`
**Explanation:** Visualize all types of structural variants.

### Generate report
**Args:** `svviz -i sample.bam -v sv.vcf -r reference.fasta -o visualization/ --report`
**Explanation:** Generate comprehensive HTML report.
