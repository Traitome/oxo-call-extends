---
name: rmblast
category: utility
description: RMBlast is a RepeatMasker-compatible version of NCBI BLAST+ for repeat detection.
tags: [rmblast, utility, sequence-search, repeat-detection, blast-plus]
author: oxo-call-community
source_url: "https://www.repeatmasker.org/rmblast"
---

## Concepts

- **Tool Overview**: RMBlast is a RepeatMasker-compatible BLAST+ variant.
- **Core Function**: Detects repeat sequences via cross_match-like alignments.
- **Algorithm**: Modified NCBI BLAST+ with custom matrices and complexity-adjusted scoring.
- **Input Format**: Accepts FASTA query and FASTA subject (or pre-formatted BLAST DB).
- **Output**: Produces BLAST tabular/text alignments.
- **Use Case**: Repeat annotation, RepeatMasker pipelines.

## Pitfalls

- **RepeatMasker Required**: RMBlast is specifically modified for RepeatMasker; standard BLAST+ features may differ.
- **Custom Matrices**: Supports custom matrices but disables KA-Statistics (Karlin-Altschul).
- **Masklevel**: cross_match-like masklevel filtering enabled for low-complexity regions.
- **No K-mer Indexing**: RMBlast uses blastn algorithm; performance may differ from diamond or other fast aligners.
- **BLAST DB**: Subject can be a pre-formatted BLAST database built with `makeblastdb`.
- **Output Format**: Use `-outfmt 6` for tabular output parseable by downstream tools.

## Examples

### Display help
**Args:** `rmblastn -help`
**Explanation:** Shows RMBlast-specific options and supported flags.

### Basic search
**Args:** `rmblastn -query query.fasta -subject reference.fasta`
**Explanation:** Standard blastn-style alignment with RMBlast enhancements for repeat detection.

### Search against BLAST database
**Args:** `rmblastn -query query.fasta -db repeats_db`
**Explanation:** `-db` uses a pre-formatted BLAST database built with `makeblastdb` for faster search.

### Tabular output
**Args:** `rmblastn -query query.fasta -subject ref.fasta -outfmt 6 -out results.tsv`
**Explanation:** `-outfmt 6` produces 12-column tabular output; `-out` specifies output file.

### With custom matrix
**Args:** `rmblastn -query query.fasta -subject ref.fasta -matrix custom_matrix.txt`
**Explanation:** `-matrix` specifies a custom scoring matrix; KA-statistics are disabled with custom matrices.

### Stranded search
**Args:** `rmblastn -query query.fasta -subject ref.fasta -strand plus`
**Explanation:** `-strand plus` searches only forward strand; use `minus` for reverse only.

### Batch processing
**Args:** `rmblastn -query queries/*.fasta -db repeats_db -outfmt 6 -out all_results.tsv`
**Explanation:** Processes multiple query files against a pre-built database in one invocation.