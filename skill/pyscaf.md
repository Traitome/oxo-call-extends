---
name: pyscaf
category: assembly
description: PyScaf performs genome assembly scaffolding using paired-end/mate-pair reads, long reads, and synteny information.
tags: [pyscaf, assembly, scaffolding, genome]
author: oxo-call-community
source_url: "https://github.com/lpryszcz/pyScaf"
---

## Concepts

- **Tool Overview**: pyscaf scaffolds assemblies.
- **Core Function**: Scaffold building.
- **Algorithm**: Uses read pairs.
- **Input Format**: Accepts FASTA/BAM files.
- **Output**: Produces scaffolds.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Read Coverage**: Affects scaffolding.
- **Repeat Regions**: May cause issues.
- **Runtime**: Scaffolding may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyscaf --help`
**Explanation:** Shows available options and usage instructions.

### Run scaffolding
**Args:** `pyscaf scaffold -i contigs.fasta -b reads.bam -o scaffolds.fasta`
**Explanation:** Builds scaffolds from contigs.

### With parameters
**Args:** `pyscaf scaffold -i contigs.fasta -p params.yaml -o scaffolds.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyscaf -v scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyscaf -t 4 scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Using long reads
**Args:** `pyscaf scaffold -i contigs.fasta -l long_reads.fastq -o scaffolds.fasta`
**Explanation:** Incorporates long reads.

### Generate report
**Args:** `pyscaf scaffold -i contigs.fasta -o scaffolds.fasta --report report.html`
**Explanation:** Generates HTML report.