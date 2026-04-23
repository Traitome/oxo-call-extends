---
name: colabfold
category: annotation
description: Making protein folding accessible to all using AlphaFold2 and MMseqs2
tags: [colabfold, protein-structure, alphafold, structure-prediction, mmseqs2]
author: oxo-call-community
source_url: "https://github.com/sokrypton/ColabFold"
---

## Concepts

- **Tool Overview**: ColabFold is a fast and accessible protein structure prediction tool that combines AlphaFold2 with MMseqs2 for rapid MSA generation, making structure prediction practical for large-scale use.
- **Core Function**: Predicts 3D protein structures from amino acid sequences using AlphaFold2's deep learning models with accelerated MSA search via MMseqs2.
- **Input/Output**: Input: FASTA file with protein sequences. Output: Predicted structures in PDB format, confidence scores (pLDDT), and MSA files.
- **MMseqs2 Acceleration**: Uses MMseqs2 instead of HHblits for MSA generation, reducing search time from hours to minutes.
- **Batch Processing**: Supports predicting structures for multiple sequences in a single run.
- **Multiple Modes**: Supports monomer, multimer (complex), and custom MSA input modes.

## Pitfalls

- **GPU Required**: Structure prediction requires GPU. CPU-only mode is extremely slow and not practical.
- **Sequence Length**: Very long sequences (>2000aa) may exceed GPU memory. Split into domains if possible.
- **MSA Depth**: Poor MSA depth (few homologs) reduces prediction accuracy. Consider providing custom MSA.
- **Recycle Count**: More recycles improve accuracy but increase runtime. Default 3 is sufficient for most cases.
- **Model Parameters**: Uses AlphaFold2 model weights. Ensure correct model version is downloaded.

## Examples

### Predict single protein structure
**Args:** `--input query.fasta --output results/`
**Explanation:** Predicts the 3D structure of a single protein sequence, outputs PDB files and confidence metrics.

### Predict protein complex (multimer)
**Args:** `--input complex.fasta --output results/ --model-type alphafold2_multimer_v2`
**Explanation:** Predicts the structure of a protein complex using the multimer model, with chains separated by ':' in FASTA.

### Use custom MSA
**Args:** `--input query.fasta --output results/ --msa-only`
**Explanation:** Only generates MSA without running structure prediction, useful for customizing MSA before prediction.

### Predict with custom templates
**Args:** `--input query.fasta --output results/ --templates custom_templates/`
**Explanation:** Uses custom template structures instead of searching the PDB database automatically.

### Batch prediction
**Args:** `--input multiple_sequences.fasta --output results/ --batch`
**Explanation:** Predicts structures for all sequences in the FASTA file in batch mode.

### Reduce recycles for faster prediction
**Args:** `--input query.fasta --output results/ --num-recycle 1`
**Explanation:** Reduces recycle count to 1 for faster (but potentially less accurate) predictions.

### Use specific GPU
**Args:** `--input query.fasta --output results/ --gpu 0`
**Explanation:** Specifies which GPU to use for prediction when multiple GPUs are available.

### Predict with amber relaxation
**Args:** `--input query.fasta --output results/ --use-amber`
**Explanation:** Applies AMBER force field relaxation to refine the predicted structure, improving physical plausibility.
