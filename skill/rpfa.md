---
name: rpfa
category: utility
description: Retrosynthesis Pathway FBA Analysis (rpfa) — CLI wrapper for running OptGene/OptKnock flux-balance-analysis with a heterologous pathway insertion, used in retrosynthetic design of microbial cell factories.
tags: ["rpfa", "fba", "flux-balance-analysis", "optknock", "optgene", "metabolic-engineering"]
author: oxo-call-community
source_url: "https://github.com/brsynth/rpFbaAnalysis"
---

## Concepts

- **Tool Overview**: rpfa (v1.0.1, brsynth / Bristol SynBio) is a command-line wrapper for running OptGene/OptKnock flux-balance-analysis (FBA) simulations with a heterologous pathway insertion. It is part of the brsynth retrosynthesis pipeline and is used to evaluate whether a heterologous pathway (synthesized via retrosynthesis) can sustain growth in a host organism.
- **Core Function**: Takes a genome-scale metabolic model (GSM, in SBML), a heterologous pathway (a list of reactions to add), and a target metabolite, and runs an FBA simulation that predicts (1) the maximum growth rate of the host, and (2) the maximum production rate of the target, with the pathway inserted. OptKnock identifies the gene knockouts required to couple growth to production.
- **Algorithm**: A standard FBA formulation (linear programming) with OptKnock's bilevel optimization (a nested LP that maximizes the target production while constraining growth). The heterologous pathway is added to the GSM as a new set of reactions; the biomass equation is the optimization target. COBRApy is the underlying solver.
- **Input Format**: (1) An SBML file with the host GSM (e.g., `iJO1366.xml` for E. coli); (2) a JSON or YAML file describing the heterologous pathway (list of reactions, KEGG IDs, stoichiometry); (3) an optional list of gene knockouts to evaluate (OptKnock mode). The SBML must be COBRA-compatible.
- **Output Format**: A JSON or TSV with the FBA results: `growth_rate, target_production_rate, pathway_fluxes, knockout_suggestions`. In OptKnock mode, the output also includes the list of gene knockouts that achieve the target production.
- **Use Case**: The standard FBA step in a retrosynthesis-based cell-factory design (the canonical use case for the brsynth pipeline), screening heterologous pathways for growth-coupled production, identifying required gene knockouts in a metabolic engineering project, and validating a retrosynthesis-derived pathway against a GSM.

## Pitfalls

- **CRITICAL — The GSM must be COBRA-compatible**: A SBML file from BiGG Models (e.g., `iJO1366`) is COBRA-compatible; a SBML from a custom pipeline may not load. Verify with `cobra.io.read_sbml_model("model.xml")` in a Python REPL.
- **CRITICAL — The heterologous pathway must be specified in COBRA reaction format**: A pathway described as "A + B -> C" must be converted to a COBRA reaction object with stoichiometry and bounds. The brsynth retrosynthesis tools produce COBRA-compatible pathway JSON; hand-written pathways may need manual conversion.
- **OptKnock is computationally expensive**: A 5-knockout OptKnock search on a 2000-reaction GSM takes ~30 minutes. Reduce the knockout count or use OptGene (a faster evolutionary algorithm) for exploratory work.
- **FBA assumes a steady-state metabolic flux**: FBA does not model kinetics, regulation, or enzyme capacity. The predicted growth rate is an upper bound; the actual growth rate is typically 30–50% lower. Use the result as a feasibility check, not a quantitative prediction.
- **No automatic biomass equation update**: Adding a heterologous pathway does not update the host's biomass equation. If the pathway consumes a biomass precursor (e.g., an amino acid), the prediction may be inaccurate. Update the biomass equation manually if needed.
- **The default solver is GLPK**: GLPK is open-source but slower than CPLEX or Gurobi. For large models or OptKnock searches, install a commercial solver via `pip install cplex` or `gurobipy` and select with `cobra.Configuration().solver = "cplex"`.

## Examples

### Basic FBA with a heterologous pathway
**Args:** `rpfa --model iJO1366.xml --pathway pathway.json --target lycopene --out fba_results.json`
**Explanation:** `--model` is the SBML GSM, `--pathway` is the heterologous pathway JSON, `--target` is the target metabolite (must be in the GSM), `--out` is the output JSON. The output has the predicted growth rate and lycopene production rate.

### OptKnock mode
**Args:** `rpfa --model iJO1366.xml --pathway pathway.json --target lycopene --optknock --max-knockouts 5 --out optknock_results.json`
**Explanation:** `--optknock` enables OptKnock's bilevel optimization. `--max-knockouts 5` allows up to 5 gene knockouts. The output includes the knockout set that maximizes lycopene production while maintaining growth.

### OptGene mode (faster, evolutionary algorithm)
**Args:** `rpfa --model iJO1366.xml --pathway pathway.json --target lycopene --optgene --population 100 --generations 50 --out optgene_results.json`
**Explanation:** `--optgene` switches to OptGene's evolutionary algorithm. `--population 100 --generations 50` are the EA hyperparameters. Faster than OptKnock for large knockout spaces.

### Use a different solver
**Args:** `rpfa --model iJO1366.xml --pathway pathway.json --target lycopene --solver cplex --out fba_results.json`
**Explanation:** `--solver cplex` uses CPLEX instead of GLPK. Requires the `cplex` Python package. Much faster for large models.

### Specify a custom medium
**Args:** `rpfa --model iJO1366.xml --pathway pathway.json --target lycopene --medium minimal_glucose --out fba_results.json`
**Explanation:** `--medium minimal_glucose` specifies a minimal medium with glucose as the sole carbon source. The model file `iJO1366.xml` includes medium definitions; this selects one of them.

### Output a flux distribution
**Args:** `rpfa --model iJO1366.xml --pathway pathway.json --target lycopene --output-fluxes flux_dist.json --out fba_results.json`
**Explanation:** `--output-fluxes` writes the per-reaction flux distribution as a JSON. Useful for inspecting the active pathway and identifying flux bottlenecks.

### Run a parameter sweep
**Args:** `for ko_count in 1 2 3 4 5; do rpfa --model iJO1366.xml --pathway pathway.json --target lycopene --optknock --max-knockouts $ko_count --out optknock_${ko_count}.json; done`
**Explanation:** Composite: sweep the OptKnock knockout count from 1 to 5 and produce a per-knockout-count result file. Useful for understanding the trade-off between knockout burden and lycopene production.
