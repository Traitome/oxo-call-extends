---
name: mutserve
category: variant-calling
description: Variant caller for the mitochondrial genome to detect homoplasmic and heteroplasmic sites
tags: [mutserve, variant-calling, mitochondrial, heteroplasmy, homoplasmy, mtDNA]
author: oxo-call-community
source_url: "https://github.com/seppinho/mutserve"
---

## Concepts

- **Tool Overview**: MutServe v2.0.3 is a specialized variant caller for mitochondrial DNA (mtDNA). It accurately detects both homoplasmic (100% frequency) and heteroplasmic (mixed population) variants in sequencing data, which is crucial for mitochondrial disease research and forensics.
- **Core Function**: Calls point mutations and small indels in the mitochondrial genome, quantifying the allele frequency of each variant. Distinguishes heteroplasmy levels from near-homoplasmy to low-level heteroplasmy.
- **Algorithm**: Uses statistical models for heteroplasmy detection at low variant allele frequencies. Applies filtering for common artifacts like alignment to nuclear mitochondrial sequences (NUMTs).
- **Input Format**: Accepts BAM files aligned to the mitochondrial reference (rCRS is the standard reference). Works with whole-genome sequencing, mtDNA-enriched sequencing, or amplicon sequencing data.
- **Output**: Produces VCF files with heteroplasmy levels (variant allele frequencies), quality scores, and coverage statistics. Includes per-site and per-sample summary metrics.
- **Use Case**: Mitochondrial disease diagnostics, population genetics of mtDNA, forensic science, and evolutionary biology studies of mitochondrial genomes.

## Pitfalls

- **Reference Choice**: The revised Cambridge Reference Sequence (rCRS) is the standard mtDNA reference. Using other references requires coordinate conversion.
- **NUMT Artifacts**: Nuclear mitochondrial pseudogenes (NUMTs) can cause false positive variant calls. MutServe includes filtering but be aware of this issue.
- **Heteroplasmy Threshold**: Detecting low-level heteroplasmy (below 1%) requires high coverage and appropriate statistical thresholds. Default settings may miss very low frequency variants.
- **Assembly Quality**: Draft assemblies with many gaps or misassemblies can confound variant calling. Use high-quality mtDNA assemblies when possible.
- **Strand Bias**: Mitochondrial genome is circular with biased replication. Some regions may show technical artifacts. Check strand balance metrics.
- **Phasing**: MutServe doesn't currently phase heteroplasmic variants. Allele-specific expression cannot be determined from standard sequencing.

## Examples

### Basic variant calling
**Args:** `call --reference rCRS.fasta --output output.vcf.gz --threads 4 *.bam`
**Explanation:** Standard MutServe workflow. Calls variants from all BAM files and outputs gzipped VCF with heteroplasmy information.

### Specify output directory
**Args:** `call -r ref.fa -o results/ -t 8 samples/*.bam`
**Explanation:** Sets output directory with `-o` and thread count with `-t`. Runs variant calling on all BAM files in parallel.

### Call with explicit genome version
**Args:** `call -r rCRS.fasta --build hg19 -o output.vcf *.bam`
**Explanation:** Explicitly specifies genome build for coordinate consistency. Important when working with multiple reference versions.

### Annotate variants
**Args:** `annotate --input variants.vcf --annotation rCRS_annot.txt --output annotated.tsv`
**Explanation:** Takes a VCF with variant positions and adds annotation from a reference annotation file, producing a tab-delimited table.

### Generate summary report
**Args:** `call -r ref.fa -o results/ --summary *.bam`
**Explanation:** The `--summary` flag generates an additional summary report with per-sample statistics and quality metrics.
