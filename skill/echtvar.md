---
name: echtvar
category: variant-calling
description: "Using all the bits for echt rapid variant annotation and filtering."
tags: [echtvar, variant-calling, variant-annotation, rapid-filtering, VCF]
author: oxo-call-community
source_url: "https://github.com/brentp/echtvar"
---

## Concepts

- **Tool Overview**: Echtvar is a fast variant annotation and filtering tool that efficiently stores and retrieves variant annotations using bit-level encoding.
- **Core Function**: Annotates VCF files with various genomic annotations and enables rapid filtering based on annotation criteria.
- **Input/Output**: Input: VCF files, annotation databases. Output: Annotated VCF files, filtered variants.
- **Algorithm**: Uses bit-packing and indexed data structures for efficient annotation storage and retrieval.
- **Key Features**: Ultra-fast annotation, low memory footprint, support for multiple annotation sources, flexible filtering, VCF manipulation.
- **Installation**: `conda install -c bioconda echtvar`

## Pitfalls

- **Database Building**: Requires building annotation databases before use.
- **Memory Mapping**: Uses memory mapping for performance; ensure sufficient memory.
- **Annotation Compatibility**: Some annotations may not be available in all versions.
- **Filter Syntax**: Requires learning the filtering syntax.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Build annotation database
**Args:** `echtvar build -d db/ -f ref.fasta --bed regions.bed --vcf annotations.vcf`
**Explanation:** Builds annotation database from various sources.

### Annotate VCF
**Args:** `echtvar annotate -d db/ -i input.vcf -o annotated.vcf`
**Explanation:** Annotates VCF file using built database.

### Filter variants
**Args:** `echtvar filter -d db/ -i input.vcf -o filtered.vcf -f "AF > 0.01"`
**Explanation:** Filters variants based on annotation criteria (allele frequency > 1%).

### List available annotations
**Args:** `echtvar list -d db/`
**Explanation:** Lists all available annotations in database.

### Merge annotations
**Args:** `echtvar merge -d db/ -a new_annotations.vcf -o updated_db/`
**Explanation:** Merges new annotations into existing database.