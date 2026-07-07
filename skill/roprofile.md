---
name: roprofile
category: utility
description: Generates pan-genome profile files (gene presence/absence, frequency, and per-sample gene counts) from Roary output, suitable for downstream tools like Scoary, pyseer, and custom association analyses.
tags: ["roprofile", "roary", "pangenome", "profile", "presence-absence", "scoary"]
author: oxo-call-community
source_url: "https://github.com/cimendes/roProfile"
---

## Concepts

- **Tool Overview**: roProfile (v1.4.5, cimendes) is a small Python utility that converts the Roary pan-genome matrix (`gene_presence_absence.csv`) into a profile file that downstream association tools (Scoary, pyseer) expect. It is essentially a Roary-output re-formatter with additional QC metrics.
- **Core Function**: Takes the Roary `gene_presence_absence.csv` (or Rtab) and produces a profile TSV with per-gene metadata: gene name, annotation, presence count, group ID, and a "core" / "accessory" / "unique" label. The output can be used as input to Scoary, pyseer, or any tool that expects a per-gene metadata table.
- **Algorithm**: A simple pandas-based reformatting: read the Roary CSV, compute per-gene statistics (presence count, frequency, mean pairwise identity, number of paralogs), and write a tidy TSV with one row per gene group. The classification (core/accessory/unique) is based on the Roary `-cd` threshold (default 99%).
- **Input Format**: A Roary `gene_presence_absence.csv` (the standard output) or `gene_presence_absence.Rtab` (the binary form). The script accepts either via `--input` (auto-detect). The input must be the post-Roary version, with the standard Roary column header.
- **Output Format**: A TSV with one row per gene group: `Gene, Annotation, Presence_count, Frequency, Group_category, Mean_identity, Num_paralogs, Isolate_names`. The `Group_category` is "core" (present in ≥ 99% of genomes), "accessory" (present in 2–98%), or "unique" (present in 1 genome). Output to stdout by default; redirect with `-o`.
- **Use Case**: Pre-processing Roary output for Scoary (gene-phenotype association), feeding a pangenome profile into pyseer for genome-wide association, generating a tidy gene-presence matrix for a custom R / Python analysis, and producing a per-gene summary table for a paper's supplement.

## Pitfalls

- **CRITICAL — The Roary CSV must be the post-Roary, not the pre-Roary version**: A `gene_presence_absence.csv` produced by a different tool (or a hand-edited one) will not have the standard Roary columns and will produce a malformed profile. Verify with `head -1 gene_presence_absence.csv`.
- **CRITICAL — Comma-containing gene annotations break parsing**: If the Annotation column contains commas (e.g., `Klebsiella, partial`), the CSV parsing produces extra columns. Pre-process with `sed -i 's/,/_/g' gene_presence_absence.csv` to replace commas with underscores.
- **The "core" threshold is taken from Roary's `-cd` setting**: The Roary run must have used the desired `-cd` value; if you want a stricter core (100% of genomes), re-run Roary with `-cd 100` rather than re-classifying the profile.
- **Paralog counts may be inconsistent with downstream tools**: Roary counts paralogs in the `Number of paralogs` column; Scoary expects a binary "any paralog" flag. Use `--collapse-paralogs` to convert to a binary flag.
- **Output is a "snapshot" of the Roary run**: If you re-run Roary with different parameters (e.g., different `-i` BLASTP identity), the profile will be inconsistent. Re-run roProfile after every Roary run.
- **The "frequency" column is the fraction, not the count**: The `Presence_count` is the integer count; the `Frequency` is `count / num_genomes`. Some downstream tools expect the count, some expect the fraction; verify the tool's documentation.

## Examples

### Basic profile generation
**Args:** `roProfile -i gene_presence_absence.csv -o profile.tsv`
**Explanation:** `-i` is the Roary CSV, `-o` is the output profile TSV. The output has one row per gene group with `Gene, Annotation, Presence_count, Frequency, Group_category, Mean_identity, Num_paralogs, Isolate_names`.

### Use the Rtab as input
**Args:** `roProfile -i gene_presence_absence.Rtab --input-format rtab -o profile.tsv`
**Explanation:** `--input-format rtab` reads the Roary binary Rtab format. Equivalent output to the CSV conversion.

### Custom core-gene threshold
**Args:** `roProfile -i gene_presence_absence.csv --core-threshold 1.0 -o profile_strict.tsv`
**Explanation:** `--core-threshold 1.0` requires a gene to be in 100% of genomes to be classified as "core" (overrides the default 99%). Useful for a strict-core pan-genome.

### Collapse paralogs to a binary flag
**Args:** `roProfile -i gene_presence_absence.csv --collapse-paralogs -o profile_paralogs.tsv`
**Explanation:** `--collapse-paralogs` converts the `Number of paralogs` column to a binary "has paralog" flag. Required for Scoary, which expects binary paralog information.

### Use the profile with Scoary
**Args:** `roProfile -i gene_presence_absence.csv -o profile.tsv && scoary -t traits.csv -g profile.tsv -o scoary_out/`
**Explanation:** Composite: build the profile, then run Scoary on it. `-t traits.csv` is the phenotype file (one row per isolate, one column per trait). The output `scoary_out/` contains per-trait association results.

### Add a custom metadata column
**Args:** `roProfile -i gene_presence_absence.csv --metadata sample_metadata.tsv -o profile_with_meta.tsv`
**Explanation:** `--metadata` adds a per-sample metadata table to the profile. Each gene row includes the metadata of the isolates in which it is present. Useful for QC and stratified analyses.

### Output a JSON profile
**Args:** `roProfile -i gene_presence_absence.csv --format json -o profile.json`
**Explanation:** `--format json` outputs the profile in JSON instead of TSV. Useful for downstream pipelines that consume JSON (e.g., a Snakemake rule that parses the profile in Python).
