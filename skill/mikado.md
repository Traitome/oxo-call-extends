---
name: mikado
category: alignment
description: A Python3 annotation program to select the best gene model in each locus.
tags: [mikado, alignment, alignment]
author: oxo-call-community
source_url: "https://github.com/EI-CoreBioinformatics/mikado"
---

## Concepts

- **Tool Overview**: mikado v2.3.4 - Mikado is a lightweight Python3 pipeline whose purpose is to facilitate the identification of expressed loci from RNA-Seq data * and to select the best models in each locus.  The logic of the pipeline is as follows:  1. In a first step, the annotation (provided in GTF/GFF3 format) is parsed to locate *superloci* of overlapping features on the **same strand**. 2. The superloci are divided into different *subloci*, each of which is defined as follows:      * For multiexonic transcripts, to belong to the same sublocus they must share at least a splicing junction (i.e. an intron)     * For monoexonic transcripts, they must overlap for at least one base pair     * All subloci must contain either only multiexonic or only monoexonic transcripts 3. In each sublocus, the pipeline selects the best transcript according to a user-defined prioritization scheme. 4. The resulting *monosubloci* are merged together, if applicable, into *monosubloci_holders* 5. The best non-overlapping transcripts are selected, in order to define the *loci* contained inside the superlocus.      * At this stage, monoexonic and multiexonic transcript are checked for overlaps     * Moreover, two multiexonic transcripts are considered to belong to the same locus if they share a splice *site* (not junction)      6. Once the loci have been defined, the program backtracks and looks for transcripts which can be assigned unambiguously to a single locus and constitute valid alternative splicing isoforms of the main transcripts.   The criteria used to select the "*best*" transcript are left to the user's discretion, using specific configuration files..
- **Core Function**: A Python3 annotation program to select the best gene model in each locus.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mikado`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
