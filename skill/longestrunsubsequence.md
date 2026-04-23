---
name: longestrunsubsequence
category: alignment
description: Implementation of a solver for the Longest Run Subsequence Problem. Given a sequence as input, compute a longest subsequence such that there is at most one run for every character.
tags: [longestrunsubsequence, alignment, alignment]
author: oxo-call-community
source_url: "https://github.com/AlBi-HHU/longest-run-subsequence"
---

## Concepts

- **Tool Overview**: longestrunsubsequence v1.0.1 - This is an implementation of the longest run subsequence problem, introduced in (Schrinner et al., WABI 2020) https://drops.dagstuhl.de/opus/volltexte/2020/12795/. It describes a string problem, which looks for the longest subsequence of a string such that this sequence contains at most one consecutive run for each character in the underlying alphabet. The code contains two different algorithms (based on Integer Linear Programming and on Dynamic Programming) as described in the publication. The problem appears in the context of homology-based scaffolding of two contig sets, originating from two individuals of the same species..
- **Core Function**: Implementation of a solver for the Longest Run Subsequence Problem. Given a sequence as input, compute a longest subsequence such that there is at most one run for every character.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda longestrunsubsequence`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
