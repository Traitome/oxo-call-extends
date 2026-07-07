---
name: irida-linker
category: data-management
description: Perl script for generating a structure of links for files stored in the IRIDA platform
tags: [irida-linker, data-management, irida, sequencing-data, bioinformatics-platform]
author: oxo-call-community
source_url: "https://github.com/phac-nml/irida-linker"
---

## Concepts

- **Tool Overview**: irida-linker is a Perl script that creates directory structures with symbolic links to sequencing files managed by the IRIDA platform.
- **Core Function**: Generates organized directory structures mirroring IRIDA project/sample hierarchies with links to actual data files.
- **Input/Output**: Accepts IRIDA project information and generates a directory tree with symlinks to sequence files.
- **Installation**: `conda install -c bioconda irida-linker` or download from GitHub
- **IRIDA Integration**: Works with the IRIDA bioinformatics platform for managing and analyzing sequencing data in public health genomics.
- **Data Organization**: Maintains project/sample/file hierarchy while avoiding data duplication through symbolic links.

## Pitfalls

- **Path Length**: Long file paths may cause issues on some file systems, especially with deeply nested project structures.
- **Permissions**: Requires read access to IRIDA data directories and write access to the output directory.
- **Link Validity**: Symbolic links may break if source files are moved or deleted.
- **Network Storage**: Performance may be affected when working with network-mounted storage.
- **Duplicate Samples**: Care must be taken to avoid creating duplicate links for shared samples.
- **File Formats**: Assumes standard sequencing file naming conventions (FASTQ, BAM, etc.).

## Examples

### Basic link generation
**Args:** `irida-linker --project ProjectName --output /path/to/output --server irida.example.com`
**Explanation:** Creates directory structure with links for all samples in the specified IRIDA project.

### Specific sample selection
**Args:** `irida-linker --project MyProject --samples Sample1,Sample2,Sample3 --output ./links/`
**Explanation:** Generates links only for the specified samples within the project.

### Include all file types
**Args:** `irida-linker --project ProjectX --output ./data/ --include-all`
**Explanation:** Includes all file types (FASTQ, BAM, assemblies, etc.) in the link structure.

### Dry run mode
**Args:** `irida-linker --project TestProject --output ./test/ --dry-run`
**Explanation:** Shows what would be created without actually generating any links.

### Verbose output
**Args:** `irida-linker --project Analysis --output ./results/ --verbose`
**Explanation:** Provides detailed information about the link generation process.

### Custom link structure
**Args:** `irida-linker --project Study --output ./organized/ --structure sample/file`
**Explanation:** Creates a simplified directory structure organized by sample then file type.