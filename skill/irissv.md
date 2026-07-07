---
name: irissv
category: variant-calling
description: Iris - Software for refining insertion sequences in structural variant calls using consensus methods.
tags: [irissv, Iris, structural variants, SV refinement, insertion sequences]
author: oxo-call-community
source_url: "https://github.com/mkirsche/Iris"
---

## Concepts

- **Insertion Sequence Refinement**: irissv (v1.0.5) improves the accuracy of breakpoint positions and inserted sequence content in structural variant calls.
- **Consensus-based Improvement**: Uses multiple alignment and consensus methods to refine SV calls from various callers.
- **Integration with Jasmine**: Works alongside Jasmine for population-scale structural variant comparison and analysis.
- **Breakpoint Validation**: Validates and improves breakpoint accuracy using read-based evidence.
- **Sequence Resolution**: Determines the exact sequence of inserted material in structural variants.
- **Multi-sample Analysis**: Supports joint analysis across multiple individuals for improved variant calling.

## Pitfalls

- **Dependency Requirements**: Requires minimap2, racon, samtools, and Java 11+ for full functionality.
- **Input Format Sensitivity**: Expects specific VCF/BCF formats with proper SV annotations.
- **Computational Resources**: Large datasets may require significant memory and processing time.
- **Reference Genome Dependencies**: Results depend on the quality and version of the reference genome.
- **Variant Caller Compatibility**: Best results achieved with high-quality input SV calls from multiple callers.
- **Complex Rearrangements**: May struggle with highly complex structural variants involving multiple breakpoints.

## Examples

### Basic SV refinement
**Args:** `irissv -v input.vcf -r reference.fasta -o refined.vcf`
**Explanation:** Refines insertion sequences in the input VCF file using the reference genome.

### With long-read support
**Args:** `irissv -v input.vcf -r reference.fasta -b long_reads.bam -o refined.vcf`
**Explanation:** Incorporates long-read alignment data to improve insertion sequence resolution.

### Consensus mode with multiple callers
**Args:** `irissv -v caller1.vcf caller2.vcf caller3.vcf -r reference.fasta -o consensus.vcf`
**Explanation:** Merges and refines SV calls from multiple variant callers into a consensus set.

### Output detailed statistics
**Args:** `irissv -v input.vcf -r reference.fasta -o refined.vcf --stats stats.txt`
**Explanation:** Generates a statistics file summarizing refinement improvements and variant characteristics.

### Filter by variant type
**Args:** `irissv -v input.vcf -r reference.fasta -o insertions.vcf --type INS`
**Explanation:** Processes only insertion variants, ignoring deletions, inversions, and other SV types.

### Quality-based filtering
**Args:** `irissv -v input.vcf -r reference.fasta -o filtered.vcf --min-quality 30`
**Explanation:** Applies minimum quality threshold to filter low-confidence variants before refinement.