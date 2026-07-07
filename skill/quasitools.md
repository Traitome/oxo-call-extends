---
name: quasitools
category: utility
description: QuasiTools is a collection of tools for analyzing viral quasispecies from sequencing data.
tags: [quasitools, utility, viral, quasispecies]
author: oxo-call-community
source_url: "https://github.com/phac-nml/quasitools/"
---

## Concepts

- **Tool Overview**: quasitools analyzes viral quasispecies.
- **Core Function**: Variant calling.
- **Algorithm**: Uses consensus methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces variants.
- **Use Case**: Viral sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Coverage**: Must be sufficient.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quasitools --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `quasitools call -i aligned.bam -o variants.vcf`
**Explanation:** Calls viral variants.

### With parameters
**Args:** `quasitools call -i aligned.bam -p params.yaml -o variants.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quasitools -v call -i aligned.bam -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quasitools -t 4 call -i aligned.bam -o variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Consensus sequence
**Args:** `quasitools consensus -i aligned.bam -o consensus.fasta`
**Explanation:** Generates consensus.

### Generate report
**Args:** `quasitools call -i aligned.bam -o variants.vcf --report report.html`
**Explanation:** Generates HTML report.