---
name: gatk-framework
category: programming
description: The MIT-licensed core framework of GATK for developers building custom genomics tools.
tags: [gatk-framework, programming, library, genomics, development]
author: oxo-call-community
source_url: "https://github.com/chapmanb/gatk"
---

## Concepts

- **Tool Overview**: GATK-framework is the core MIT-licensed framework for building custom genomics tools, originally derived from Broad Institute's GATK.
- **Core Function**: Provides programmatic APIs for variant calling, read processing, and genomics data manipulation for custom tool development.
- **MIT License**: Unlike Broad's GATK which uses a specific license, gatk-framework uses MIT license enabling free commercial use.
- **Language**: Built with Java, enabling integration with other Java-based genomics pipelines and libraries.
- **Community Development**: Maintained by the open-source community with contributions for custom genomics analysis needs.
- **Compatibility**: Designed as a drop-in framework compatible with standard GATK concepts and data formats.
- **Use Cases**: Building custom variant callers, developing novel genomics algorithms, creating specialized analysis pipelines.
- **Data Formats**: Supports BAM/SAM, VCF, GFF, FASTA, and other standard genomics file formats.
- **Installation**: `pip install gatk-framework` or build from source at GitHub

## Pitfalls

- **Documentation Gaps**: Community-maintained framework may have less comprehensive documentation than Broad's official GATK.
- **Version Sync**: May lag behind official GATK releases in features and bug fixes.
- **Java Dependency**: Requires Java Runtime Environment (JRE) for execution. Check version compatibility.
- **API Stability**: As a community project, API changes may occur between versions without deprecation warnings.
- **Limited Tool Wrappers**: Unlike official GATK, fewer command-line wrappers are provided. Requires programming knowledge.
- **Testing Resources**: Fewer automated tests may mean less validation of edge cases.
- **Support Channels**: Relies on GitHub issues rather than dedicated support forums.

## Examples

### Install via pip
**Args:** `pip install gatk-framework`
**Explanation:** Installs the Python package with Java dependencies.

### Import in Python
**Args:** `from gatk import VariantCaller, ReadProcessor`
**Explanation:** Imports core classes for building custom genomics workflows.

### Basic variant calling workflow
**Args:** `java -jar gatk-framework.jar -T HaplotypeCaller -R reference.fa -I reads.bam -o variants.vcf`
**Explanation:** Example of invoking a tool through the framework JAR.

### List available tools
**Args:** `java -jar gatk-framework.jar --list`
**Explanation:** Displays all tools available in this framework build.

### Process BAM file
**Args:** `java -jar gatk-framework.jar -T BaseRecalibrator -R reference.fa -I reads.bam -knownSites dbsnp.vcf.gz -o recal.table`
**Explanation:** Example of read processing with known variants.

### Build from source
**Args:** `git clone https://github.com/chapmanb/gatk.git && cd gatk && ./gradlew jar`
**Explanation:** Compiles the framework from source code.
