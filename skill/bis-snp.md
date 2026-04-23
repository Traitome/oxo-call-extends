---
name: bis-snp
category: epigenomics
description: Bisulfite-seq SNPs and cytosine methylation caller
tags: [bisulfite, snp, methylation, variant-calling]
author: oxo-call-community
source_url: "https://github.com/dnaase/Bis-tools"
---

## Concepts
- **Tool Overview**: Bis-SNP is a bisulfite-seq/NOMe-seq SNP and cytosine methylation caller that identifies genetic variants from bisulfite-treated DNA.
- **Bisulfite-aware SNP Calling**: Detects SNPs while accounting for bisulfite conversion (C→T changes).
- **Methylation Calling**: Simultaneously calls methylation status at cytosines.
- **Applications**: WGBS variant calling, methylation-aware genotyping, NOMe-seq analysis.

## Pitfalls
- **Bisulfite Conversion**: Must account for bisulfite conversion when calling variants.
- **Coverage**: Requires sufficient coverage for reliable SNP and methylation calls.

## Examples
### Call SNPs and methylation
**Args:** `java -jar BisSNP.jar -T BisulfiteGenotyper -R reference.fa -I aligned.bam -O variants.vcf`
**Explanation:** Calls SNPs and methylation from bisulfite alignment.
