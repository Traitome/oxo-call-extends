---
name: rnanorm
category: expression
description: Apply common RNA-Seq normalization methods (TPM, FPKM, DESeq2 size factors, TMM, median-of-ratios) to a raw count matrix with a single command.
tags: ["rnanorm", "rna-seq", "normalization", "tpm", "fpkm", "deseq2", "tmm"]
author: oxo-call-community
source_url: "https://github.com/genialis/RNAnorm"
---

## Concepts

- **Tool Overview**: RNAnorm (v2.2.0, Genialis) is a Python CLI for applying common RNA-Seq normalization methods to a raw count matrix. It supports TPM, FPKM, RPKM, CPM, DESeq2 size factors, TMM (edgeR), and median-of-ratios. The output is a normalized count matrix in the same tab-separated format.
- **Core Function**: Reads a genes-by-samples count matrix (rows = gene/transcript IDs, columns = samples, first row = header, first column = IDs) and applies a user-selected normalization, optionally with log transformation, output filtering, and gene-length normalization. A second subcommand, `rnanorm-deseq2`, runs DESeq2 (via rpy2) for differential expression and emits the DESeq2-normalized matrix.
- **Algorithm**: Implements each normalization in pure Python (TPM/FPKM use the gene length; TMM uses edgeR's M-values; median-of-ratios is the DESeq2 approach). The DESeq2 subcommand delegates to R's `DESeq2` package via `rpy2`, which requires an R installation with `DESeq2` available.
- **Input Format**: A TSV count matrix with the structure: `gene_id<TAB>sample1<TAB>sample2<TAB>...`. Gene lengths are required for TPM/FPKM and can be passed as a second file (`--gene-lengths`) or auto-derived from a GTF. Sample names must be unique and contain no spaces.
- **Output Format**: A TSV with the same dimensions, with normalized values. By default the first column is the gene ID, but `--output-no-header` and `--output-no-index` are available for piping into downstream tools (e.g., edgeR's `read.delim`).
- **Use Case**: Normalizing a raw featureCounts / Salmon / kallisto matrix for cross-sample comparison without invoking the full DESeq2/edgeR pipelines, applying multiple normalizations side-by-side for comparison, and producing a log-CPM matrix for heatmap visualization (`pheatmap`).

## Pitfalls

- **CRITICAL — TPM/FPKM require accurate gene lengths**: The gene length for a multi-isoform gene is the union of all isoforms, not the longest isoform. RNAnorm uses the average gene length if multiple are given. For Salmon/kallisto output, use the Salmon-kallisto "effective length" (`--gene-lengths sal_len.tsv`) rather than the FASTA-derived length.
- **CRITICAL — TMM and median-of-ratios require integer counts**: These methods assume un-normalized integer counts (RNA-Seq reads). Applying them to a TPM/FPKM matrix produces nonsense negative-size factors. Always apply TMM/MoR to a raw `featureCounts` matrix, not to a normalized one.
- **Sample groups for TMM are inferred from the header**: The TMM normalization expects samples in a particular order (reference first, then others). RNAnorm uses the first column as reference; reorder with `awk` or `csvkit` if your experiment design requires a different reference.
- **DESeq2 subcommand requires R + rpy2 + DESeq2 installed**: The `rnanorm-deseq2` binary is a thin wrapper around R; if `R` is not on PATH or `DESeq2` is not installed, it fails with a confusing `rpy2` error. Pre-install with `conda install -c bioconda deseq2`.
- **Log transformation is base-2 by default** (`--log-base 2`); passing `--log` without `--log-base` may default to base-10 in older versions. Be explicit to avoid confusion across pipelines.
- **Output preserves the input order of genes and samples**: There is no `--sort-by-mean` or similar; sorting is the user's responsibility. Combine with `awk`/`csvkit` for downstream processing.

## Examples

### TPM normalization
**Args:** `rnanorm -m tpm -i counts.tsv -g gene_lengths.tsv -o counts.tpm.tsv`
**Explanation:** `-m tpm` selects TPM normalization; `-i` is the raw integer count matrix; `-g` is a two-column TSV of gene_id and gene length (in bp). Output `counts.tpm.tsv` has the same shape and is directly comparable across samples (column sums ≈ 1e6).

### FPKM normalization
**Args:** `rnanorm -m fpkm -i counts.tsv -g gene_lengths.tsv -o counts.fpkm.tsv`
**Explanation:** `-m fpkm` selects FPKM; requires both gene lengths and a `--read-length` argument (default 100 bp for single-end libraries). Use FPKM for cross-sample visualization; use TPM for cross-gene comparison within a sample.

### DESeq2 size factors (median-of-ratios)
**Args:** `rnanorm -m deseq2 -i counts.tsv -o counts.deseq2.tsv`
**Explanation:** `-m deseq2` computes the median-of-ratios size factors (no gene lengths needed). Output values are normalized counts that are appropriate input for differential expression (without further transformation). This is the recommended normalization for DESeq2/edgeR input.

### TMM (edgeR) normalization
**Args:** `rnanorm -m tmm -i counts.tsv -o counts.tmm.tsv`
**Explanation:** `-m tmm` implements the TMM method (Robinson & Oshlack, 2010). Output is a log-CPM matrix by default; pass `--no-log` to get raw CPM values. Suitable as input to edgeR's `glmQLFit` and similar.

### CPM normalization with log2
**Args:** `rnanorm -m cpm -i counts.tsv --log --log-base 2 -o counts.log2cpm.tsv`
**Explanation:** `-m cpm` produces counts-per-million; `--log --log-base 2` applies log2(CPM+1) for variance stabilization. The "+1" pseudo-count is the default; use `--pseudocount 0` to disable.

### Run full DESeq2 via rpy2
**Args:** `rnanorm-deseq2 -i counts.tsv --design "design.tsv" -o dds_results.tsv`
**Explanation:** `rnanorm-deseq2` is a separate subcommand that runs DESeq2 in R via rpy2; `--design` is a TSV with `sample,condition` columns. Output `dds_results.tsv` includes baseMeans, log2FoldChanges, p-values, and adjusted p-values per gene. Requires an R installation with `DESeq2` available.

### Normalize a Salmon quant.sf file
**Args:** `rnanorm -m tpm -i sal_quant/quant.sf -g tx_lengths.tsv -o sal_quant.tpm.tsv`
**Explanation:** Salmon's `quant.sf` files have a per-transcript format (Name, Length, EffectiveLength, TPM, NumReads). Convert to RNAnorm's expected two-column gene-length file first (`awk 'NR>1 {print $1"\t"$2}' sal_quant/quant.sf > tx_lengths.tsv`), then re-run with `-i sal_quant/quant.sf` and `-g` to obtain TPM values normalized with the Salmon effective length.
