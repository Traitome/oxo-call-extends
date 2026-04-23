---
name: fiji-max_inscribed_circles
category: alignment
description: ImageJ / Fiji plugin implementing an iterative Largest Inscribed Circle algorithm using a euclidean distance map
tags: [fiji-max_inscribed_circles, alignment]
author: oxo-call-community
source_url: "https://imagej.net/plugins/max-inscribed-circles"
---

## Concepts
- **Tool Overview**: ImageJ / Fiji plugin implementing an iterative Largest Inscribed Circle algorithm which runs over a binary image or selection in order to fit the maximum number of non-touching circles down to a minimum diameter. The approach uses a Euclidean Distance Map in order to find candidate circles from the largest to the smallest. The code is written for Java 8, which is the currently supported Java version for Fiji and ImageJ.
- **Core Function**: ImageJ / Fiji plugin implementing an iterative Largest Inscribed Circle algorithm using a euclidean distance map
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda fiji-max_inscribed_circles`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
