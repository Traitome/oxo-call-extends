---
name: gencore
category: quality-control
description: GenCore - Generate consensus reads to reduce sequencing noises and remove duplications.
tags: [gencore, consensus, sequencing-quality, deduplication]
author: oxo-call-community
source_url: "https://github.com/OpenGene/gencore/blob/v0.17.2/README.md"
---

## Concepts
- **Consensus Generation**: Generates consensus reads from overlapping sequences.
- **Noise Reduction**: Reduces sequencing noise through consensus calling.
- **Duplicate Removal**: Removes duplicate reads from sequencing data.
- **Error Correction**: Corrects sequencing errors using consensus approach.
- **Quality Improvement**: Improves overall sequence quality.

## Pitfalls
- **Over-correction**: May over-correct true biological variations.
- **Parameter Sensitivity**: Results depend on consensus threshold settings.
- **Memory Usage**: Large datasets require significant memory.
- **Computational Time**: Processing time increases with dataset size.
- **Input Quality**: Poor input quality affects consensus accuracy.

## Examples
### Generate consensus reads
**Args:** `gencore -i input.fastq -o consensus.fastq`
**Explanation:** Generates consensus reads from input FASTQ file.

### With quality filtering
**Args:** `gencore -i input.fastq -o consensus.fastq -q 20`
**Explanation:** Filters reads with quality score below 20 before consensus generation.

### Remove duplicates
**Args:** `gencore -i input.fastq -o consensus.fastq -d`
**Explanation:** Enables duplicate removal during consensus generation.

### Paired-end data
**Args:** `gencore -i input_1.fastq -i2 input_2.fastq -o consensus_1.fastq -o2 consensus_2.fastq`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `gencore -i ./fastq_files/ -o ./consensus_output/`
**Explanation:** Processes multiple FASTQ files in batch.