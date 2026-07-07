---
name: meneco
category: utility
description: Metabolic network completion tool that computes minimal completions using repair networks.
tags: [meneco, metabolic-model, network-analysis]
author: oxo-call-community
source_url: "http://bioasp.github.io/meneco/"
---

## Concepts

- **Tool Overview**: Meneco completes metabolic networks using repair reactions.
- **Core Function**: Computes minimal network completions.
- **Repair Network**: Uses external repair network for missing reactions.
- **Gap Filling**: Identifies and fills gaps in metabolic models.
- **Flux Balance**: Ensures network functionality.
- **Installation**: `conda install -c bioconda meneco`

## Pitfalls

- **Model Format**: Requires specific SBML format.
- **Repair Network**: Depends on comprehensive repair network.
- **Computation Time**: Slow for large networks.
- **Memory Requirements**: High memory for complex models.
- **Parameter Tuning**: Requires careful configuration.
- **Result Interpretation**: Complex output requires expertise.

## Examples

### Complete metabolic network
**Args:** `meneco -d draft.xml -r repair.xml -o completed.xml`
**Explanation:** Completes draft metabolic network.

### With target compounds
**Args:** `meneco -d draft.xml -r repair.xml -t targets.txt -o completed.xml`
**Explanation:** Targets specific compounds for production.

### Verbose mode
**Args:** `meneco -d draft.xml -r repair.xml -v -o completed.xml`
**Explanation:** Shows detailed completion process.

### List repair reactions
**Args:** `meneco --list-reactions repair.xml`
**Explanation:** Lists available repair reactions.

### Help documentation
**Args:** `meneco --help`
**Explanation:** Displays available options.
