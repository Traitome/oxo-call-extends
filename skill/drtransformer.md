---
name: drtransformer
category: expression
description: "Heuristic cotranscriptional folding using the nearest neighbor energy model."
tags: [drtransformer, expression, RNA-folding, cotranscriptional, thermodynamics]
author: oxo-call-community
source_url: "https://pypi.org/project/drtransformer/"
---

## Concepts

- **Tool Overview**: DRTransformer is a tool for heuristic cotranscriptional RNA folding using the nearest neighbor energy model.
- **Core Function**: Predicts RNA secondary structure formation during transcription.
- **Input/Output**: Input: RNA sequences (FASTA). Output: Folding trajectories, energy landscapes, structure predictions.
- **Algorithm**: Uses dynamic programming with nearest neighbor thermodynamic parameters.
- **Key Features**: Cotranscriptional folding simulation, kinetic analysis, multiple folding pathways, energy landscape visualization.
- **Installation**: `conda install -c bioconda drtransformer`

## Pitfalls

- **Sequence Length**: Very long sequences may require significant computation time.
- **Thermodynamic Parameters**: Results depend on accuracy of energy parameters.
- **Kinetic Traps**: May not capture all kinetic folding intermediates.
- **Temperature Effects**: Default temperature may not match experimental conditions.
- **Ion Concentrations**: Salt conditions affect folding predictions.

## Examples

### Basic folding prediction
**Args:** `--input sequence.fasta --output structures.txt`
**Explanation:** Predicts cotranscriptional folding for RNA sequence.

### With temperature
**Args:** `--input sequence.fasta --output structures.txt --temperature 37`
**Explanation:** Sets folding temperature to 37°C.

### Kinetic analysis
**Args:** `--input sequence.fasta --output structures.txt --kinetic`
**Explanation:** Performs kinetic analysis of folding pathways.

### Energy landscape
**Args:** `--input sequence.fasta --output landscape.png --plot`
**Explanation:** Generates energy landscape visualization.

### Multiple sequences
**Args:** `--input sequences.fasta --output structures.txt --batch`
**Explanation:** Processes multiple RNA sequences in batch mode.