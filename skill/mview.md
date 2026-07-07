---
name: mview
category: formatting
description: MView extracts and reformats the results of a sequence database search or multiple alignment
tags: [mview, formatting, alignment, blast, html, visualization, fasta, clustal]
author: oxo-call-community
source_url: "https://desmid.github.io/mview"
---

## Concepts

- **Tool Overview**: MView v1.68 is a data formatting and visualization tool that converts sequence search results and multiple alignments into various output formats. It transforms BLAST, FASTA, CLUSTAL, and other alignment formats into readable HTML, or converts between sequence alignment formats.
- **Core Function**: Takes alignment or search result files and reformatts them into HTML (with coloring and highlighting), or converts to formats like FASTA, CLUSTAL, MSF, PIR, RDB for downstream analysis.
- **Input Format**: Supports BLAST XML/Text, FASTA search output, CLUSTAL, HSSP, MSF, FASTA, PIR, and MAF alignment formats. Auto-detects format in most cases.
- **Output Formats**: HTML (colored and styled for web), FASTA, CLUSTAL, MSF, PIR, RDB (tab-delimited), and others. Multiple output options enable flexible downstream use.
- **HTML Features**: When outputting HTML, MView colors residues by property (hydrophobicity, charge, etc.), highlights conserved regions, and produces web-ready visualizations.
- **Use Case**: Converting bioinformatics analysis results for publication, creating web-based alignment viewers, and converting between alignment formats for different tools.

## Pitfalls

- **Format Detection**: MView usually auto-detects input format but may fail on unusual files. Use `-in` flag to explicitly specify format if needed.
- **Large Alignments**: Very large alignments (thousands of sequences) may produce large HTML files. Consider using `-top` to limit sequences shown.
- **HTML Compatibility**: Generated HTML uses CSS and may not render correctly in all browsers or email clients. Test before sharing.
- **Color Schemes**: Default coloring may not be ideal for all purposes. MView offers multiple color schemes - choose based on your data type (proteins vs nucleotides).
- **Reference Sequence**: When highlighting conservation, ensure the first sequence in the alignment is appropriate as the reference.
- **Version Differences**: MView has undergone significant rewrites. Command-line options may differ between versions.

## Examples

### Convert BLAST results to HTML
**Args:** `-in blast_results.xml -html on -out output.html`
**Explanation:** Converts BLAST XML output to a styled HTML page. Residues are colored by property and matches are highlighted.

### Convert to FASTA format
**Args:** `-in alignment.clustal -out reformatted.fasta -out_format fasta`
**Explanation:** Converts CLUSTAL alignment to FASTA format. Useful for tools that require FASTA input.

### Color by conservation level
**Args:** `-in proteins.aln -html on -color conservation -out conserved.html`
**Explanation:** HTML output with residues colored by conservation level. Highly conserved positions get distinct colors.

### Limit displayed sequences
**Args:** `-in large_alignment.sth -top 50 -html on -out top50.html`
**Explanation:** Shows only the top 50 sequences in the HTML output. Useful for large alignments where full display is impractical.

### Generate RDB (tab-delimited) format
**Args:** `-in alignment.maf -out_format rdb -out table.rdb`
**Explanation:** Outputs alignment in tab-delimited format suitable for spreadsheet analysis or database import.
