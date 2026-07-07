---
name: squire
category: transposons
description: SQuIRE - Quantitative, locus-specific transposable element expression analysis
tags: [squire, transposons, expression, rna-seq, transposable-elements]
author: oxo-call-community
source_url: "https://github.com/wyang17/SQuIRE"
---

## Concepts

- **Tool Overview**: squire (v0.9.9.92) - A transposable element analysis tool
- **Core Function**: Provides quantitative, locus-specific view of transposable element expression
- **Input/Output**: Accepts RNA-seq data; outputs TE expression analysis
- **Algorithm**: Locus-specific TE expression quantification
- **Installation**: `conda install -c bioconda squire`
- **Key Features**: TE expression, locus-specific, RNA-seq analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted RNA-seq data
- **Read Quality**: Read quality affects expression quantification
- **TE Annotation**: TE annotation affects analysis accuracy
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Expression Accuracy**: Accuracy depends on read quality and annotation

## Examples

### Display help
**Args:** `squire --help`
**Explanation:** Shows available options and usage information.

### Basic TE expression analysis
**Args:** `squire -i rna_seq.bam -o te_expression.txt`
**Explanation:** Analyze transposable element expression.

### With TE annotation
**Args:** `squire -i rna_seq.bam -a te_annotation.gtf -o te_expression.txt`
**Explanation:** Use specific TE annotation.

### With locus-specific analysis
**Args:** `squire -i rna_seq.bam -o te_expression.txt --locus-specific`
**Explanation:** Enable locus-specific expression analysis.

### Multiple samples
**Args:** `squire -i sample1.bam sample2.bam -o te_expression.txt`
**Explanation:** Analyze TE expression in multiple samples.

### Output detailed results
**Args:** `squire -i rna_seq.bam -o te_expression.txt --detailed`
**Explanation:** Output detailed TE expression information.

### Output statistics
**Args:** `squire -i rna_seq.bam -o te_expression.txt --stats`
**Explanation:** Output expression statistics.

### Generate report
**Args:** `squire -i rna_seq.bam -o te_expression.txt --report`
**Explanation:** Generate TE expression report.

### With threads
**Args:** `squire -i rna_seq.bam -o te_expression.txt -p 8`
**Explanation:** Use multiple threads for analysis.