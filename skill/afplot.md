---
name: afplot
category: utility
description: Tool for plotting allele frequencies from VCF files across genomic regions
tags: [allele-frequency, vcf, plot, visualization, genomics]
author: oxo-call-community
source_url: "https://github.com/sndrtj/afplot"
---

## Concepts

- **Tool Overview**: afplot is a command-line tool for visualizing allele frequencies in VCF files, generating plots for specific regions or whole genomes.
- **Core Function**: Extracts allele frequency data from VCF files and creates publication-quality plots showing frequency distributions across genomic regions.
- **Input/Output**: Input: VCF file(s) with allele frequency information. Output: Plot images (PNG/PDF) and optional data tables.
- **Subcommands**: Two main modes: `regions` for specific genomic regions, `whole-genome` for genome-wide frequency plots.
- **Installation**: Install via bioconda: `conda install -c bioconda afplot`

## Pitfalls

- **AF Field Required**: VCF must contain AF (allele frequency) field in INFO column - will fail on VCFs without this annotation.
- **Memory Usage**: Whole-genome plots on large VCFs may require significant memory.
- **Chromosome Naming**: Ensure consistent chromosome naming (chr1 vs 1) between VCF and reference.
- **Multiple Samples**: For multi-sample VCFs, specify which sample's AF to plot or use combined AF.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available subcommands and general options.

### Plot specific region
**Args:** `regions input.vcf -r chr1:1000000-2000000 -o region_plot.png`
**Explanation:** Plots allele frequencies for a specific genomic region on chromosome 1.

### Whole genome plot
**Args:** `whole-genome input.vcf -o genome_af.png`
**Explanation:** Creates genome-wide allele frequency distribution plot.

### Plot multiple VCFs
**Args:** `whole-genome sample1.vcf sample2.vcf -l Sample1 Sample2 -o comparison.png`
**Explanation:** Compares allele frequencies across multiple samples with legend labels.

### Custom output format
**Args:** `regions input.vcf -r chr1:1-100000 -o plot.pdf --format pdf`
**Explanation:** Outputs plot in PDF format for publication quality.

### Specify window size
**Args:** `whole-genome input.vcf -w 1000000 -o genome_windowed.png`
**Explanation:** Uses 1Mb windows for smoothing allele frequency calculations.

### Plot with title and labels
**Args:** `regions input.vcf -r chr1:1-500000 -o plot.png --title "Chromosome 1 AF" --xlabel "Position" --ylabel "Allele Frequency"`
**Explanation:** Adds custom title and axis labels to the plot.

### Export data table
**Args:** `whole-genome input.vcf -o plot.png --output-data af_data.tsv`
**Explanation:** Saves the underlying frequency data to a TSV file for further analysis.
