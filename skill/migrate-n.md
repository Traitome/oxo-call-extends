---
name: migrate-n
category: population-genomics
description: Population Genetics - Panmixia and Migration detection
tags: [migrate-n, population-genomics, migration]
author: oxo-call-community
source_url: "http://popgen.sc.fsu.edu/Migrate/Migrate-n.html"
---

## Concepts

- **Tool Overview**: Migrate-N v3.6.11 analyzes population genetics and detects migration patterns.
- **Core Function**: Detects panmixia and migration patterns among populations.
- **Migration Detection**: Identifies migration events between populations.
- **Population Differentiation**: Measures genetic differentiation between populations.
- **Input/Output**: Accepts population genetic data; outputs migration rates.
- **Coalescent Modeling**: Uses coalescent models for population inference.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Inference accuracy depends on input data quality.
- **Runtime**: Analysis can be time-consuming for complex models.
- **Model Complexity**: Complex models may require longer computation times.

## Examples

### Run migration analysis
**Args:** `migrate-n -i data.nex -o results/`
**Explanation:** Analyzes population migration patterns.

### With bootstrap
**Args:** `migrate-n -i data.nex -o results/ -b 100`
**Explanation:** Performs 100 bootstrap replicates.

### Custom model
**Args:** `migrate-n -i data.nex -o results/ -m 4`
**Explanation:** Uses migration model 4.

### Batch processing
**Args:** `migrate-n -i nexus/ -o results/`
**Explanation:** Processes multiple datasets in batch mode.

### Generate trees
**Args:** `migrate-n -i data.nex -o results/ -t`
**Explanation:** Generates population trees.