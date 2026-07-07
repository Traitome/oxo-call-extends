---
name: rascaf
category: alignment
description: RasCAF performs scaffolding with RNA-seq read alignment for improved genome assembly.
tags: [rascaf, alignment, scaffolding, rna-seq]
author: oxo-call-community
source_url: "https://github.com/mourisl/Rascaf/blob/master/README.md"
---

## Concepts

- **Tool Overview**: rascaf scaffolds assemblies.
- **Core Function**: RNA-seq scaffolding.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts RNA-seq data.
- **Output**: Produces scaffolds.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Coverage**: Affects scaffolding.
- **Parameters**: Must be configured.
- **Runtime**: Scaffolding may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rascaf --help`
**Explanation:** Shows available options and usage instructions.

### Scaffold assembly
**Args:** `rascaf scaffold -i contigs.fasta -r rna.bam -o scaffolds.fasta`
**Explanation:** Scaffolds using RNA-seq.

### With parameters
**Args:** `rascaf scaffold -i contigs.fasta -p params.yaml -o scaffolds.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rascaf -v scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rascaf -t 4 scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With alignment
**Args:** `rascaf scaffold -i contigs.fasta -a alignments.bam -o scaffolds.fasta`
**Explanation:** Uses RNA-seq alignments.

### Generate report
**Args:** `rascaf scaffold -i contigs.fasta -o scaffolds.fasta --report report.html`
**Explanation:** Generates HTML report.