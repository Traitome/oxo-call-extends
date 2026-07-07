---
name: dadi
category: population-genomics
description: Fit population genetic models using diffusion approximations to the allele frequency spectrum
tags: [dadi, population-genomics, demographic-inference, allele-frequency-spectrum, dfe, bioinformatics]
author: oxo-call-community
source_url: "https://bitbucket.org/gutenkunstlab/dadi"
---

## Concepts

- **Tool Overview**: dadi (v2.0.5+) is a Python library for population genetic analysis using diffusion approximations to the allele frequency spectrum (AFS).
- **Core Function**: Infers demographic history and natural selection from population genetic data by fitting models to the site frequency spectrum.
- **Input/Output**: Input: VCF files, allele frequency spectrum files (.fs). Output: Parameter estimates, model fits, demographic plots.
- **Key Features**: Supports 1D and 2D frequency spectra, demographic modeling, DFE (distribution of fitness effects) inference.
- **Optimization**: Uses NLopt for efficient parameter optimization with customizable bounds.
- **Installation**: `conda install -c bioconda dadi` or `pip install dadi`

## Pitfalls

- **Spectrum File**: AFS must be in dadi's native .fs format; use `dadi-cli` for VCF conversion.
- **Grid Points**: Sufficient grid points are needed for accurate integration; start with [40,50,60].
- **Parameter Bounds**: Carefully set lower and upper bounds to prevent optimizer from exploring invalid regions.
- **Polarization**: Use unfolded spectrum with ancestral state information when available; fold otherwise.
- **Bootstrapping**: Always perform multiple optimization runs and bootstrap replicates for confidence intervals.

## Examples

### Generate frequency spectrum from VCF
**Args:** `dadi-cli GenerateFS --vcf input.vcf --popfile populations.txt --out-prefix output.fs`
**Explanation:** Create an allele frequency spectrum from a VCF file using dadi-cli.

### Infer demographic model (split with migration)
**Args:** `dadi-cli InferDM --fs data.fs --model split_mig --lbounds 1e-3 1e-3 0 0 --ubounds 100 100 1 10 --output-prefix results`
**Explanation:** Fit a split-with-migration demographic model to the frequency spectrum.

### Single population bottleneck model
**Args:** `dadi-cli InferDM --fs data.fs --model bottlegrowth --lbounds 1e-2 1e-2 0 0 --ubounds 100 100 5 5 --output-prefix bottleneck_results`
**Explanation:** Fit a three-epoch model (ancestral growth, bottleneck, recovery) to single population data.

### DFE inference
**Args:** `dadi-cli InferDFE --fs data.fs --cache-file cache.bpkl --dfe-gamma --output-prefix dfe_results`
**Explanation:** Infer the distribution of fitness effects using a gamma distribution model.

### Plot demographic model
**Args:** `dadi-cli PlotDemog --params results.params --output-prefix demog_plot`
**Explanation:** Generate visualization of the inferred demographic history.

### Simulate frequency spectrum
**Args:** `dadi-cli Simulate --model split_mig --params 2.0 0.5 0.1 1.0 --sample-sizes 20 20 --output-prefix simulated`
**Explanation:** Simulate an allele frequency spectrum under a specified demographic model.

### Godambe confidence intervals
**Args:** `dadi-cli Godambe --fs data.fs --params results.params --model split_mig --output-prefix confidence`
**Explanation:** Calculate Godambe information matrix-based confidence intervals for parameter estimates.
