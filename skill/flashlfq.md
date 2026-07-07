---
name: flashlfq
category: expression
description: "FlashLFQ is an ultrafast label-free quantification algorithm for mass spectrometry-based proteomics data analysis."
tags: [flashlfq, expression, proteomics, mass-spectrometry, quantification, bioinformatics, label-free]
author: oxo-call-community
source_url: "https://github.com/smith-chem-wisc/FlashLFQ"
---

## Concepts
- **Tool Overview**: FlashLFQ is a rapid label-free quantification tool for mass spectrometry proteomics, designed for high-throughput analysis of large datasets.
- **Core Function**: Identifies and quantifies peptides from LC-MS/MS data using a fast alignment algorithm and robust statistical scoring.
- **Input/Output**: Input: Mass spectrometry raw files (mzML, mzXML), FASTA protein database. Output: Peptide/protein abundance tables, identification results.
- **Speed Optimization**: Uses vectorized operations and parallel processing to achieve speeds up to 100x faster than traditional tools.
- **Feature Detection**: Implements noise filtering and peak detection algorithms optimized for label-free quantification.
- **Retention Time Alignment**: Uses dynamic programming for accurate retention time alignment across multiple runs.
- **Installation**: `conda install -c bioconda flashlfq` or download from GitHub. Requires Mono runtime for cross-platform support.

## Pitfalls
- **Raw File Format**: Supports mzML and mzXML formats. Other formats require conversion using ProteoWizard.
- **Database Requirements**: Requires FASTA database with decoy sequences for FDR calculation.
- **Retention Time Drift**: Significant retention time drift between runs affects quantification accuracy. Use alignment options.
- **Contaminant Removal**: Pre-process raw files to remove common contaminants (keratin, trypsin) before analysis.
- **Memory Requirements**: Very large datasets (>100 runs) may require increased memory allocation.
- **Mono Runtime**: Requires Mono for Linux/macOS. Ensure proper Mono installation for command-line usage.

## Examples
### Basic label-free quantification
**Args:** `flashlfq --raw-files *.mzML --database uniprot.fasta --output results/`
**Explanation:** Processes all mzML files in directory against FASTA database and outputs quantification results.

### Include decoy database
**Args:** `flashlfq --raw-files *.mzML --database uniprot.fasta --decoy-prefix DECOY_ --output results/`
**Explanation:** Uses custom decoy prefix for FDR calculation. Decoy sequences must be present in database.

### Custom precursor mass tolerance
**Args:** `flashlfq --raw-files *.mzML --database uniprot.fasta --precursor-tolerance 20 --output results/`
**Explanation:** Sets precursor mass tolerance to 20 ppm for matching peptides.

### Parallel processing with multiple threads
**Args:** `flashlfq --raw-files *.mzML --database uniprot.fasta --threads 8 --output results/`
**Explanation:** Uses 8 threads for parallel processing to speed up analysis.

### Generate detailed report
**Args:** `flashlfq --raw-files *.mzML --database uniprot.fasta --verbose --output results/`
**Explanation:** Generates detailed log file with processing statistics and identification metrics.
