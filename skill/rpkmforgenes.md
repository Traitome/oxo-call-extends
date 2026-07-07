---
name: rpkmforgenes
category: utility
description: Calculates RPKM (Reads Per Kilobase per Million mapped reads) gene expression values from a read mapping file (BAM) and a gene annotation, with species-specific read normalization.
tags: ["rpkmforgenes", "rpkm", "gene-expression", "rna-seq", "normalization", "species-specific"]
author: oxo-call-community
source_url: "https://github.com/danielramskold/S3_species-specific_sequencing"
---

## Concepts

- **Tool Overview**: rpkmforgenes (v1.0.1, Ramsköld / S3 project) is a Perl/Python tool for calculating RPKM gene expression values from a read mapping file (BAM/SAM) and a gene annotation. It is the canonical tool for the S3 (Species-Specific Sequencing) protocol and handles species-specific read normalization for metagenomic or species-mixed samples.
- **Core Function**: Takes a BAM file of reads, a gene annotation (GTF or BED), and an optional list of species-specific gene sets, and reports per-gene RPKM values. The "species-specific" mode normalizes the read counts by the per-species read fraction, allowing accurate expression estimation in metagenomic samples.
- **Algorithm**: Standard RPKM = (reads in gene) / (gene length in kb × total mapped reads in millions). The species-specific extension partitions the total mapped reads by species (via a per-species gene set) and computes per-species RPKM: the per-species total is the total reads mapped to that species' genes, not the global total. The output is normalized by the species' share of the library.
- **Input Format**: (1) A BAM file (coordinate-sorted); (2) a gene annotation (GTF or BED); (3) optional: a species-gene-set mapping (a TSV with `species<TAB>gene_list`); (4) optional: a list of genes to include. The species mapping is required for the species-specific RPKM mode.
- **Output Format**: A TSV with one row per gene: `gene_id, length, raw_count, rpkm, species_rpkm`. The `species_rpkm` column is filled only in species-specific mode. The output is sorted by `rpkm` (or `species_rpkm`) descending.
- **Use Case**: The standard expression-quantification step in the S3 species-specific sequencing protocol (canonical use case), RPKM calculation for a standard RNA-Seq experiment (when TPM/FPKM are not desired), metagenomic expression estimation where multiple species contribute to the library, and quick QC of gene coverage in a BAM file.

## Pitfalls

- **CRITICAL — The BAM must be coordinate-sorted and indexed**: rpkmforgenes uses a position-based index for fast gene-region counting. Pre-process with `samtools sort && samtools index`.
- **CRITICAL — Species-specific RPKM is NOT comparable across species**: A gene with `species_rpkm = 100` in species A and a gene with `species_rpkm = 100` in species B do not have the same expression level — the per-species totals differ. Use `species_rpkm` for within-species comparison only.
- **RPKM is NOT recommended for differential expression**: RPKM does not account for compositional bias; use raw counts + DESeq2/edgeR for differential analysis. RPKM is fine for visualization (e.g., heatmaps) and within-sample comparison.
- **The gene length is the EXON length, not the transcript length**: For genes with multiple isoforms, the gene length is the union of exons. The RPKM is computed against this union length. For isoform-specific expression, use Salmon or kallisto.
- **The default RPKM formula assumes paired-end reads are counted as pairs**: A paired-end fragment is counted as one read; a singleton (one mate unmapped) is silently skipped. Use `--count-singletons` to include singletons.
- **The species-gene-set mapping must be EXHAUSTIVE**: If a gene is not assigned to any species, it is silently dropped from the species-specific RPKM. Verify the mapping covers all expected genes with `awk '{print $1}' species_map.tsv | sort -u | wc -l` and compare to the total gene count.

## Examples

### Basic RPKM calculation
**Args:** `rpkmforgenes --bam aligned.bam --gtf annotation.gtf --out expression.tsv`
**Explanation:** `--bam` is the input BAM, `--gtf` is the gene annotation, `--out` is the output TSV. The output has one row per gene with `gene_id, length, raw_count, rpkm`.

### Species-specific RPKM
**Args:** `rpkmforgenes --bam aligned.bam --gtf annotation.gtf --species-map species_map.tsv --out expression_species.tsv`
**Explanation:** `--species-map` is a TSV with `species<TAB>gene_list` per line. The output includes a `species_rpkm` column with the per-species normalized RPKM. Useful for metagenomic samples.

### Use a BED annotation instead of GTF
**Args:** `rpkmforgenes --bam aligned.bam --bed genes.bed --out expression.tsv`
**Explanation:** `--bed` specifies a BED file (no GTF). The gene length is the BED record length. Useful when a GTF is unavailable.

### Filter by minimum read count
**Args:** `rpkmforgenes --bam aligned.bam --gtf annotation.gtf --min-count 10 --out expression_filtered.tsv`
**Explanation:** `--min-count 10` excludes genes with < 10 mapped reads. Reduces noise in the output and speeds up downstream analysis.

### Output a BED of expressed genes
**Args:** `rpkmforgenes --bam aligned.bam --gtf annotation.gtf --min-rpkm 1.0 --out-bed expressed.bed --out expression.tsv`
**Explanation:** `--min-rpkm 1.0 --out-bed expressed.bed` writes a BED file of genes with RPKM ≥ 1.0. Useful for IGV visualization of the expressed gene set.

### Include singletons in paired-end mode
**Args:** `rpkmforgenes --bam aligned.bam --gtf annotation.gtf --count-singletons --out expression.tsv`
**Explanation:** `--count-singletons` includes reads whose mate is unmapped. Default is to count only properly-paired reads. Useful when the library has a high singleton fraction.

### Run on a subset of chromosomes
**Args:** `samtools view -b aligned.bam chr1 chr2 > aligned_subset.bam && samtools index aligned_subset.bam && rpkmforgenes --bam aligned_subset.bam --gtf annotation.gtf --out expression_subset.tsv`
**Explanation:** Composite: pre-filter the BAM to specific chromosomes, then calculate RPKM. Useful for chromosome-level analyses or for running rpkmforgenes in parallel.
