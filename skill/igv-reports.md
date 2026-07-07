---
name: igv-reports
category: variant-calling
description: Creates self-contained html pages for visual variant review with IGV (igv.js).
tags: [igv-reports, variant review, HTML report, IGV.js]
author: oxo-call-community
source_url: "https://github.com/igvteam/igv-reports"
---

## Concepts

- **Tool Overview**: igv-reports generates standalone HTML reports for visual variant review using IGV.js
- **Core Function**: Creates self-contained HTML pages with embedded IGV.js viewer for variant inspection
- **Input/Output**: Accepts VCF, BAM, and other genomic files; outputs HTML report files
- **Installation**: `conda install -c bioconda igv-reports`
- **Key Features**: Standalone HTML reports, embedded IGV.js viewer, variant-centric views

## Pitfalls

- **File Size**: Reports can be large due to embedded resources
- **Browser Compatibility**: Requires modern web browser for full functionality
- **Resource Paths**: Relative paths must be correctly specified for embedded files
- **VCF Requirements**: VCF files must be indexed for efficient variant access
- **Memory Considerations**: Large BAM files may impact report generation time

## Examples

### Generate variant report from VCF
**Args:** `igv-reports create report.html variants.vcf.gz --genome hg38`
**Explanation:** Creates an HTML report for reviewing variants in the VCF file.

### Include alignment track
**Args:** `igv-reports create report.html variants.vcf.gz --bam sample.bam --genome hg38`
**Explanation:** Adds BAM alignment visualization to the variant report.

### Specify gene list
**Args:** `igv-reports create report.html variants.vcf.gz --genes genes.txt --genome hg38`
**Explanation:** Limits report to variants in specified genes.

### Add custom tracks
**Args:** `igv-reports create report.html variants.vcf.gz --tracks annotations.gff --genome hg38`
**Explanation:** Includes additional annotation tracks in the report.

### Set output directory
**Args:** `igv-reports create output/report.html variants.vcf.gz --genome hg38`
**Explanation:** Creates report in a specified output directory.
