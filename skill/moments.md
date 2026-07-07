---
name: moments
category: utility
description: Evolutionary inference using SFS and LD statistics.
tags: [moments, utility, population-genetics]
author: oxo-call-community
source_url: "https://github.com/MomentsLD/moments"
---

## Concepts

- **Tool Overview**: moments v1.5.2 performs evolutionary inference using population genetics statistics.
- **Core Function**: Uses Site Frequency Spectrum (SFS) and Linkage Disequilibrium (LD) data.
- **SFS Analysis**: Analyzes allele frequency distributions.
- **LD Statistics**: Uses linkage disequilibrium information.
- **Demographic Inference**: Reconstructs population history.
- **Input/Output**: Accepts VCF or SFS files; outputs demographic parameters.

## Pitfalls

- **Population Genetics Specific**: Designed for population genetic data.
- **Memory Requirements**: Memory usage depends on data complexity.
- **Parameter Tuning**: May require parameter adjustment for optimal inference.
- **Data Quality**: Results depend on variant calling quality.
- **Computational Resources**: Complex models may require significant resources.
- **Model Assumptions**: Relies on population genetic model assumptions.

## Examples

### Run demographic inference
**Args:** `python -c "import moments; moments.Inference.optimize(model, data)"`
**Explanation:** Performs demographic inference from SFS.

### Load SFS data
**Args:** `python -c "sfs = moments.Spectrum.from_file('sfs.txt')"`
**Explanation:** Loads Site Frequency Spectrum data.

### Plot results
**Args:** `python -c "import moments; moments.Plotting.plot_sfs(sfs)"`
**Explanation:** Visualizes SFS data.

### Bootstrap analysis
**Args:** `python -c "import moments; moments.Inference.bootstrap(data, model)"`
**Explanation:** Performs bootstrap resampling.

### Batch processing
**Args:** `python script.py data/`
**Explanation:** Processes multiple datasets.