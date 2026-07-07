---
name: deepsignal-plant
category: epigenomics
description: DeepSignal-Plant - deep learning method for detecting DNA methylation in plant genomes from Nanopore data.
tags: [deepsignal-plant, epigenomics, methylation, nanopore, deep-learning, plant]
author: oxo-call-community
source_url: "https://github.com/PengNi/deepsignal-plant"
---

## Concepts

- **Tool Overview**: deepsignal-plant (v0.1.6+) is a deep learning-based method for detecting DNA methylation from Oxford Nanopore sequencing reads specifically optimized for plant genomes.
- **Core Function**: Detects 5mC methylation in plant genomes from Nanopore signal data using deep learning, accounting for plant-specific methylation patterns.
- **Input/Output**: Input: Nanopore FAST5/FASTQ files, plant reference genome. Output: Methylation calls in BED/VCF format, modification statistics.
- **Algorithm**: Uses deep neural networks trained on plant methylation data to identify 5mC modifications from raw Nanopore signals.
- **Key Features**: Plant-specific optimization, high accuracy, supports multiple plant species, integrates with Nanopore workflows, no bisulfite required.
- **Installation**: `conda install -c bioconda deepsignal-plant`

## Pitfalls

- **Signal Quality**: Requires high-quality Nanopore signal data.
- **Reference Genome**: Must use plant reference genome.
- **Computational Resources**: Requires significant computational resources.
- **Plant Specificity**: Optimized for plants; may not work well for other organisms.
- **Modification Types**: Currently focuses on 5mC; may not detect other modifications.

## Examples

### Detect DNA methylation in plants
**Args:** `deepsignal-plant call_mods --input_path reads/ --ref ref.fa --output results/`
**Explanation:** Detects DNA methylation from plant Nanopore reads.

### From FAST5 files
**Args:** `deepsignal-plant call_mods --input_path fast5/ --ref ref.fa --output results/ --signal`
**Explanation:** Use raw signal data for methylation detection.

### With model fine-tuning
**Args:** `deepsignal-plant train --input_path training_data/ --ref ref.fa --output model/`
**Explanation:** Train custom plant methylation detection model.