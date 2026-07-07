---
name: nanomath
category: utility
description: NanoMath - Mathematical utilities for Oxford Nanopore processing scripts
tags: [nanomath, utility, nanopore, math, statistics, library]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanomath"
---

## Concepts

- **Tool Overview**: NanoMath v1.4.0 is a Python library providing mathematical functions and utilities specifically designed for Oxford Nanopore sequencing data processing.
- **Core Function**: Offers statistical functions, quality score calculations, and utility functions used by other Nanopore tools in the NanoPack suite.
- **Algorithm**: Implements efficient statistical calculations optimized for sequencing data. Includes functions for mean, median, mode, and custom metrics.
- **Input Format**: Primarily used as a Python library import. Functions accept numeric arrays and sequences.
- **Output**: Returns computed statistics and transformed values for use in downstream analysis.
- **Use Case**: Used as a dependency by other Nanopore tools (NanoPack, NanoFilt, NanoGet), and can be imported into custom Python scripts.

## Pitfalls

- **Library Only**: Primarily designed as a Python library, not a standalone command-line tool.
- **Version Compatibility**: Ensure compatibility with dependent tools. API changes may affect downstream tools.
- **Data Types**: Functions expect specific input data types. Incorrect types may cause errors.
- **Memory Usage**: Processing very large arrays may require careful memory management.
- **Unit Testing**: Functions should be tested with edge cases before production use.
- **Documentation**: Limited standalone documentation. Refer to source code for detailed usage.

## Examples

### Import and use in Python
**Args:** `from nanomath import mean_qscore, median_length`
**Explanation:** Import functions for quality score and length calculations.

### Calculate mean quality
**Args:** `mean_qscore(quality_scores)`
**Explanation:** Computes mean quality score from array of phred scores.

### Calculate median length
**Args:** `median_length(read_lengths)`
**Explanation:** Computes median read length from array of lengths.

### Compute statistics
**Args:** `from nanomath import statistics; stats = statistics(read_lengths)`
**Explanation:** Returns dictionary with mean, median, mode, and other statistics.

### Display help
**Args:** `python -c "import nanomath; help(nanomath)"`
**Explanation:** Shows available functions and their documentation.
