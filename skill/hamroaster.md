---
name: hamroaster
category: bioinformatics
description: hAMRoaster compares outputs from different AMR detection tools and provides performance metrics for antimicrobial resistance analysis.
tags: [hamroaster, AMR, antimicrobial-resistance, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ewissel/hAMRoaster"
---

## Concepts

- **AMR Detection Comparison**: hAMRoaster compares multiple AMR detection tools.

- **Performance Metrics**: Evaluates tool performance using various metrics.

- **Benchmarking**: Provides benchmarking for AMR detection methods.

- **Tool Integration**: Supports integration with multiple AMR tools.

- **Result Aggregation**: Aggregates results from different tools.

- **Quality Assessment**: Assesses the quality of AMR predictions.

## Pitfalls

- **Tool Compatibility**: Requires compatible AMR detection tools.

- **Reference Database**: Results depend on reference database quality.

- **Input Format**: Ensure correct input format for all tools.

- **Performance Variability**: Tool performance may vary by dataset.

- **Result Interpretation**: Carefully interpret comparison results.

## Examples

### Run hAMRoaster
**Args:** `hamroaster -i amr_results/ -o comparison/`
**Explanation:** Compares AMR detection results from multiple tools.

### With reference data
**Args:** `hamroaster -i amr_results/ -r reference.txt -o comparison/`
**Explanation:** Uses reference data for performance evaluation.

### Generate report
**Args:** `hamroaster -i amr_results/ -report -o report.html`
**Explanation:** Generates comprehensive comparison report.

### Batch processing
**Args:** `for d in */; do hamroaster -i $d -o ${d%/}_comparison/; done`
**Explanation:** Processes multiple result directories.

### Specific tools
**Args:** `hamroaster -i amr_results/ -t abricate,mlst -o comparison/`
**Explanation:** Compares specific AMR detection tools.

### Generate statistics
**Args:** `hamroaster -i amr_results/ -stats -o stats.txt`
**Explanation:** Generates performance statistics.

### Help command
**Args:** `hamroaster --help`
**Explanation:** Shows available options and usage information.