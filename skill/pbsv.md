---
name: pbsv
category: qc
description: pbsv provides PacBio structural variant calling and analysis tools.
tags: [pbsv, qc, pacbio, structural-variants]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbsv calls structural variants.
- **Core Function**: Detects SVs from PacBio alignments.
- **Algorithm**: Uses signature-based SV detection.
- **Input Format**: Accepts BAM/SAM alignments.
- **Output**: Produces VCF variant calls.
- **Use Case**: Structural variant analysis, genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Alignment Quality**: Results depend on input alignments.
- **Coverage Requirements**: Requires sufficient coverage.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbsv --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `pbsv call alignments.bam variants.vcf`
**Explanation:** Calls structural variants from alignments.

### With reference
**Args:** `pbsv call alignments.bam reference.fasta variants.vcf`
**Explanation:** Uses reference genome for calling.

### Verbose mode
**Args:** `pbsv -v call alignments.bam variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbsv call -t 8 alignments.bam variants.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pbsv call alignments.bam variants.gvcf --gvcf`
**Explanation:** Outputs in GVCF format.

### Generate report
**Args:** `pbsv report variants.vcf -o report.html`
**Explanation:** Generates HTML report.