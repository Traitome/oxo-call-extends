---
name: sumstats-liftover
category: utility
description: Fast chain-based liftover for pandas DataFrames of summary statistics.
tags: [sumstats-liftover, liftover, pandas, gwas]
author: oxo-call-community
source_url: "https://github.com/Cloufield/sumstats-liftover"
---

## Concepts

- **Tool Overview**: sumstats-liftover (v1.1.0) performs fast chain-based liftover for summary statistics.
- **Core Function**: Lifts over genomic coordinates between genome assemblies.
- **Algorithm**: Uses chain files for efficient coordinate conversion.
- **Input/Output**: Input: pandas DataFrame with genomic positions; Output: Lifted-over coordinates.
- **Applications**: GWAS analysis, genome assembly conversion, coordinate mapping.
- **Installation**: `conda install -c bioconda sumstats-liftover` or pip install.

## Pitfalls

- **Chain File**: Requires appropriate chain file for liftover.
- **Coordinate Format**: Requires correct coordinate format.
- **Memory Requirements**: Large DataFrames require significant memory.
- **Performance**: Very large datasets can be slow.
- **Ambiguous Lifts**: Some positions may have ambiguous mappings.
- **Assembly Compatibility**: Requires compatible genome assemblies.

## Examples

### Display help
**Args:** `sumstats-liftover --help`
**Explanation:** Shows available options and usage information.

### Basic liftover
**Args:** `sumstats-liftover -i sumstats.tsv -c hg19ToHg38.over.chain -o sumstats_hg38.tsv`
**Explanation:** Lift over summary statistics from hg19 to hg38.

### With pandas
**Args:** `python -c "import sumstats_liftover; sumstats_liftover.liftover_df(df, 'hg19ToHg38.over.chain')"`
**Explanation:** Use Python API for liftover.

### Verbose mode
**Args:** `sumstats-liftover -i sumstats.tsv -c chain.chain -o output.tsv -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `sumstats-liftover -i sumstats.tsv -c chain.chain -o output.tsv --stats`
**Explanation:** Generate statistics about liftover.

### Batch processing
**Args:** `sumstats-liftover -i sumstats/ -c chain.chain -o results/`
**Explanation:** Process multiple summary statistics files together.

### Filter by quality
**Args:** `sumstats-liftover -i sumstats.tsv -c chain.chain -o output.tsv -q 0.9`
**Explanation:** Filter by liftover quality score.

### Include unmapped
**Args:** `sumstats-liftover -i sumstats.tsv -c chain.chain -o output.tsv --include-unmapped`
**Explanation:** Include unmapped positions in output.

### Generate report
**Args:** `sumstats-liftover -i sumstats.tsv -c chain.chain -o output.tsv --report`
**Explanation:** Generate comprehensive HTML report.
