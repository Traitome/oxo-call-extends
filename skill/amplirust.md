---
name: amplirust
category: utility
description: High-performance in-silico PCR tool for primer matching and product extraction
tags: [amplirust, in-silico-pcr, primer-matching, rust, simd, IUPAC]
author: oxo-call-community
source_url: "https://github.com/erdikilic/amplirust"
---

## Concepts

- **Tool Overview**: Amplirust is a high-performance in-silico PCR tool written in Rust that performs primer matching and PCR product extraction from FASTA sequences. Version 0.2.0.
- **Core Function**: Uses SIMD-accelerated approximate matching algorithms for fast and accurate primer matching across large sequence datasets.
- **Input/Output**: Inputs: FASTA sequences, primer sequences (command line or CSV); Outputs: PCR product sequences, amplification details.
- **Installation**: Available via Bioconda (`conda install -c bioconda amplirust`) or from source.
- **Key Features**: IUPAC ambiguity code support, primer pool mode for multiplex screening, circular genome handling, multi-threaded processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format (FASTA for sequences).
- **Primer Specificity**: Primer sequences must be correctly specified for accurate matching.
- **Circular vs Linear**: Use appropriate flags for circular genomes (e.g., plasmids, mitochondrial DNA).
- **Memory Usage**: Large genomes may require significant memory; consider splitting large inputs.

## Examples

### Basic in-silico PCR
**Args:** `amplirust -i genome.fasta -p "FWD:ATGCGT" -p "REV:CGATGA"`
**Explanation:** Performs in-silico PCR using forward and reverse primers on the input FASTA file.

### Use primer CSV file
**Args:** `amplirust -i genome.fasta --primer-file primers.csv`
**Explanation:** Uses primers from CSV file for batch processing multiple primer pairs.

### Handle circular genome
**Args:** `amplirust -i plasmid.fasta -p "FWD:ATGCGT" -p "REV:CGATGA" --circular`
**Explanation:** Treats input sequence as circular (e.g., plasmid, mitochondrial DNA).

### Primer pool mode
**Args:** `amplirust -i genome.fasta --primer-pool primers.fasta`
**Explanation:** Runs all-vs-all multiplex primer screening using primers from FASTA file.

### Specify maximum product size
**Args:** `amplirust -i genome.fasta -p "FWD:ATGCGT" -p "REV:CGATGA" --max-product-size 5000`
**Explanation:** Limits PCR product detection to sequences up to 5000 bp.

### Show help
**Args:** `amplirust --help`
**Explanation:** Displays available options and usage information.

### Output to file
**Args:** `amplirust -i genome.fasta -p "FWD:ATGCGT" -p "REV:CGATGA" -o products.fasta`
**Explanation:** Saves PCR products to output FASTA file.