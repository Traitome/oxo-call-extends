---
name: lepwrap
category: workflow
description: Snakemake pipeline for linkage map construction and genome assembly anchoring
tags: [lepwrap, workflow, linkage-map, genome-assembly, snakemake, Lep-Map3]
author: oxo-call-community
source_url: "https://github.com/pdimens/LepWrap"
---

## Concepts

- **Linkage Mapping**: Constructs genetic linkage maps
- **Genome Anchoring**: Anchors and orients genome assemblies
- **Snakemake Pipeline**: Built on Snakemake workflow management
- **Lep-Map3 Integration**: Uses Lep-Map3 for linkage mapping
- **LepAnchor**: Anchors scaffolds to linkage groups
- **Automated Workflow**: Streamlines complex analysis pipeline

## Pitfalls

- **Input Data Quality**: Poor quality sequencing data affects mapping
- **Computational Resources**: Large datasets require significant resources
- **Parameter Tuning**: Requires careful parameter optimization
- **Reference Genome**: Needs good quality reference genome
- **Memory Usage**: Memory-intensive operations
- **Software Dependencies**: Requires multiple dependencies

## Examples

### Run pipeline
**Args:** `snakemake --snakefile LepWrap.smk`
**Explanation:** Runs the complete LepWrap pipeline.

### Specify config
**Args:** `snakemake --snakefile LepWrap.smk --configfile config.yaml`
**Explanation:** Uses custom configuration file.

### Linkage map only
**Args:** `snakemake --snakefile LepWrap.smk linkage_map`
**Explanation:** Runs only linkage map construction.

### Genome anchoring only
**Args:** `snakemake --snakefile LepWrap.smk anchor`
**Explanation:** Runs only genome anchoring step.

### Parallel execution
**Args:** `snakemake --snakefile LepWrap.smk --jobs 8`
**Explanation:** Runs pipeline with 8 parallel jobs.

### Dry run
**Args:** `snakemake --snakefile LepWrap.smk --dryrun`
**Explanation:** Shows what would be executed without running.