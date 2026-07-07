---
name: illumina-interop
category: qc
description: The Illumina InterOp libraries are a set of common routines used for reading and writing InterOp metric files. These metric files are binary files produced during a run providing detailed statistics about a run.
tags: [illumina-interop, qc, metrics, sequencing]
author: oxo-call-community
source_url: "http://illumina.github.io/interop/index.html"
---

## Concepts

- **Tool Overview**: illumina-interop (v1.9.0) - A library for reading and analyzing Illumina InterOp binary metric files generated during sequencing runs
- **Core Function**: Provides programmatic access to run metrics including cluster density, quality scores, phasing, and signal intensity
- **Input/Output**: Reads binary InterOp files from Illumina sequencer output directories, outputs structured metrics data
- **Installation**: `pip install interop` for Python, conda package available for C++ libraries
- **API Access**: Supports Python, C++, and C# bindings for flexible integration into analysis pipelines

## Pitfalls

- **File Compatibility**: InterOp format may vary between sequencer models and RTA versions
- **Python Version**: Requires Python 3.8-3.14 for binary builds; older versions need source compilation
- **Missing Files**: Incomplete run folders cause read failures; ensure all InterOp files are present
- **Memory Usage**: Loading all metrics for large runs can be memory-intensive
- **Metric Interpretation**: Understanding requires familiarity with Illumina sequencing metrics terminology

## Examples

### Load and summarize run metrics
**Args:** `python -c "from interop import py_interop_run_metrics, py_interop_summary; m=py_interop_run_metrics.run_metrics(); m.read('run_folder'); s=py_interop_summary.run_summary(); py_interop_summary.summarize_run_metrics(m,s); print(s.total_summary().yield_g())"`
**Explanation:** Loads all InterOp files and retrieves total yield in gigabases.

### Extract imaging metrics
**Args:** `from interop.core import imaging; df = pd.DataFrame(imaging('run_folder'))`
**Explanation:** Uses simplified interface to extract imaging metrics into a pandas DataFrame.

### Get specific metric types
**Args:** `from interop import py_interop_run; print(py_interop_run.to_string_metric_type(1))`
**Explanation:** Converts metric type enumeration to human-readable name (FWHM).

### Validate installation
**Args:** `python -m interop --test`
**Explanation:** Runs built-in tests to verify proper installation and configuration.

### Generate summary statistics
**Args:** `interop_summary run_folder/ --csv output.csv`
**Explanation:** Generates CSV summary of key run metrics including yield, Q30%, and aligned reads.

### List available metrics
**Args:** `from interop import py_interop_run; names = py_interop_run.string_vector(); py_interop_run.list_metric_type(names); print([names[i] for i in range(len(names))])`
**Explanation:** Lists all available metric types supported by the InterOp library.