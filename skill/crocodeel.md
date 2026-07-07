---
name: crocodeel
category: metagenomics
description: CroCoDeEL detects cross-sample contamination in shotgun metagenomic data by identifying contamination sources and estimating pollution levels
tags: [crocodeel, metagenomics, contamination, well-to-well, SAM, BAM, species-abundance]
author: oxo-call-community
source_url: "https://github.com/metagenopolis/CroCoDeEL"
---

## Concepts

- **Tool Overview**: CroCoDeEL (v1.2.1+) detects cross-sample (well-to-well) contamination in shotgun metagenomic data.
- **Core Function**: Identifies contaminated samples, pinpoints contamination sources, and estimates contamination rates using only species abundance tables—no negative controls or plate maps required.
- **Algorithm**: (1) Input species abundance tables from metagenomic profiling. (2) For each sample pair, identify species forming a "contamination line" (linear relationship in scatter plot). (3) Extract 10 features from the contamination line. (4) Apply random forest classifier to determine contamination probability. (5) Output detailed contamination events and estimated rates.
- **Input/Output**: Accepts species abundance tables (TSV/CSV); outputs contamination_events.tsv with source, target, and estimated contamination level
- **Installation**: `pip install crocodeel` or `conda install -c bioconda crocodeel`

## Pitfalls

- **Species Abundance Format**: Input must contain sample names as rows and species as columns. Row names must exactly match between files for proper pairing.
- **No Negative Controls Needed**: Unlike other contamination tools, CroCoDeEL uses only sample-to-sample comparisons; negative controls can be included but are not required.
- **Detection Sensitivity**: Can detect contamination levels as low as 0.1%, making it suitable for low-level well-to-well leakage detection.

## Examples

### Basic contamination detection
**Args:** `crocodeel -i species_abundance.tsv -o contamination_results/`
**Explanation:** Run detection on species abundance table. Output includes contamination_events.tsv with identified contamination pairs.

### Specify output directory
**Args:** `crocodeel --abundance species_table.csv --output results/ --prefix experiment1`
**Explanation:** Set custom output directory and prefix for result files.

### Adjust contamination probability threshold
**Args:** `crocodeel -i species_abundance.tsv -o results/ --probability_threshold 0.7`
**Explanation:** Set minimum probability threshold for reporting contamination events. Higher values reduce false positives.

### View chain file format help
**Args:** `crocodeel view-chain --input chain.tsv`
**Explanation:** Display chain file in readable block-pair format for understanding sample relationships.

### Species abundance table format
**Args:** `crocodeel validate --abundance species_table.tsv`
**Explanation:** Validate input species abundance table format before running full analysis.

### Output interpretation
**Args:** `crocodeel -i species_abundance.tsv -o results/`
**Explanation:** Results file contamination_events.tsv contains: contamination source, contaminated sample (target), estimated contamination rate (%), and probability score.
