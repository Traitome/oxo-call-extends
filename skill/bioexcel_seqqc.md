---
name: bioexcel_seqqc
category: qc
description: Sequence Quality Control pipeline/modules
tags: [quality-control, sequencing, pipeline]
author: oxo-call-community
source_url: "https://github.com/bioexcel/bioexcel_seqqc"
---

## Concepts
- **Tool Overview**: BioExcel_SeqQC provides sequence quality control pipeline modules for automated QC of sequencing data.
- **QC Modules**: Quality assessment, adapter trimming, contamination screening, and reporting.
- **Applications**: Automated sequencing QC, pipeline integration, quality reporting.

## Pitfalls
- **Configuration**: Requires proper pipeline configuration.

## Examples
### Run QC pipeline
**Args:** `bioexcel_seqqc --input reads.fq --output qc_results/`
**Explanation:** Runs automated sequence quality control pipeline.
