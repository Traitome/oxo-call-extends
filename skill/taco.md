---
name: taco
category: rna-analysis
description: Multi-sample transcriptome assembly from RNA-Seq data.
tags: [taco, transcriptome-assembly, rna-seq, multi-sample]
author: oxo-call-community
source_url: "https://github.com/tacorna/taco"
---

## Concepts

- **Tool Overview**: taco (v0.7.3) performs multi-sample transcriptome assembly.
- **Core Function**: Assembles transcripts from multiple RNA-Seq samples.
- **Algorithm**: Combines individual assemblies and resolves conflicts.
- **Input/Output**: Input: RNA-Seq alignments; Output: Combined transcriptome.
- **Applications**: RNA-Seq analysis, transcriptome reconstruction.
- **Installation**: `conda install -c bioconda taco` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing multiple samples can be slow.
- **Parameter Tuning**: Incorrect parameters affect assembly quality.
- **Alignment Quality**: Requires well-aligned BAM files.
- **Sample Heterogeneity**: Diverse samples may be challenging.
- **Annotation Quality**: Reference annotations affect results.

## Examples

### Display help
**Args:** `taco --help`
**Explanation:** Shows available options and usage information.

### Basic transcriptome assembly
**Args:** `taco -i samples.txt -g annotation.gtf -o assembly/`
**Explanation:** Assemble transcriptome from multiple samples.

### With reference
**Args:** `taco -i samples.txt -g annotation.gtf -r reference.fasta -o assembly/`
**Explanation:** Use reference genome for assembly.

### Verbose mode
**Args:** `taco -i samples.txt -g annotation.gtf -o assembly/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `taco -i samples.txt -g annotation.gtf -o assembly/ --stats`
**Explanation:** Generate statistics about assembly.

### Batch processing
**Args:** `for f in bams/*.bam; do taco -i $f -g annotation.gtf -o assemblies/${f%.bam}/; done`
**Explanation:** Process multiple BAM files.

### Filter by expression
**Args:** `taco -i samples.txt -g annotation.gtf -o assembly/ -e 1`
**Explanation:** Filter by minimum expression level.

### Include novel transcripts
**Args:** `taco -i samples.txt -g annotation.gtf -o assembly/ --novel`
**Explanation:** Include novel transcript discovery.

### Generate report
**Args:** `taco -i samples.txt -g annotation.gtf -o assembly/ --report`
**Explanation:** Generate comprehensive assembly report.
