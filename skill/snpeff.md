---
name: snpeff
category: variant-calling
description: Genetic variant annotation and effect prediction toolbox
tags: [snpeff, variant-calling, annotation, vcf, genome]
author: oxo-call-community
source_url: "http://snpeff.sourceforge.net/"
---

## Concepts

- **Tool Overview**: SnpEff (v5.4+) is a genetic variant annotation and effect prediction toolbox that annotates variants in VCF files and predicts their effects on genes (e.g., missense, nonsense, frameshift).
- **Core Function**: Annotates variants with functional consequences, gene names, protein changes, and conservation scores based on a pre-built genome database.
- **Input/Output**: Input: VCF file with variants. Output: Annotated VCF file with additional INFO fields for variant effects.
- **Algorithm**: Uses genome annotations (RefSeq, Ensembl) to determine the effect of each variant on genes, transcripts, and proteins.
- **Key Features**: Supports multiple species (human, mouse, fly, etc.), predicts functional effects, outputs HTML reports, and integrates with downstream analysis tools.
- **Installation**: `conda install -c bioconda snpeff`

## Pitfalls

- **Database Requirements**: Requires a pre-built database for the target organism. Download databases with `snpEff download <species>`.
- **Version Compatibility**: Database version must match SnpEff version. Outdated databases may cause errors.
- **Reference Genome**: Ensure the VCF uses the same reference genome build as the SnpEff database (e.g., hg38, GRCh38).
- **Memory Usage**: Annotating large VCF files requires significant memory. Increase heap size with `java -Xmx16g -jar snpEff.jar`.
- **Output Format**: Default output is annotated VCF. Use `-htmlStats` to generate HTML summary reports.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Annotate VCF file
**Args:** `eff -i vcf -o vcf -s summary.html GRCh38.105 variants.vcf > annotated.vcf`
**Explanation:** Annotates variants in variants.vcf using GRCh38.105 database, outputs annotated VCF and HTML summary report.

### Download database for human (GRCh38)
**Args:** `download GRCh38.105`
**Explanation:** Downloads and installs the GRCh38.105 database for human variant annotation.

### Annotate and generate HTML report
**Args:** `eff -i vcf -o vcf -htmlStats report.html GRCh38.105 variants.vcf > annotated.vcf`
**Explanation:** Annotates variants and generates a detailed HTML report with variant statistics.

### Annotate with custom database
**Args:** `eff -i vcf -o vcf my_custom_db variants.vcf > annotated.vcf`
**Explanation:** Uses a custom-built database for annotation. Custom databases can be created with SnpEff's build command.

### Generate summary statistics
**Args:** `stats -html -csv variants.vcf > stats.html`
**Explanation:** Generates HTML and CSV statistics from an annotated VCF file.

### Build custom database
**Args:** `build -gff3 -v my_genome.gff3 -d my_custom_db my_genome.fa`
**Explanation:** Builds a custom SnpEff database from a GFF3 annotation file and genome FASTA.

### Annotate with maximum memory
**Args:** `java -Xmx32g -jar snpEff.jar eff GRCh38.105 variants.vcf > annotated.vcf`
**Explanation:** Runs SnpEff with 32GB heap space for large VCF files.

### Filter by effect type
**Args:** `eff -filter "EFFECT=missense_variant" GRCh38.105 variants.vcf > missense.vcf`
**Explanation:** Filters variants to include only missense variants in the output.