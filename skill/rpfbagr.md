---
name: rpfbagr
category: utility
description: Retrosynthesis Pathway FBA with Gene Ranking (rpfbagr) — predicts gene knockout targets that maximize a target metabolite's production when a heterologous pathway is inserted, ranking knockouts by their impact on production.
tags: ["rpfbagr", "fba", "flux-balance-analysis", "knockout-ranking", "metabolic-engineering", "retrosynthesis"]
author: oxo-call-community
source_url: "https://github.com/brsynth/rpfbagr"
---

## Concepts

- **Tool Overview**: rpfbagr (v2.2.2, brsynth) is a CLI wrapper for predicting gene knockout targets in a metabolic model after a heterologous pathway insertion, with a per-gene ranking of knockout impact. It extends `rpfa` (OptGene/OptKnock) with a gene-level sensitivity analysis that ranks single and double gene knockouts by their effect on target production.
- **Core Function**: Takes a genome-scale metabolic model (GSM), a heterologous pathway, and a target metabolite, and reports a ranked list of single and double gene knockouts that increase target production. The ranking is by the FBA-predicted target production rate after the knockout.
- **Algorithm**: A sensitivity analysis over single and double gene knockouts: for each candidate knockout (or pair), re-solve the FBA, record the target production rate, and rank by the rate. The sensitivity analysis uses COBRApy; the underlying FBA is the same as in `rpfa`. For very large GSMs, the analysis can be restricted to a candidate set.
- **Input Format**: (1) An SBML file with the host GSM; (2) a JSON or YAML pathway description; (3) a target metabolite; (4) optional: a candidate gene set (a TSV of gene IDs to evaluate). The SBML must be COBRA-compatible; the candidate set restricts the search to a focused set of genes (e.g., transcription factors, known regulatory genes).
- **Output Format**: A TSV with one row per knockout: `gene1, gene2, target_production_rate, growth_rate, rank`. The `rank` is 1 for the top-scoring knockout. The output is sorted by `target_production_rate` descending.
- **Use Case**: The standard step in a retrosynthesis-driven cell factory design (the canonical use case for the brsynth pipeline), identifying the top gene knockout candidates for experimental validation, prioritizing knockouts for a metabolic engineering project, and producing a knockout shortlist for a combinatorial library screen.

## Pitfalls

- **CRITICAL — The GSM must be COBRA-compatible**: A SBML file from BiGG Models is COBRA-compatible; a custom SBML may not load. Verify with `cobra.io.read_sbml_model("model.xml")` first.
- **CRITICAL — Double-knockout analysis is combinatorial**: For 2000 genes, the number of double knockouts is 2000 × 1999 / 2 = ~2M, which takes ~10 hours. Restrict to a candidate set (e.g., 100 transcription factors) for a tractable analysis.
- **The target production rate is the FBA-predicted UPPER BOUND**: FBA assumes a steady-state metabolic flux; the actual production is typically 30–50% lower. Use the result to rank knockouts, not to predict absolute production.
- **Knockouts that increase production but kill growth are not useful**: A knockout that doubles the target production rate but drops the growth rate to zero is a "growth-decoupled" knockout and is not industrially viable. Filter the output to knockouts with `growth_rate > 0.1` (or a similar threshold).
- **No automatic medium adjustment**: The default medium is the GSM's default. For a minimal medium screen, pre-set the medium in COBRApy before running rpfbagr.
- **The ranking does not account for genetic interactions (epistasis)**: A single knockout may rank highly, but a double knockout combining two highly-ranked single knockouts may not improve production. For epistasis-aware ranking, use a combinatorial optimization tool (e.g., OptKnock).

## Examples

### Basic single-gene knockout ranking
**Args:** `rpfbagr --model iJO1366.xml --pathway pathway.json --target lycopene --out knockouts.tsv`
**Explanation:** `--model` is the SBML GSM, `--pathway` is the heterologous pathway JSON, `--target` is the target metabolite, `--out` is the output TSV. The output has one row per single-gene knockout, ranked by lycopene production rate.

### Restrict to a candidate gene set
**Args:** `rpfbagr --model iJO1366.xml --pathway pathway.json --target lycopene --candidates tfs.txt --out knockouts_tfs.tsv`
**Explanation:** `--candidates` is a TSV with one gene ID per line. The analysis is restricted to these genes (e.g., transcription factors). Speeds up the analysis and focuses on regulatory targets.

### Run a double-knockout analysis
**Args:** `rpfbagr --model iJO1366.xml --pathway pathway.json --target lycopene --double-knockout --candidates tfs.txt --out double_knockouts.tsv`
**Explanation:** `--double-knockout` enables the double-knockout analysis. The output has one row per pair of gene knockouts. The number of rows is `C(n, 2)` for `n` candidate genes. Slow for large candidate sets.

### Filter to growth-coupled knockouts
**Args:** `rpfbagr --model iJO1366.xml --pathway pathway.json --target lycopene --min-growth 0.1 --out knockouts_growth.tsv`
**Explanation:** `--min-growth 0.1` filters the output to knockouts with growth rate > 0.1 (in h⁻¹). Useful for restricting to industrially viable knockouts.

### Specify a custom medium
**Args:** `rpfbagr --model iJO1366.xml --pathway pathway.json --target lycopene --medium minimal_glucose --out knockouts_medium.tsv`
**Explanation:** `--medium minimal_glucose` specifies a minimal glucose medium (defined in the GSM). Useful for industrial production scenarios.

### Use a different solver
**Args:** `rpfbagr --model iJO1366.xml --pathway pathway.json --target lycopene --solver cplex --out knockouts.tsv`
**Explanation:** `--solver cplex` uses CPLEX instead of the default GLPK. Much faster for large models and double-knockout analyses.

### Compare with a no-knockout baseline
**Args:** `rpfbagr --model iJO1366.xml --pathway pathway.json --target lycopene --include-baseline --out knockouts_with_baseline.tsv`
**Explanation:** `--include-baseline` adds a row for the no-knockout (wild-type) prediction. The first row in the output is the baseline; subsequent rows are ranked single-gene knockouts.
