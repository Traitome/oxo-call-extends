---
name: amos
category: assembly
description: A Modular, Open-Source whole genome assembler infrastructure
tags: [amos, assembly, genome-assembly, Minimus, AMOScmp, Bambus]
author: oxo-call-community
source_url: "http://amos.sourceforge.net/wiki/index.php/AMOS"
---

## Concepts

- **Tool Overview**: AMOS (A Modular Open Source Assembler) is a software infrastructure for genome assembly, providing a collection of modular tools and pipelines rather than a single assembler.
- **Core Function**: Provides assembly pipelines (Minimus, AMOScmp), scaffolding (Bambus 2.0), validation tools, and data conversion utilities for genome assembly projects.
- **Input/Output**: Inputs: Sequence reads (FASTA/FASTQ), assembly files; Outputs: Assembled contigs, scaffolds, AMOS bank format files.
- **Installation**: Available via Bioconda (`conda install -c bioconda amos`) or from source.
- **Modules**: Includes tools for data conversion (toAmos, bank-transact), assembly (Minimus, AMOScmp), scaffolding (Bambus), validation (amosvalidate), and visualization (Hawkeye).

## Pitfalls

- **Bank Compatibility**: AMOS banks are version-specific; old banks require rebuilding for new versions.
- **Memory Requirements**: Assembly of large genomes requires significant memory resources.
- **Input Format**: Requires conversion to AMOS format (AFG) using toAmos before assembly.
- **Tool Specificity**: Different tools have different requirements; consult individual tool documentation.
- **Performance**: May not perform as well as modern assemblers for large or complex genomes.

## Examples

### Convert reads to AMOS format
**Args:** `toAmos -f reads.frg -o assembly.afg`
**Explanation:** Converts sequence reads to AMOS message file format for assembly.

### Run Minimus assembler
**Args:** `minimus -d assembly.afg -o output`
**Explanation:** Runs the Minimus assembler on the input AMOS file.

### Create AMOS bank
**Args:** `bank-transact -m assembly.afg -b assembly.bnk -c`
**Explanation:** Creates an AMOS bank database from the message file.

### Run comparative assembly (AMOScmp)
**Args:** `runAmos -C AMOScmp.config`
**Explanation:** Executes the AMOScmp comparative assembly pipeline using a configuration file.

### Convert bank to contigs
**Args:** `bank2contig assembly.bnk > contigs.fasta`
**Explanation:** Extracts contig sequences from an AMOS bank and outputs FASTA format.

### Run scaffolder
**Args:** `Bambus2 -b assembly.bnk -o scaffolds.fasta`
**Explanation:** Runs Bambus 2.0 scaffolder to generate scaffolds from assembled contigs.

### Validate assembly
**Args:** `amosvalidate assembly.bnk`
**Explanation:** Validates assembly quality and identifies potential issues.