---
name: soapdenovo2
category: assembly
description: SOAPdenovo2 - De novo genome assembler for short reads
tags: [soapdenovo2, assembly, genome, de-novo, short-reads]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapdenovo.html"
---

## Concepts

- **Tool Overview**: soapdenovo2 (v2.40) - A short-read de novo genome assembler
- **Core Function**: Builds draft assemblies from short-read sequencing data
- **Input/Output**: Accepts FASTQ reads; outputs assembled contigs/scaffolds
- **Algorithm**: Uses de Bruijn graph approach for assembly
- **Installation**: `conda install -c bioconda soapdenovo2`
- **Key Features**: De novo assembly, short-read support, human genome scale

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTQ files
- **K-mer Size**: K-mer size critically affects assembly quality
- **Memory Usage**: Large genomes require significant memory
- **Coverage**: Requires sufficient read coverage for good assembly
- **Repeat Regions**: Repeats may cause assembly fragmentation
- **Configuration**: Requires proper configuration file

## Examples

### Display help
**Args:** `SOAPdenovo2 --help`
**Explanation:** Shows available options and usage information.

### Basic assembly
**Args:** `SOAPdenovo2 all -s config.txt -K 31 -o assembly`
**Explanation:** Run complete assembly pipeline.

### Pregraph only
**Args:** `SOAPdenovo2 pregraph -s config.txt -K 31 -o assembly`
**Explanation:** Build de Bruijn graph only.

### Contig assembly
**Args:** `SOAPdenovo2 contig -g assembly`
**Explanation:** Assemble contigs from graph.

### Scaffold assembly
**Args:** `SOAPdenovo2 scaff -g assembly`
**Explanation:** Build scaffolds from contigs.

### With threads
**Args:** `SOAPdenovo2 all -s config.txt -K 31 -o assembly -p 16`
**Explanation:** Use multiple threads for assembly.

### Set k-mer
**Args:** `SOAPdenovo2 all -s config.txt -K 63 -o assembly`
**Explanation:** Set k-mer size for assembly.

### Map reads
**Args:** `SOAPdenovo2 map -s config.txt -g assembly`
**Explanation:** Map reads back to assembly.