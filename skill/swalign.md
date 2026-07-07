---
name: swalign
category: alignment
description: Smith-Waterman local sequence aligner for pairwise sequence comparison.
tags: [swalign, sequence-alignment, smith-waterman, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/mbreese/swalign/"
---

## Concepts

- **Tool Overview**: swalign (v0.3.7) is a Python implementation of Smith-Waterman aligner.
- **Core Function**: Performs local sequence alignment using dynamic programming.
- **Algorithm**: Implements Smith-Waterman algorithm for sensitive local alignment.
- **Input/Output**: Input: FASTA sequences; Output: Alignment results.
- **Applications**: Sequence comparison, motif finding, homology detection.
- **Installation**: `conda install -c bioconda swalign` or pip install.

## Pitfalls

- **Performance**: Slow for very long sequences.
- **Memory Requirements**: Large sequences require significant memory.
- **Parameter Tuning**: Incorrect scoring parameters affect alignment.
- **Sequence Quality**: Poor quality sequences affect alignment.
- **Python Environment**: Requires proper Python environment.
- **Scalability**: Not suitable for very large-scale alignments.

## Examples

### Display help
**Args:** `python -c "import swalign; help(swalign)"`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `python -c "from swalign import Aligner; a = Aligner(); print(a.align('ACGT', 'ACCT'))"`
**Explanation:** Align two sequences.

### Custom scoring
**Args:** `python -c "from swalign import Aligner; a = Aligner(match=2, mismatch=-1, gap=-2); print(a.align(s1, s2))"`
**Explanation:** Use custom scoring parameters.

### Verbose mode
**Args:** `python -c "from swalign import Aligner; a = Aligner(); result = a.align(s1, s2); print(result)"`
**Explanation:** Get detailed alignment result.

### Output statistics
**Args:** `python -c "from swalign import Aligner; a = Aligner(); result = a.align(s1, s2); print(result.score)"`
**Explanation:** Get alignment score.

### Batch processing
**Args:** `python -c "from swalign import Aligner; a = Aligner(); [a.align(s, ref) for s in sequences]"`
**Explanation:** Align multiple sequences.

### Local alignment
**Args:** `python -c "from swalign import LocalAligner; a = LocalAligner(); print(a.align(s1, s2))"`
**Explanation:** Perform local alignment.

### Global alignment
**Args:** `python -c "from swalign import GlobalAligner; a = GlobalAligner(); print(a.align(s1, s2))"`
**Explanation:** Perform global alignment.

### Generate report
**Args:** `python -c "from swalign import Aligner; a = Aligner(); result = a.align(s1, s2); result.save('alignment.txt')"`
**Explanation:** Save alignment to file.
