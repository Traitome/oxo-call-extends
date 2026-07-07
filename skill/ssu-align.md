---
name: ssu-align
category: alignment
description: "SSU-ALIGN: structural alignment of SSU rRNA sequences."
tags: [ssu-align, rRNA, alignment, structural]
author: oxo-call-community
source_url: "http://eddylab.org/software/ssu-align/"
---
## Concepts

- **Tool Overview**: ssu-align (v0.1.1) is a tool for structural alignment of small subunit (SSU) rRNA sequences using covariance models.
- **Core Function**: Aligns rRNA sequences based on both sequence similarity and secondary structure conservation.
- **Algorithm**: Uses profile covariance models (CMs) from Infernal to align sequences to a consensus structure.
- **Input/Output**: Input: FASTA format rRNA sequences; Output: Structurally aligned sequences in Stockholm format.
- **Structure Conservation**: Considers base pairing constraints and secondary structure elements during alignment.
- **Installation**: `conda install -c bioconda ssu-align` or download from Eddy Lab website.

## Pitfalls

- **Sequence Quality**: Poor quality sequences affect alignment accuracy and structure prediction.
- **Sequence Length**: Optimal for full-length SSU rRNA sequences; partial sequences may need adjustment.
- **Reference Database**: Using outdated reference alignments affects alignment quality.
- **Memory Requirements**: Aligning many sequences simultaneously may require significant memory.
- **Output Format**: Stockholm format may need conversion for downstream tools.
- **Model Selection**: Incorrect covariance model selection leads to poor alignments.

## Examples

### Display help
**Args:** `ssu-align --help`
**Explanation:** Shows available options and usage information.

### Basic structural alignment
**Args:** `ssu-align -i sequences.fasta -o alignment.sto`
**Explanation:** Align sequences using default SSU rRNA model.

### With specific model
**Args:** `ssu-align -i sequences.fasta -o alignment.sto -m bacterial.ssu`
**Explanation:** Use specific covariance model for bacterial SSU rRNA.

### Align to reference
**Args:** `ssu-align -i query.fasta -r reference.sto -o alignment.sto`
**Explanation:** Align query sequences to existing reference alignment.

### Build profile
**Args:** `ssu-align --build -i sequences.fasta -o profile.cm`
**Explanation:** Build covariance model profile from aligned sequences.

### With secondary structure
**Args:** `ssu-align -i sequences.fasta -o alignment.sto --structure`
**Explanation:** Output alignment with secondary structure annotation.

### Quality filtering
**Args:** `ssu-align -i sequences.fasta -o alignment.sto -q 20`
**Explanation:** Apply quality filter to input sequences.

### Verbose output
**Args:** `ssu-align -i sequences.fasta -o alignment.sto -v`
**Explanation:** Run with verbose output for debugging.
