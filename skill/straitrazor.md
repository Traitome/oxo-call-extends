---
name: straitrazor
category: variant-calling
description: The STR Allele Identification Tool for genotyping short tandem repeats.
tags: [straitrazor, str-genotyping, variant-calling, genetics]
author: oxo-call-community
source_url: "https://github.com/Ahhgust/STRaitRazor"
---

## Concepts

- **Tool Overview**: straitrazor (v3.0.1) is a tool for identifying and genotyping short tandem repeat (STR) alleles.
- **Core Function**: Extracts and analyzes STR alleles from sequencing data for genetic analysis.
- **Algorithm**: Uses pattern matching and allele calling to identify STR variations.
- **Input/Output**: Input: Sequencing reads or VCF file; Output: STR allele calls with genotypes.
- **Applications**: Forensic genetics, population genetics, disease association studies.
- **Installation**: `conda install -c bioconda straitrazor` or download from GitHub.

## Pitfalls

- **Repeat Complexity**: Complex repeat patterns are hard to genotype.
- **Read Quality**: Low-quality reads affect allele calling accuracy.
- **Reference Bias**: Reference genome may not contain all known alleles.
- **Stutter Artifacts**: PCR stutter affects allele sizing.
- **Allele Dropout**: Large alleles may be missed due to amplification bias.
- **Memory Requirements**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `straitrazor --help`
**Explanation:** Shows available options and usage information.

### Basic STR genotyping
**Args:** `straitrazor -i reads.fastq -o results.txt`
**Explanation:** Identify STR alleles from sequencing reads.

### With VCF input
**Args:** `straitrazor -i variants.vcf -o results.txt`
**Explanation:** Analyze STR variants from VCF file.

### Verbose mode
**Args:** `straitrazor -i reads.fastq -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `straitrazor -i reads.fastq -o results.txt --plot`
**Explanation:** Generate visualization of STR alleles.

### Custom STR panel
**Args:** `straitrazor -i reads.fastq -o results.txt -p str_panel.txt`
**Explanation:** Use custom STR panel for targeted analysis.

### Batch processing
**Args:** `straitrazor -i batch/ -o results/`
**Explanation:** Process multiple sequencing samples together.

### Quality filtering
**Args:** `straitrazor -i reads.fastq -o results.txt -q 20`
**Explanation:** Filter alleles by quality score threshold.

### Generate report
**Args:** `straitrazor -i reads.fastq -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
