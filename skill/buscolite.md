---
name: buscolite
category: qc
description: Simplified BUSCO analysis for gene prediction using pyhmmer/miniprot/augustus, with Python API and plotting
tags: [busco, qc, completeness, gene-prediction, annotation, funannotate]
author: oxo-call-community
source_url: "https://github.com/nextgenusfs/buscolite"
---

## Concepts

- **Tool Overview**: BUSCOlite is a simplified BUSCO analysis tool designed for gene prediction quality assessment. It runs miniprot/augustus-mediated genome predictions and pyhmmer HMM predictions using BUSCO v9, v10, or v12 databases. It is NOT a replacement for full BUSCO — it is optimized for integration into gene prediction pipelines like Funannotate.
- **Core Function**: Assesses completeness of genome assemblies or predicted protein sets using BUSCO ortholog databases. Implements the same filtering logic as BUSCO v6 for accurate results.
- **Two Analysis Modes**: `genome` mode (runs miniprot + augustus gene prediction on a genome FASTA, then HMM search) and `protein` mode (directly searches HMMs against a provided protein FASTA).
- **Dependencies**: augustus (note: many conda versions have non-functional PPX/--proteinprofile mode), miniprot, pyhmmer, pyfastx, natsort. Fewer dependencies than full BUSCO, making it easier to install alongside tools like Funannotate.
- **Plotting**: Includes `buscolite-plot` for generating publication-quality SVG plots from results with zero additional dependencies. Supports multi-sample comparison in a single plot.
- **Python API**: Can be used programmatically from within Python scripts, enabling integration into custom pipelines (e.g., Funannotate uses it to find core conserved marker genes for training ab-initio gene predictors).
- **Lineage Databases**: BUSCO models/lineages must be downloaded separately from the BUSCO website (v5 or v4 lineages). BUSCOlite does not provide an internal download method.
- **Installation**: `python -m pip install buscolite` (pip, not conda). Also available via `python -m pip install git+https://github.com/nextgenusfs/buscolite.git` for latest master.

## Pitfalls

- **Not a Full BUSCO Replacement**: For most general use cases, you should continue to use [BUSCO](https://busco.ezlab.org). BUSCOlite is specifically designed for gene prediction pipelines where minimal dependencies and Python API access are needed. It lacks some BUSCO v5 features like metaeuk integration.
- **Augustus PPX Mode**: Many augustus versions on conda have non-functional PPX/--proteinprofile mode, which BUSCOlite relies on for protein profile-based gene prediction. You may need to compile augustus from source to get a working PPX mode.
- **Lineage Database Not Included**: BUSCOlite does not download lineage databases automatically. You must manually download the appropriate lineage (e.g., fungi_odb12, eukaryota_odb10) from the BUSCO website and provide the path via `-l`.
- **Miniprot Output Limitation**: When using miniprot for gene prediction (genome mode), only amino acid (protein) sequences are output. Nucleotide sequences of predicted genes are not available, which may be a limitation for downstream analyses requiring CDS.
- **Database Version Compatibility**: Supports BUSCO v9, v10, and v12 databases. Ensure the lineage database version matches what BUSCOlite expects — using incompatible versions may cause HMM search failures.
- **Funannotate Integration**: BUSCOlite was originally written to replace BUSCO v2 within Funannotate (due to dependency conflicts). The metaeuk method used by BUSCO v5 does not produce complete gene models (outputs lowercase sequences not found in the genome), making it unsuitable for training ab-initio predictors — BUSCOlite's miniprot approach is preferred for this use case.

## Examples

### Genome mode analysis with augustus + miniprot
**Args:** `buscolite -i genome.fasta -o mygenome -m genome -l /path/to/fungi_odb12 -c 8`
**Explanation:** Runs BUSCOlite in genome mode: miniprot aligns BUSCO proteins to the genome, augustus refines gene predictions using protein profiles (PPX mode), then pyhmmer searches HMMs. `-c 8` uses 8 CPU cores. Output is a `.buscolite.json` results file and summary statistics.

### Protein mode analysis (pre-predicted proteins)
**Args:** `buscolite -i predicted_proteins.fa -o myproteins -m protein -l /path/to/eukaryota_odb10 -c 8`
**Explanation:** Directly searches BUSCO HMMs against a provided protein FASTA using pyhmmer. Skips gene prediction (no augustus/miniprot needed). Faster than genome mode — use when you already have a predicted proteome.

### Generate publication-quality plot from results
**Args:** `buscolite-plot mygenome.buscolite.json -o mygenome_plot.svg`
**Explanation:** Creates an SVG completeness plot (complete/single-copy/duplicated/fragmented/missing percentages) from a BUSCOlite JSON results file. Zero additional dependencies required — uses built-in SVG generation.

### Compare multiple samples in one plot
**Args:** `buscolite-plot sample1.buscolite.json sample2.buscolite.json sample3.buscolite.json -o comparison.svg`
**Explanation:** Generates a multi-sample comparison plot showing BUSCO completeness across all samples side-by-side. Useful for comparing assembly quality across different assemblies or annotation versions.

### Python API usage within a script
**Args:** `python -c "from buscolite import run_busco; run_busco(genome='genome.fa', outdir='out', mode='genome', lineage='fungi_odb12', cpus=8)"`
**Explanation:** Uses BUSCOlite's Python API to run analysis programmatically. This is how Funannotate integrates BUSCOlite — calling `run_busco()` directly from Python without subprocess overhead. Returns a results dictionary.

### Install via pip (recommended)
**Args:** `python -m pip install buscolite`
**Explanation:** Installs BUSCOlite and its Python dependencies (pyhmmer, pyfastx, natsort). Note: augustus and miniprot must be installed separately (via conda or system package manager) and available in `$PATH` for genome mode. For latest development version: `python -m pip install git+https://github.com/nextgenusfs/buscolite.git`.
