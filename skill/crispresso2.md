---
name: crispresso2
category: genome-editing
description: Software pipeline for analysis of CRISPR-Cas9 genome editing experiments
tags: [crispresso2, crispr, genome-editing, cas9, indel, ngs]
author: oxo-call-community
source_url: "https://github.com/pinellolab/CRISPResso2"
---

## Concepts

- **Tool Overview**: CRISPResso2 is a software pipeline for rapid and intuitive interpretation of genome editing experiments from amplicon sequencing data.
- **Core Function**: Quantifies editing efficiency, identifies indels and substitutions, and characterizes editing outcomes at CRISPR target sites.
- **Input/Output**: Input: FASTQ files from amplicon sequencing, reference sequence, and sgRNA. Output: Editing statistics, alignment visualizations, and HTML report.
- **Multiple Modes**: Supports CRISPResso (single amplicon), CRISPRessoBatch (multiple samples), CRISPRessoPooled (pooled screens), and CRISPRessoCompare (comparison).
- **Allele Analysis**: Provides detailed allele frequency tables and nucleotide-level quantification of editing outcomes.
- **Prime Editing**: Supports prime editing analysis with CRISPRessoPulse for pegRNA experiments.

## Pitfalls

- **Amplicon Design**: Amplicon should include at least 50bp flanking the cut site for accurate alignment.
- **Quality Encoding**: Ensure FASTQ quality encoding is correct (Phred+33). Incorrect encoding causes alignment failures.
- **Reference Sequence**: Must include the full amplicon region. Partial references may cause misalignment.
- **sgRNA Position**: sgRNA position must be specified relative to the reference sequence for accurate cut site prediction.
- **Batch Processing**: Use CRISPRessoBatch for multiple samples with consistent parameters.

## Examples

### Basic CRISPR analysis
**Args:** `-r reference.fa -q reads_R1.fastq -q2 reads_R2.fastq -g GAGTCCGAGCAGAAGAAGAA --output-folder results/`
**Explanation:** Analyzes paired-end amplicon sequencing data for CRISPR editing at the specified sgRNA target site.

### Single-end reads analysis
**Args:** `-r reference.fa -q reads.fastq -g GAGTCCGAGCAGAAGAAGAA --output-folder results/`
**Explanation:** Analyzes single-end amplicon sequencing data for CRISPR editing efficiency.

### Batch processing multiple samples
**Args:** `CRISPRessoBatch --batch-settings batch_config.csv --output-folder batch_results/`
**Explanation:** Processes multiple samples in batch mode using a configuration file specifying FASTQ files and parameters.

### Compare editing conditions
**Args:** `CRISPRessoCompare --crispresso-output control/ --crispresso-output-2 treatment/ -o comparison/`
**Explanation:** Compares editing outcomes between control and treatment conditions, identifying significant differences.

### Prime editing analysis
**Args:** `CRISPRessoPulse -r reference.fa -q reads_R1.fastq -q2 reads_R2.fastq --peg-pegRNA pegRNA.fa --output-folder prime_results/`
**Explanation:** Analyzes prime editing experiments with pegRNA, quantifying prime editing efficiency and outcomes.

### Pooled screen analysis
**Args:** `CRISPRessoPooled -r reference.fa -q reads_R1.fastq -q2 reads_R2.fastq --sgRNA-file sgrnas.txt --output-folder pooled_results/`
**Explanation:** Analyzes pooled CRISPR screens with multiple sgRNAs, generating per-sgRNA editing statistics.

### Set quantification window
**Args:** `-r reference.fa -q reads.fastq -g GAGTCCGAGCAGAAGAAGAA --quantification-window 20 --output-folder results/`
**Explanation:** Limits quantification to a 20bp window around the cut site for more focused analysis.

### Output allele tables
**Args:** `-r reference.fa -q reads.fastq -g GAGTCCGAGCAGAAGAAGAA --allele-plot --output-folder results/`
**Explanation:** Generates detailed allele frequency tables and visualizations for comprehensive editing analysis.
