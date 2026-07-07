---
name: pacbio_falcon
category: alignment
description: FALCON aligns long reads for consensus and assembly from PacBio data.
tags: [pacbio_falcon, alignment, long-reads, assembly]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/FALCON"
---

## Concepts

- **Tool Overview**: FALCON processes PacBio long reads for assembly.
- **Core Function**: Aligns long reads and generates consensus sequences.
- **Algorithm**: Uses hierarchical assembly approach.
- **Input Format**: Accepts FASTQ reads from PacBio sequencing.
- **Output**: Produces assembled contigs and consensus sequences.
- **Use Case**: De novo assembly, genome finishing, and long-read analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Assembly can be computationally intensive.
- **Read Quality**: Results depend on input read quality.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `falcon --help`
**Explanation:** Shows available options and usage instructions.

### Run assembly
**Args:** `fc_run fc_run.cfg`
**Explanation:** Executes FALCON assembly workflow.

### Configure assembly
**Args:** `fc_align -c config.json reads.fastq`
**Explanation:** Aligns reads with configuration.

### Generate consensus
**Args:** `fc_consensus -i aligned.bam -o consensus.fasta`
**Explanation:** Generates consensus sequence.

### Verbose mode
**Args:** `fc_run -v fc_run.cfg`
**Explanation:** Runs with verbose output.

### Resume workflow
**Args:** `fc_run --resume fc_run.cfg`
**Explanation:** Resumes from last checkpoint.

### Number of threads
**Args:** `fc_run -t 16 fc_run.cfg`
**Explanation:** Uses 16 threads for parallel processing.