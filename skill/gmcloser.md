---
name: gmcloser
category: genome-finishing
description: gmcloser - Fill and close gaps in scaffold assemblies using NGS reads.
tags: [gmcloser, genome-finishing, gap-closing, assembly]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/gmcloser/"
---

## Concepts
- **Gap Closing**: Closes gaps in assemblies.
- **Scaffold Finishing**: Finishes scaffold assemblies.
- **NGS Data**: Uses next-generation sequencing reads.
- **Iterative Process**: Iteratively closes gaps.
- **Quality Improvement**: Improves assembly quality.

## Pitfalls
- **Assembly Quality**: Requires good initial assembly.
- **Read Coverage**: Low coverage affects closing.
- **Repeat Regions**: May fail in repetitive regions.
- **Computational Resources**: Requires resources.
- **Validation**: Results require validation.

## Examples
### Close gaps
**Args:** `gmcloser -i assembly.fasta -r reads.fastq -o closed.fasta`
**Explanation:** Closes gaps in assembly.

### With options
**Args:** `gmcloser -i assembly.fasta -r reads.fastq -t 8 -o closed.fasta`
**Explanation:** Uses 8 threads.

### Generate report
**Args:** `gmcloser -i assembly.fasta -r reads.fastq -o closed.fasta -report`
**Explanation:** Generates closing report.

### Validate results
**Args:** `gmcloser -i closed.fasta -v -o validation.txt`
**Explanation:** Validates closed assembly.

### Batch processing
**Args:** `gmcloser -l assemblies.txt -r reads/ -o ./closed/`
**Explanation:** Processes multiple assemblies.