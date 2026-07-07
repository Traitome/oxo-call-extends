---
name: jvarkit-msa2vcf
category: alignment
description: Converts multiple sequence alignments (MSA) to VCF format.
tags: [jvarkit-msa2vcf, alignment, FASTA, VCF, MSA]
author: oxo-call-community
source_url: "https://lindenb.github.io/jvarkit/MsaToVcf.html"
---

## Concepts

- **Tool Overview**: jvarkit-msa2vcf (v201904251722) - Converts multiple sequence alignments to VCF variant format.
- **MSA Conversion**: Converts alignment data to variant calls.
- **Format Support**: Supports CLUSTAL and FASTA alignment formats.
- **VCF Generation**: Generates standard VCF output for variant analysis.
- **Reference Based**: Requires reference sequence for variant calling.
- **Multi-sample**: Handles multiple samples from alignment.

## Pitfalls

- **Alignment Quality**: Poor alignments produce poor variants.
- **Reference Matching**: Reference must match alignment sequences.
- **Indel Handling**: Complex indels may not be handled correctly.
- **Ambiguous Bases**: Ambiguous bases can cause issues.
- **Java Version**: Requires specific Java version.
- **Memory Usage**: Large alignments require significant memory.

## Examples

### Convert MSA to VCF
**Args:** `java -jar jvarkit-msa2vcf.jar -i alignment.fasta -r ref.fasta -o variants.vcf`
**Explanation:** Converts FASTA alignment to VCF using reference.

### CLUSTAL format input
**Args:** `java -jar jvarkit-msa2vcf.jar -i alignment.clustal -f clustal -r ref.fasta -o variants.vcf`
**Explanation:** Processes CLUSTAL format alignment.

### Include all positions
**Args:** `java -jar jvarkit-msa2vcf.jar -i alignment.fasta -r ref.fasta -o variants.vcf -all`
**Explanation:** Includes invariant positions in output.

### Quality filtering
**Args:** `java -jar jvarkit-msa2vcf.jar -i alignment.fasta -r ref.fasta -o variants.vcf -min-quality 20`
**Explanation:** Filters variants by quality score.

### Output genotype info
**Args:** `java -jar jvarkit-msa2vcf.jar -i alignment.fasta -r ref.fasta -o variants.vcf -genotype`
**Explanation:** Includes genotype information in VCF.

### Compressed output
**Args:** `java -jar jvarkit-msa2vcf.jar -i alignment.fasta -r ref.fasta -o variants.vcf.gz`
**Explanation:** Outputs compressed VCF file.