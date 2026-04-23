---
name: advntr
category: variant-calling
description: Tool for genotyping Variable Number Tandem Repeats (VNTR) from sequence data using hidden Markov models
tags: [vntr, tandem-repeat, genotyping, str, repeat, hmm]
author: oxo-call-community
source_url: "https://github.com/mehrdadbakhtiari/adVNTR"
---

## Concepts

- **Tool Overview**: adVNTR uses hidden Markov models to genotype Variable Number Tandem Repeats (VNTRs), counting repeat units and detecting sequence variations in tandem repeat regions.
- **Core Function**: Genotypes VNTRs by modeling each repeat region with HMMs, accurately counting repeat unit numbers from aligned sequencing reads.
- **Input/Output**: Input: BAM file with aligned reads. Output: VNTR genotypes with repeat unit counts for each allele.
- **Sequencing Platforms**: Supports both Illumina short reads and PacBio long reads with platform-specific parameters.
- **Installation**: Install via bioconda: `conda install -c bioconda advntr`

## Pitfalls

- **Pre-aligned BAM Required**: Input must be a BAM file with reads already aligned to a reference genome containing VNTR annotations.
- **Reference Models**: Requires pre-trained VNTR models - download recommended loci datasets from the project website.
- **Read Length Limitations**: Accuracy depends on read length - 90bp reads achieve ~90% accuracy; longer reads improve results.
- **Frameshift Detection**: Use `--frameshift` flag to detect potential frameshift mutations in coding VNTRs.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for adVNTR genotyping.

### Genotype VNTRs from Illumina BAM
**Args:** `genotype --alignment_file aligned_reads.bam --working_directory ./output/`
**Explanation:** Genotypes all VNTRs in the recommended loci set from Illumina short-read data.

### Genotype VNTRs from PacBio data
**Args:** `genotype --alignment_file pacbio_reads.bam --working_directory ./output/ --pacbio`
**Explanation:** Genotypes VNTRs from PacBio long-read data using platform-specific parameters.

### Detect frameshift mutations
**Args:** `genotype --alignment_file aligned_reads.bam --working_directory ./output/ --frameshift`
**Explanation:** Genotypes VNTRs and specifically checks for frameshift mutations in coding regions.

### Genotype specific VNTR by ID
**Args:** `genotype --alignment_file aligned_reads.bam --working_directory ./output/ --vntr_id 12345`
**Explanation:** Genotypes only the specified VNTR locus, useful for targeted analysis.

### Genotype with GRCh38 reference
**Args:** `genotype --alignment_file aligned_hg38.bam --working_directory ./output/ --reference_model vntr_data_hg38/`
**Explanation:** Uses GRCh38-specific VNTR models for genotyping (requires hg38 model dataset).

### Batch process multiple samples
**Args:** `genotype --alignment_file sample1.bam --working_directory ./sample1/ && advntr genotype --alignment_file sample2.bam --working_directory ./sample2/`
**Explanation:** Process multiple BAM files sequentially, each with separate output directories.
