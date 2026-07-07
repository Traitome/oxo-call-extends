---
name: taranis
category: typing
description: Pipeline for whole-genome and core-genome MLST (wg/cgMLST) allele calling.
tags: [taranis, mlst, allele-calling, typing]
author: oxo-call-community
source_url: "https://github.com/BU-ISCIII/taranis"
---

## Concepts

- **Tool Overview**: taranis (v2.0.1) performs wg/cgMLST allele calling.
- **Core Function**: Multi-locus sequence typing for bacterial isolates.
- **Algorithm**: Uses BLAST-based allele matching.
- **Input/Output**: Input: FASTQ reads; Output: MLST profiles.
- **Applications**: Bacterial typing, outbreak investigation, epidemiology.
- **Installation**: `conda install -c bioconda taranis` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Schema Quality**: Depends on MLST schema quality.
- **Read Quality**: Poor quality reads affect typing.
- **Computational Time**: Processing large datasets can be slow.
- **False Positives**: May assign incorrect alleles.
- **Schema Updates**: Requires regular schema updates.

## Examples

### Display help
**Args:** `taranis --help`
**Explanation:** Shows available options and usage information.

### Basic MLST calling
**Args:** `taranis -i reads.fastq -s schema/ -o mlst_profile.txt`
**Explanation:** Call MLST alleles from reads.

### With assembly
**Args:** `taranis -i assembly.fasta -s schema/ -o mlst_profile.txt -a`
**Explanation:** Use assembled genome for typing.

### Verbose mode
**Args:** `taranis -i reads.fastq -s schema/ -o mlst_profile.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `taranis -i reads.fastq -s schema/ -o mlst_profile.txt --stats`
**Explanation:** Generate statistics about typing.

### Batch processing
**Args:** `for f in fastq/*.fastq; do taranis -i $f -s schema/ -o profiles/${f%.fastq}_mlst.txt; done`
**Explanation:** Process multiple FASTQ files.

### Include all loci
**Args:** `taranis -i reads.fastq -s schema/ -o mlst_profile.txt --all-loci`
**Explanation:** Report all locus calls.

### Quality filtering
**Args:** `taranis -i reads.fastq -s schema/ -o mlst_profile.txt -q 20`
**Explanation:** Minimum quality threshold.

### Generate report
**Args:** `taranis -i reads.fastq -s schema/ -o mlst_profile.txt --report`
**Explanation:** Generate comprehensive MLST report.
