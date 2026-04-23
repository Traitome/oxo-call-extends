---
name: addrg
category: formatting
description: Add read group information to BAM files for GATK compatibility
tags: [bam, read-group, gatk, formatting, samtools]
author: oxo-call-community
source_url: "https://github.com/holtgrewe/addrg"
---

## Concepts

- **Tool Overview**: addrg is a lightweight tool for adding read group (RG) information to BAM files, making them compatible with GATK and other tools requiring RG tags.
- **Core Function**: Adds or replaces read group information in BAM files with specified sample ID, library, platform, and other RG fields.
- **Input/Output**: Input: BAM file without RG or with incomplete RG. Output: BAM file with complete read group information.
- **GATK Requirement**: Many GATK tools require properly formatted RG tags - addrg ensures BAM files meet these requirements.
- **Installation**: Install via bioconda: `conda install -c bioconda addrg`

## Pitfalls

- **Required Fields**: GATK requires specific RG fields (ID, SM, LB, PL) - ensure all are provided.
- **Platform Codes**: Use standard platform codes (ILLUMINA, PACBIO, etc.) for the PL field.
- **Sorting**: Output BAM is typically coordinate-sorted; verify sorting if needed for downstream tools.
- **Indexing**: Output BAM needs indexing with `samtools index` after adding read groups.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and required parameters for addrg.

### Add basic read group
**Args:** `-i input.bam -o output.bam -r ID:sample1 -r SM:sample1 -r LB:lib1 -r PL:ILLUMINA`
**Explanation:** Adds read group with ID, sample name, library, and platform to the BAM file.

### Add with sequencing center
**Args:** `-i input.bam -o output.bam -r ID:sample1 -r SM:sample1 -r LB:lib1 -r PL:ILLUMINA -r CN:BroadInstitute`
**Explanation:** Includes sequencing center (CN) in the read group information.

### Add with platform unit
**Args:** `-i input.bam -o output.bam -r ID:sample1 -r SM:sample1 -r LB:lib1 -r PL:ILLUMINA -r PU:unit1`
**Explanation:** Adds platform unit (PU) field, typically lane or flowcell identifier.

### Add with description
**Args:** `-i input.bam -o output.bam -r ID:sample1 -r SM:sample1 -r LB:lib1 -r PL:ILLUMINA -r DS:"Whole genome sequencing"`
**Explanation:** Includes description field for additional metadata.

### Process PacBio data
**Args:** `-i pacbio.bam -o output.bam -r ID:sample1 -r SM:sample1 -r LB:lib1 -r PL:PACBIO`
**Explanation:** Adds read group for PacBio sequencing data with appropriate platform code.

### Add with run date
**Args:** `-i input.bam -o output.bam -r ID:sample1 -r SM:sample1 -r LB:lib1 -r PL:ILLUMINA -r DT:2024-01-15`
**Explanation:** Includes sequencing run date in ISO 8601 format.
