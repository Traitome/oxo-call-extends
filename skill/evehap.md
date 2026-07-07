---
name: evehap
category: formatting
description: "Universal mtDNA haplogroup classifier for ancient and modern DNA"
tags: [evehap, formatting, mtDNA, haplogroup-classification, ancient-DNA]
author: oxo-call-community
source_url: "https://github.com/trianglegrrl/eveHap"
---

## Concepts

- **Tool Overview**: eveHap is a universal mtDNA (mitochondrial DNA) haplogroup classifier designed for both ancient and modern DNA samples.
- **Core Function**: Classifies mtDNA samples into phylogenetic haplogroups using reference databases and provides detailed classification reports.
- **Input/Output**: Input: mtDNA sequences (FASTA), BAM files, VCF files, or microarray data. Output: Haplogroup assignments, confidence scores, phylogenetic information.
- **Algorithm**: Uses Kulczynski scoring for high-coverage samples and tree traversal for low-coverage ancient DNA samples.
- **Key Features**: Multi-format support, ancient DNA handling, confidence scoring, phylogenetic classification, visualization tools.
- **Installation**: `conda install -c bioconda evehap`

## Pitfalls

- **DNA Quality**: Ancient DNA samples may have low coverage affecting classification.
- **Reference Database**: Classification depends on comprehensive reference database.
- **Input Format**: Requires properly formatted input files.
- **Contamination**: Nuclear DNA contamination may affect results.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic haplogroup classification
**Args:** `evehap -i mtDNA.fasta -o haplogroup_result.txt`
**Explanation:** Classifies mtDNA sequence into haplogroup.

### From BAM file
**Args:** `evehap -i reads.bam -o haplogroup_result.txt --bam`
**Explanation:** Classifies mtDNA from aligned BAM file.

### From VCF file
**Args:** `evehap -i variants.vcf -o haplogroup_result.txt --vcf`
**Explanation:** Classifies mtDNA from VCF variant calls.

### Low-coverage ancient DNA
**Args:** `evehap -i mtDNA.fasta -o haplogroup_result.txt --ancient`
**Explanation:** Uses tree traversal method for ancient DNA samples.

### Detailed output
**Args:** `evehap -i mtDNA.fasta -o haplogroup_result.txt --detailed`
**Explanation:** Outputs detailed classification report with confidence scores.