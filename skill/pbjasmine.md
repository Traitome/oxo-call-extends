---
name: pbjasmine
category: utility
description: pbjasmine provides Jasmine assembly polishing utilities.
tags: [pbjasmine, utility, assembly, polishing]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbjasmine polishes assemblies.
- **Core Function**: Improves assembly quality with polishing.
- **Algorithm**: Uses read-based polishing algorithms.
- **Input Format**: Accepts assembly and alignment files.
- **Output**: Produces polished assemblies.
- **Use Case**: Assembly polishing, quality improvement.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Alignment Quality**: Results depend on input alignments.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `jasmine --help`
**Explanation:** Shows available options and usage instructions.

### Polish assembly
**Args:** `jasmine -a assembly.fasta -b alignments.bam -o polished.fasta`
**Explanation:** Polishes assembly with alignments.

### With reference
**Args:** `jasmine -a assembly.fasta -r reference.fasta -o polished.fasta`
**Explanation:** Uses reference for polishing.

### Verbose mode
**Args:** `jasmine -v -a assembly.fasta -b alignments.bam -o polished.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `jasmine -t 8 -a assembly.fasta -b alignments.bam -o polished.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `jasmine -a assembly.fasta -b alignments.bam -o polished.fastq --fastq`
**Explanation:** Outputs in FASTQ format.

### Generate report
**Args:** `jasmine -a assembly.fasta -b alignments.bam -o polished.fasta --report report.html`
**Explanation:** Generates polishing report.