---
name: nextclade_js
category: variant-calling
description: Nextclade JS is a JavaScript implementation of Nextclade for SARS-CoV-2 genome analysis.
tags: [nextclade_js, variant-calling, viral-genomics, javascript, nextstrain]
author: oxo-call-community
source_url: "https://github.com/nextstrain/nextclade"
---

## Concepts

- **Tool Overview**: Nextclade JS provides browser-based viral genome analysis.
- **Core Function**: Performs clade assignment, mutation calling, and quality checks in JavaScript.
- **Algorithm**: Implements Nextclade algorithms in JavaScript for web deployment.
- **Input Format**: Accepts FASTA sequences via API or file upload.
- **Output**: Produces analysis results as JSON or visual reports.
- **Use Case**: Web-based viral sequence analysis, real-time surveillance, and public health applications.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Browser Limitations**: Web implementation has memory constraints.
- **Data Privacy**: Browser-based analysis may have privacy considerations.
- **Performance**: JavaScript implementation may be slower than native.
- **Dataset Updates**: Requires regular data updates.
- **Offline Usage**: Requires network access for web version.

## Examples

### Display help
**Args:** `nextclade_js --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `nextclade_js --input-fasta sequences.fasta --input-dataset data/ --output-json results.json`
**Explanation:** Runs clade analysis and outputs JSON.

### Web API usage
**Args:** `curl -X POST -F "sequence=@sequence.fasta" https://api.nextstrain.org/nextclade`
**Explanation:** Uses Nextclade web API for analysis.

### Node.js usage
**Args:** `const nextclade = require('@nextstrain/nextclade'); const result = await nextclade.analyze(sequence);`
**Explanation:** Uses Nextclade in Node.js application.

### Batch processing
**Args:** `nextclade_js --input-fasta batch.fasta --input-dataset data/ --output-json results.json`
**Explanation:** Processes multiple sequences in batch.

### Output CSV
**Args:** `nextclade_js --input-fasta sequences.fasta --input-dataset data/ --output-csv results.csv`
**Explanation:** Outputs results in CSV format.