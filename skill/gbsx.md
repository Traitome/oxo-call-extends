---
name: gbsx
category: variant-calling
description: Toolkit for experimental design and demultiplexing genotyping by sequencing experiments
tags: [gbsx, variant-calling, demultiplexing, genotyping, barcode, gbs, rad]
author: oxo-call-community
source_url: "https://github.com/GenomicsCoreLeuven/GBSX"
---

## Concepts

- **Tool Overview**: GBSX (Genotyping By Sequencing demultipleXing) is a Java-based toolkit that provides four functions for GBS/RAD experiments: barcode generator, restriction enzyme predictor, barcode discovery, and demultiplexer. It is designed to support experimental design and the first stages of GBS data analysis before variant calling.
- **Core Function**: The primary function is demultiplexing raw sequencing data containing inline barcodes into sample-specific FASTQ files. GBSX handles both single-read and paired-end sequencing data from GBS (Genotype-by-Sequencing) and RAD (Restriction site Associated DNA) protocols.
- **GBS Protocol Structure**: In standard GBS, the read structure is: inlineBarcode-RestrictionEnzyme-insert-RestrictionEnzyme-CommonAdaptor. The inline barcode (4-6bp) is used for demultiplexing, and the restriction enzyme cut sites flank the genomic insert.
- **RAD Protocol Structure**: In RAD-seq, the structure is: inlineBarcode-RestrictionEnzyme-insert-CommonAdaptor. Only one restriction site is present, as opposed to two in standard GBS.
- **Barcode List Format**: The demultiplexer requires a tab-delimited file without headers containing: column 1 (sample name - letters, numbers, underscores only), column 2 (barcode sequence), column 3 (restriction enzyme name), column 4 (optional second enzyme), column 5 (optional second barcode).
- **Common Adaptor**: All GBSX protocols use `AGATCGGAAGAGCG` as the common adaptor sequence, which must be present in the read but is trimmed during demultiplexing.
- **Mismatch Tolerance**: GBSX allows configurable mismatches in barcode matching to recover reads with sequencing errors. The default is 0 mismatches but can be increased at the cost of potential cross-contamination between samples.
- **Installation**: Java Runtime Environment (JRE) required. Download JAR from GitHub releases or install via Bioconda (`conda install -c bioconda gbsx`). Perl is also required for the GBSX Digest script.

## Pitfalls

- **Incorrect Barcode File Format**: The barcode list file must be tab-delimited without headers. Spaces or wrong column ordering will cause demultiplexing failures. Always verify the format matches: sample_name<tab>barcode<tab>enzyme.
- **Enzyme Name Case Sensitivity**: Enzyme names must match exactly (e.g., "ApeKI", not "apeki" or "Apeki"). Check the NEB website for correct enzyme naming conventions when creating the barcode list.
- **Paired-End File Order**: For paired-end data, Read1 and Read2 files must correspond to the same library. GBSX will error if the files have different numbers of reads or are misaligned.
- **No Restriction Enzyme (RAD mode)**: If demultiplexing RAD data without restriction enzymes, use "NA" as the restriction enzyme name. The RAD protocol does not include restriction site trimming.
- **Java Memory Allocation**: Large GBS datasets may require increased Java heap size. Use `java -Xmx4g -jar GBSX.jar` to allocate 4GB of memory for large files.
- **Gzip File Handling**: When using gzip-compressed input files, ensure the `-gzip true` flag is set. The tool will produce gzip-compressed output automatically when this flag is enabled.

## Examples

### Generate barcodes for a new experiment
**Args:** `java -jar GBSX_v1.3.jar --BarcodeGenerator -b 48 -e ApeKI -o barcode_output/`
**Explanation:** The BarcodeGenerator creates 48 unique random barcodes compatible with the ApeKI restriction enzyme. The output contains barcode_list.txt (for demultiplexing) and barcode_summary.txt (showing base composition to verify randomness). Always manually inspect the base occurrence matrix to ensure balanced nucleotide distribution.

### Demultiplex single-read GBS data
**Args:** `java -jar GBSX_v1.3.jar --Demultiplexer -f1 sample_R1.fastq.gz -i barcode_list.txt -gzip true -o demultiplexed/`
**Explanation:** The standard demultiplexing command for single-read data. Reads are matched to samples by finding the inline barcode, then written to sample-specific gzip-compressed FASTQ files in the output directory. Unmatched reads (no valid barcode) go to an "unknown" file.

### Demultiplex paired-end GBS data
**Args:** `java -jar GBSX_v1.3.jar --Demultiplexer -f1 run_R1.fastq.gz -f2 run_R2.fastq.gz -i barcode_list.txt -gzip true -o paired_output/`
**Explanation:** For paired-end sequencing, both Read1 and Read2 files must be specified. Both files must contain the same barcodes. GBSX writes matching Read1 and Read2 files for each sample, maintaining file pair integrity for downstream paired-end analysis.

### Allow barcode mismatches for lower quality data
**Args:** `java -jar GBSX_v1.3.jar --Demultiplexer -f1 sample_R1.fastq.gz -i barcode_list.txt -mm 1 -gzip true -o tolerant_demux/`
**Explanation:** Setting `-mm 1` allows one mismatch in the barcode sequence. This is useful for older flowcells or lower quality data where sequencing errors in the barcode are common. Be aware this may increase sample cross-contamination.

### Discover unknown barcodes from sequencing data
**Args:** `java -jar GBSX_v1.3.jar --BarcodeDiscovery -f1 raw_data.fastq.gz -gzip true -max 16 -o discovery_output/`
**Explanation:** BarcodeDiscovery analyzes raw sequencing data to find all unique inline barcodes without needing a predefined barcode list. The `-max 16` parameter limits analysis to barcodes up to 16bp in length. Output shows discovered barcodes and their frequency, which can be used to create a barcode list for retrospective demultiplexing.

### Predict restriction fragments for experimental design
**Args:** `perl GBSX_digest_v1.0.pl -d G^CWGC -l 100 -f genome_links.txt`
**Explanation:** The Perl-based digest script predicts which genome fragments would be sequenced given a restriction enzyme (ApeKI with cut site G^CWGC) and read length (100bp). The genome_links.txt file contains paths to chromosome FASTA files. Output includes a BED file of fragment coordinates for overlap with known SNPs or other genomic features.
