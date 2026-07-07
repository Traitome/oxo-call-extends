---
name: pepnovo
category: expression
description: PepNovo performs de novo peptide sequencing from MS data.
tags: [pepnovo, expression, de-novo, proteomics]
author: oxo-call-community
source_url: "http://proteomics.ucsd.edu/Software/PepNovo/"
---

## Concepts

- **Tool Overview**: PepNovo sequences peptides de novo.
- **Core Function**: Performs peptide sequencing from MS.
- **Algorithm**: Uses de novo sequencing algorithms.
- **Input Format**: Accepts tandem MS data files.
- **Output**: Produces peptide sequences.
- **Use Case**: Proteomics, peptide identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large MS datasets require memory.
- **MS Quality**: Results depend on MS data quality.
- **Sequence Accuracy**: De novo may have errors.
- **Runtime**: Sequencing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pepnovo --help`
**Explanation:** Shows available options and usage instructions.

### Sequence peptides
**Args:** `pepnovo -i ms_data.mgf -o peptides.txt`
**Explanation:** Performs de novo peptide sequencing.

### With parameters
**Args:** `pepnovo -i ms_data.mgf -p params.txt -o peptides.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pepnovo -v -i ms_data.mgf -o peptides.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pepnovo -t 4 -i ms_data.mgf -o peptides.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pepnovo -i ms_data.mgf -o peptides.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pepnovo -i ms_data.mgf -o peptides.txt --report report.html`
**Explanation:** Generates HTML report.