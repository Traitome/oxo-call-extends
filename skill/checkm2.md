---
name: checkm2
category: qc
description: Assess metagenome-assembled genome quality using machine learning
tags: [checkm2, genome-quality, completeness, contamination, metagenomics, mag]
author: oxo-call-community
source_url: "https://github.com/chklovski/CheckM2"
---

## Concepts

- **Tool Overview**: CheckM2 assesses the quality of metagenome-assembled genomes (MAGs) using machine learning models, providing completeness and contamination estimates.
- **Core Function**: Predicts genome completeness and contamination from protein-coding gene features using either a general model (gradient boosting) or specific model (neural network).
- **Input/Output**: Input: Directory of genome FASTA files or protein FASTA files. Output: TSV file with completeness, contamination, and quality scores per genome.
- **Two Models**: General model (gradient boosting, works for all genomes) and specific model (neural network, better for well-represented lineages). Auto-selects best model by default.
- **Database Required**: Needs DIAMOND database for protein annotation. Download with `checkm2 database --download`.
- **Faster than CheckM1**: Significantly faster than the original CheckM, especially with multi-threading.

## Pitfalls

- **Database Required**: Must download DIAMOND database before first use. Set custom path with `--database_path` if not in default location.
- **Model Selection**: Default auto-selects between general and specific models. Use `--specific` for known lineages or `--general` for novel genomes.
- **Input Format**: Default expects nucleotide FASTA (.fna). Use `--genes` flag for protein FASTA input and `--extension` for non-default file extensions.
- **Empty Files**: Zero-byte files are detected and skipped automatically.
- **Memory Usage**: Use `--lowmem` flag to reduce DIAMOND memory consumption for large datasets.
- **Translation Table**: Default auto-detects. Use `--ttable 4` for Mycoplasma and other organisms using alternative genetic codes.

## Examples

### Basic quality assessment
**Args:** `predict --input ./bins/ --output-directory ./results/ -t 8`
**Explanation:** Assesses all genome files in the bins directory using 8 threads, auto-selects the best model per genome.

### Force specific model
**Args:** `predict --input ./bins/ --output-directory ./results/ --specific`
**Explanation:** Forces use of the neural network (specific) model, better for genomes from well-represented lineages.

### Output both models
**Args:** `predict --input ./bins/ --output-directory ./results/ --allmodels`
**Explanation:** Outputs predictions from both general and specific models for comparison.

### Process protein files
**Args:** `predict --input ./proteins/ --output-directory ./results/ --genes`
**Explanation:** Treats input as protein FASTA files instead of nucleotide, skipping gene prediction step.

### Download database
**Args:** `database --download --path /custom/db/path/`
**Explanation:** Downloads the DIAMOND database to a custom location for offline use.

### Set existing database location
**Args:** `database --setdblocation /path/to/checkm2_db.dmnd`
**Explanation:** Points CheckM2 to an existing database file without re-downloading.

### Resume interrupted run
**Args:** `predict --input ./bins/ --output-directory ./results/ --resume`
**Explanation:** Resumes a previously interrupted run by reusing intermediate files.

### Custom file extension
**Args:** `predict --input ./bins/ --output-directory ./results/ -x .fasta`
**Explanation:** Looks for .fasta files instead of default .fna extension in the input directory.

### Low memory mode
**Args:** `predict --input ./bins/ --output-directory ./results/ --lowmem -t 4`
**Explanation:** Reduces memory usage for DIAMOND search, useful on memory-constrained systems.

### Test installation
**Args:** `testrun`
**Explanation:** Runs quality prediction on three test genomes to verify CheckM2 installation is working correctly.
