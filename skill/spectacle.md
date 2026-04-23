---
name: spectacle
category: epigenomics
description: This software implements a spectral learning algorithm for hidden Markov models for epigenomic data. Please see our paper for further details: Song, J and Chen, K. C. Spectacle: fast chromatin state annotation using spectral learning. Genome Biology, 16:33, 2015. http://genomebiology.com/2015/16/1/33
tags: [spectacle, epigenomics]
author: oxo-call-community
source_url: "https://github.com/jiminsong/Spectacle"
---

## Concepts

- **Tool Overview**: spectacle (v1.4) - This software implements a spectral learning algorithm for hidden Markov models for epigenomic data. Please see our paper for further details: Song, J and Chen, K. C. Spectacle: fast chromatin state annotation using spectral learning. Genome Biology, 16:33, 2015. http://genomebiology.com/2015/16/1/33
- **Core Function**: This software implements a spectral learning algorithm for hidden Markov models for epigenomic data. Please see our paper for further details: Song, J and Chen, K. C. Spectacle: fast chromatin state annotation using spectral learning. Genome Biology, 16:33, 2015. http://genomebiology.com/2015/16/1/33
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spectacle`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spectacle -i <input.bam> -o <output_dir>`
**Explanation:** Run spectacle with typical input and output options.
