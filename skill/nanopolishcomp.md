---
name: nanopolishcomp
category: utility
description: NanopolishComp - Downstream analysis of Nanopolish output files
tags: [nanopolishcomp, utility, nanopolish, downstream, analysis, methylation]
author: oxo-call-community
source_url: "https://github.com/a-slide/NanopolishComp"
---

## Concepts

- **Tool Overview**: NanopolishComp v0.6.12 is a Python package for downstream analysis of Nanopolish output files. It processes methylation calls, variant calls, and other Nanopolish results.
- **Core Function**: Aggregates and summarizes Nanopolish output for methylation analysis, variant filtering, and data visualization.
- **Algorithm**: Parses Nanopolish TSV output files, performs statistical analysis, and generates summary reports. Supports quality filtering and aggregation.
- **Input Format**: Accepts Nanopolish output files (meth.tsv, variants.vcf) and can process multiple samples simultaneously.
- **Output**: Produces aggregated methylation statistics, filtered variant calls, and summary reports in TSV or CSV format.
- **Use Case**: Processing Nanopolish methylation calls, comparing methylation patterns across samples, and preparing data for downstream analysis.

## Pitfalls

- **Nanopolish Dependency**: Requires input in Nanopolish output format. Other tools' outputs may not be compatible.
- **Output Format**: Ensure Nanopolish was run with appropriate output options for compatibility.
- **Memory Usage**: Processing very large datasets may require significant memory. Consider chunked processing.
- **Quality Thresholds**: Default quality thresholds may need adjustment for specific datasets.
- **Sample Comparison**: When comparing samples, ensure consistent processing parameters.
- **Documentation**: Limited documentation. Refer to examples for usage patterns.

## Examples

### Process methylation calls
**Args:** `-i nanopolish_meth.tsv -o processed_meth.tsv`
**Explanation:** Processes Nanopolish methylation output and generates summary.

### Filter by quality
**Args:** `-i meth.tsv -o filtered.tsv -q 20`
**Explanation:** Filters methylation calls with quality score >= 20.

### Aggregate by region
**Args:** `-i meth.tsv -o aggregated.tsv --aggregate gene`
**Explanation:** Aggregates methylation calls by gene regions.

### Compare samples
**Args:** `-i sample1.tsv sample2.tsv -n Sample1 Sample2 -o comparison.tsv`
**Explanation:** Compares methylation patterns across multiple samples.

### Display help
**Args:** `nanopolishcomp --help`
**Explanation:** Shows all available options for processing Nanopolish output.
