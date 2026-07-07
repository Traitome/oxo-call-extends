---
name: pvga
category: assembly
description: PVGA is a virus-focused genome assembler that performs both assembly and polishing.
tags: [pvga, assembly, virus-assembly, genome-polishing]
author: oxo-call-community
source_url: "https://github.com/SoSongzhi/PVGA"
---

## Concepts

- **Tool Overview**: pvga assembles viral genomes.
- **Core Function**: Virus genome assembly.
- **Algorithm**: Uses de novo assembly.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces viral contigs.
- **Use Case**: Viral genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Virus Diversity**: May affect assembly.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pvga --help`
**Explanation:** Shows available options and usage instructions.

### Assemble virus genome
**Args:** `pvga -i reads.fastq -o virus_assembly.fasta`
**Explanation:** Assembles viral genome from sequencing reads.

### With parameters
**Args:** `pvga -i reads.fastq -p params.yaml -o virus_assembly.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pvga -v -i reads.fastq -o virus_assembly.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pvga -t 4 -i reads.fastq -o virus_assembly.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Polishing only
**Args:** `pvga -i reads.fastq -a draft.fasta -o polished.fasta --polish`
**Explanation:** Polishes existing assembly.

### Generate report
**Args:** `pvga -i reads.fastq -o virus_assembly.fasta --report report.html`
**Explanation:** Generates HTML report.