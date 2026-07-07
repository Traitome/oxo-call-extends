---
name: nanoinsight
category: annotation
description: NanoInsight - Repeat annotation for insertions called by NanoVar
tags: [nanoinsight, annotation, insertion, repeat, nanopore, nanovar]
author: oxo-call-community
source_url: "https://github.com/AsmaaSamyMohamedMahmoud/nanoinsight"
---

## Concepts

- **Tool Overview**: NanoInsight v0.0.3 is a tool for annotating repeat elements in structural variant insertions called by NanoVar from Oxford Nanopore sequencing data.
- **Core Function**: Identifies and classifies repeat elements within insertion variants, helping to understand the nature of structural variations.
- **Algorithm**: Compares inserted sequences against repeat databases (RepBase, RepeatMasker) to identify repeat families and subfamilies.
- **Input Format**: Requires VCF output from NanoVar containing insertion calls, along with a reference genome in FASTA format.
- **Output**: Produces annotated VCF or TSV files with repeat element information for each insertion.
- **Use Case**: Characterizing structural variants, understanding repeat-mediated genomic rearrangements, and annotating insertion events.

## Pitfalls

- **NanoVar Dependency**: Requires input in NanoVar VCF format. Other variant callers' outputs may not be compatible.
- **Repeat Database**: Needs access to repeat databases for annotation. May require separate installation of RepeatMasker or similar tools.
- **Insertion Size**: Works best with moderate-sized insertions. Very large insertions may require additional processing.
- **Reference Quality**: Annotation accuracy depends on reference genome quality and completeness.
- **False Positives**: Low-quality variants may produce unreliable repeat annotations. Filter variants before annotation.
- **Database Updates**: Repeat databases are periodically updated. Outdated databases may miss novel repeat families.

## Examples

### Basic annotation
**Args:** `-i nanovar_variants.vcf -r reference.fasta -o annotated.tsv`
**Explanation:** Annotates repeat elements in NanoVar insertion calls.

### Output VCF format
**Args:** `-i variants.vcf -r ref.fa -o annotated.vcf -f vcf`
**Explanation:** Outputs annotated variants in VCF format with repeat information.

### Specify repeat database
**Args:** `-i variants.vcf -r ref.fa -d repeat_database.fasta -o annotated.tsv`
**Explanation:** Uses specified repeat database instead of default.

### Display help
**Args:** `nanoinsight --help`
**Explanation:** Shows all available options for repeat annotation.
