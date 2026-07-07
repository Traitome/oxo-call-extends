---
name: rpsbproc
category: utility
description: RpsbProc — the post-RPS-BLAST processing utility from NCBI that converts RPS-BLAST hits into per-query domain architectures, with options for visualization and downstream domain analysis.
tags: ["rpsbproc", "rps-blast", "cdd", "domain-architecture", "ncbi", "protein-domains"]
author: oxo-call-community
source_url: "https://ftp.ncbi.nih.gov/pub/mmdb/cdd/rpsbproc/README"
---

## Concepts

- **Tool Overview**: RpsbProc (v0.5.1, NCBI / CDD team) is the post-processing utility for RPS-BLAST (Reverse Position-Specific BLAST) hits against NCBI's Conserved Domain Database (CDD). It converts raw RPS-BLAST output into a per-query domain architecture summary, with options for visualization in CDD's domain viewer.
- **Core Function**: Takes the tabular output of `rpsblast -m 7` (or the XML output) and produces a per-query domain architecture summary: a list of the domains in the query, their order, and a confidence score. The output is a TSV or ASN.1 binary file suitable for the CDD viewer or for downstream domain analysis.
- **Algorithm**: A parser + annotator: (1) parse the RPS-BLAST tabular output; (2) for each query, identify the highest-scoring domain hit per position; (3) merge overlapping domain hits; (4) report the per-query domain list with start, stop, E-value, and domain name. Optional: filter by E-value threshold, mask low-complexity regions, and add the architecture to CDD's database.
- **Input Format**: The tabular output of `rpsblast -m 7` (or the XML output from `-m 7 -outfmt 5`). The input must be from a RPS-BLAST run against the CDD database (downloaded from NCBI). The tabular format is a 12-column TSV.
- **Output Format**: A TSV with one row per query: `query_id, num_domains, domain_list, architecture_string`. The `architecture_string` is a compact representation of the domain order (e.g., `PKinase-SH2-SH3`). An optional ASN.1 binary file (`.asn`) is produced for the CDD viewer.
- **Use Case**: The standard post-RPS-BLAST step in a protein domain analysis (canonical use case for CDD analysis), generating a per-protein domain architecture summary for a proteome, identifying domain architectures for downstream phylogenetic or functional analysis, and producing input for the CDD web viewer.

## Pitfalls

- **CRITICAL — The CDD database must be downloaded and pre-processed**: RpsbProc does NOT include the CDD database. Download from `ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/` and unpack with `rpsbproc -i cdd.le` (or the equivalent). Pre-process with `makeprofiledb` to create the binary database.
- **CRITICAL — The RPS-BLAST version must match the CDD database version**: CDD is updated regularly; an old RPS-BLAST binary may not understand the latest database format. Verify with `rpsblast -version` and the CDD README.
- **Overlapping domain hits are merged, not concatenated**: A query region with two overlapping domain hits (e.g., a partial PKinase and a full PKinase) is reported as a single hit, with the higher-scoring domain's name. The architecture may differ from a manual interpretation.
- **The architecture_string is positional, not graph-based**: A protein with a repeated domain (e.g., `SH2-SH2-SH2`) is reported as `SH2*3`, not as a graph. Downstream tools (e.g., CDViz) handle the graph representation.
- **E-value filtering is applied PER HIT, not per architecture**: A single low-E-value hit can rescue a query with multiple borderline hits. Use `--max-evalue 1e-5` for a strict per-hit threshold.
- **No automatic taxonomy filtering**: A bacterial protein may have a hit to a eukaryotic-specific domain; RpsbProc does not filter by taxonomy. Filter the output by taxonomy post hoc.

## Examples

### Basic RpsbProc run
**Args:** `rpsblast -query proteins.fa -db cdd -outfmt 7 -out rpsblast.tsv && rpsbproc -i rpsblast.tsv -o architectures.tsv`
**Explanation:** Two-step: first, `rpsblast` runs the RPS-BLAST against the CDD database; second, `rpsbproc` converts the hits to domain architectures. Output `architectures.tsv` has one row per protein with the architecture.

### Use the XML output of RPS-BLAST
**Args:** `rpsblast -query proteins.fa -db cdd -outfmt 5 -out rpsblast.xml && rpsbproc -i rpsblast.xml --input-format xml -o architectures.tsv`
**Explanation:** `--input-format xml` parses the XML output of RPS-BLAST (more detailed than the tabular format). Useful for downstream tools that consume XML.

### Specify an E-value threshold
**Args:** `rpsbproc -i rpsblast.tsv --max-evalue 1e-5 -o architectures_strict.tsv`
**Explanation:** `--max-evalue 1e-5` filters to hits with E-value < 1e-5. Default is 1e-3. Strict threshold for high-confidence architectures.

### Output an ASN.1 file for the CDD viewer
**Args:** `rpsbproc -i rpsblast.tsv --output-asn architectures.asn -o architectures.tsv`
**Explanation:** `--output-asn` writes an ASN.1 binary file for the CDD web viewer. The viewer shows the per-domain architecture on the query sequence with the CDD domain models aligned.

### Mask low-complexity regions
**Args:** `rpsbproc -i rpsblast.tsv --mask-low-complexity -o architectures_masked.tsv`
**Explanation:** `--mask-low-complexity` (if available) masks low-complexity regions (e.g., coiled coils, transmembrane regions) before the architecture is built. Useful for filtering spurious domain hits.

### Restrict to specific domain types
**Args:** `rpsbproc -i rpsblast.tsv --domain-types "PKinase,SH2,SH3" -o architectures_filtered.tsv`
**Explanation:** `--domain-types` restricts the architecture to a list of domain types (comma-separated). Useful for focused analyses (e.g., only kinase domains in a kinome study).

### Compare architectures across species
**Args:** `rpsbproc -i human_rpsblast.tsv -o human_arch.tsv && rpsbproc -i mouse_rpsblast.tsv -o mouse_arch.tsv && diff <(cut -f3 human_arch.tsv) <(cut -f3 mouse_arch.tsv) | head`
**Explanation:** Composite: run RpsbProc on two species' proteomes, then diff the architecture strings. Useful for identifying lineage-specific domain architectures.
