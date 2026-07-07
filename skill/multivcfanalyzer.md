---
name: multivcfanalyzer
category: variant-calling
description: MultiVCFAnalyzer is a VCF file post-processing tool tailored for ancient DNA (aDNA) variant analysis.
tags: [multivcfanalyzer, variant-calling, vcf, ancient-dna, adna, population-genomics]
author: oxo-call-community
source_url: "https://github.com/alexherbig/MultiVCFAnalyzer"
---

## Concepts

- **Tool Overview**: MultiVCFAnalyzer v0.89.0 is a VCF post-processing tool tailored for ancient DNA (aDNA) analysis. It combines multiple VCF files from GATK UnifiedGenotyper or similar callers into population-level genotype calls with downstream format outputs.
- **Core Function**: Reads multiple VCF files representing different samples or populations, performs filtering based on aDNA damage patterns, and produces combined genotype calls suitable for phylogenetics, population genetics, and SNP effect analysis.
- **Input Format**: Accepts VCF files from GATK UnifiedGenotyper or compatible variant callers. Requires reference genome and supports CRAM/BAM inputs for damage profiling.
- **Output**: Generates multiple output formats including FASTA alignments, SNP tables, kinship files, and summary statistics. Produces MultiVCFAnalyzer.json for MultiQC integration.
- **aDNA Features**: Specifically handles deamination patterns typical of ancient DNA, filters damage artifacts, and calculates authentication metrics for ancient samples.
- **Installation**: Available via Bioconda (`conda install -c bioconda multivcfanalyzer`). Requires Java (openjdk) and Python.

## Pitfalls

- **VCF Compatibility**: Designed for GATK UnifiedGenotyper output. Other callers may produce incompatible FORMAT fields or INFO annotations. Check output compatibility before analysis.
- **Damage Filtering**: Overly aggressive damage filtering may remove real variants in highly degraded samples. Balance between authentication and sensitivity based on sample quality.
- **Memory Usage**: Large population datasets with many samples require substantial RAM. Process in batches or subsample for initial exploration.
- **Reference Genome**: Must match the reference used for variant calling. Reference mismatch causes incorrect genotype calls and alignment issues in downstream analyses.
- **Missing Genotypes**: aDNA samples often have missing data due to low coverage. MultiVCFAnalyzer handles missing data but downstream tools may have specific requirements.
- **Multi-sample Coordination**: All input VCFs must contain the same variants and genomic positions. Coordinate VCF generation across samples before running MultiVCFAnalyzer.

## Examples

### Combine multiple VCF files
**Args:** `--input sample1.vcf sample2.vcf sample3.vcf --output population_analysis/`
**Explanation:** Combines three individual VCF files into a population-level analysis. Requires all samples to be mapped to the same reference genome.

### Filter for high-confidence ancient variants
**Args:** `--input ancient_samples/*.vcf --damage-filter --min-coverage 3 --out filtered/`
**Explanation:** Applies aDNA-specific damage filtering and requires minimum 3x coverage. Removes damage artifacts while retaining authentic ancient variants.

### Generate FASTA alignment for phylogenetics
**Args:** `--input *.vcf --reference ref.fa --output-format fasta --out phylogeny/`
**Explanation:** Produces FASTA alignment from VCF genotypes suitable for phylogenetic reconstruction tools like RAxML or IQ-TREE.

### Calculate pairwise nucleotide diversity
**Args:** `--input population.vcf --analysis pairwise-nucleotide-diversity --out nuc-div/`
**Explanation:** Computes nucleotide diversity (π) across the population. Important for population genetics and selection scans.

### Export to MultiQC format
**Args:** `--input samples.vcf --export-json --out multiqc_data/`
**Explanation:** Exports parsed VCF statistics as JSON for integration with MultiQC reports. Generates MultiVCFAnalyzer.json in standard format.

### Specify sample names for output
**Args:** `--input samples.vcf --sample-names "Sample1,Sample2,Sample3" --out named_output/`
**Explanation:** Overrides VCF sample names in output files. Useful when sample names in VCF are cryptic or contain special characters.
