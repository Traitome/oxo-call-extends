---
name: iucn_sim
category: utility
description: Simulate future extinctions and extinction rates for a given set of species, based on IUCN threat assessments.
tags: [iucn_sim, utility, conservation, extinction, IUCN]
author: oxo-call-community
source_url: "https://github.com/tobiashofmann88/iucn_extinction_simulator"
---

## Concepts

- **Tool Overview**: iucn_sim (v2.2.0) - A tool for simulating species extinction risks based on IUCN Red List categories and threat assessments.
- **IUCN Categories**: Uses IUCN threat categories (LC, NT, VU, EN, CR, EW, EX) to model extinction probabilities over time.
- **Population Dynamics**: Incorporates population growth rates, carrying capacities, and environmental stochasticity.
- **Extinction Risk Models**: Implements various extinction risk models including exponential growth, logistic growth, and stochastic processes.
- **Climate Change Integration**: Can incorporate climate change impacts on species distributions and survival.
- **Scenario Analysis**: Supports multiple scenarios to compare different conservation strategies and their effectiveness.

## Pitfalls

- **Data Quality**: Results depend heavily on the quality and completeness of input IUCN data.
- **Model Assumptions**: Simplified population models may not capture real-world complexity.
- **Uncertainty Propagation**: High uncertainty in input parameters can lead to unreliable predictions.
- **Taxonomic Bias**: May not handle understudied taxa with limited data appropriately.
- **Time Scale Limitations**: Long-term predictions (>50 years) become increasingly uncertain.
- **Climate Data Resolution**: Coarse climate data may miss local-scale impacts on species.

## Examples

### Basic extinction simulation
**Args:** `iucn_sim --input species_data.csv --output results/`
**Explanation:** Runs extinction simulation using default parameters and writes results to output directory.

### Specify time horizon
**Args:** `iucn_sim -i data.csv -o results/ --years 100`
**Explanation:** Simulates extinction risks over a 100-year time period.

### Include climate change
**Args:** `iucn_sim -i data.csv -o results/ --climate-scenario rcp85`
**Explanation:** Incorporates RCP8.5 climate change scenario into the simulation.

### Multiple scenarios
**Args:** `iucn_sim -i data.csv -o results/ --scenarios baseline conservation`
**Explanation:** Runs simulation for both baseline and conservation intervention scenarios.

### Set stochastic replicates
**Args:** `iucn_sim -i data.csv -o results/ --replicates 1000`
**Explanation:** Runs 1000 stochastic replicates to quantify uncertainty.

### Filter by region
**Args:** `iucn_sim -i data.csv -o results/ --region "Europe" --biome "Temperate"`
**Explanation:** Filters species to only include those in European temperate biomes.