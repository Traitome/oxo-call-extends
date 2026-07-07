---
name: hhsuite
category: bioinformatics
description: HH-suite3 performs fast remote homology detection and deep protein annotation using profile hidden Markov models.
tags: [hhsuite, protein-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/soedinglab/hh-suite/wiki"
---

## Concepts

- **Remote Homology Detection**: HH-suite detects distant protein relationships.

- **Profile HMMs**: Uses profile hidden Markov models.

- **Protein Annotation**: Provides deep protein annotation.

- **Sequence Comparison**: Compares protein sequences efficiently.

- **Database Search**: Searches protein databases.

- **Structure Prediction**: Aids in protein structure prediction.

## Pitfalls

- **Database Download**: Requires large database downloads.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Database Updates**: Databases need regular updates.

## Examples

### Search database
**Args:** `hhblits -i query.fasta -d uniprot20_2023_02 -o results.hhr`
**Explanation:** Searches protein database with HHblits.

### Build profile
**Args:** `hhbuild -i query.fasta -o query.hhm`
**Explanation:** Builds profile HMM from sequence.

### Align profiles
**Args:** `hhalign -i1 query.hhm -i2 target.hhm -o alignment.hhr`
**Explanation:** Aligns two profile HMMs.

### Batch processing
**Args:** `for f in *.fasta; do hhblits -i $f -d uniprot20_2023_02 -o ${f%.fasta}.hhr; done`
**Explanation:** Processes multiple query sequences.

### Generate report
**Args:** `hhblits -i query.fasta -d uniprot20_2023_02 -o results.hhr -report`
**Explanation:** Generates comprehensive report.

### Help command
**Args:** `hhblits -h`
**Explanation:** Shows available options and usage information.