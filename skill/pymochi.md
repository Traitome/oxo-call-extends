---
name: pymochi
category: variant-calling
description: MoCHI uses neural networks to quantify energies, couplings, and epistasis from deep mutational scanning data.
tags: [pymochi, variant-calling, neural-networks, dms]
author: oxo-call-community
source_url: "https://github.com/lehner-lab/MoCHI"
---

## Concepts

- **Tool Overview**: pymochi analyzes mutational data.
- **Core Function**: Energy quantification.
- **Algorithm**: Uses neural networks.
- **Input Format**: Accepts DMS data.
- **Output**: Produces energy models.
- **Use Case**: Protein engineering.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Requires GPU memory.
- **Data Quality**: Results depend on input quality.
- **Model Complexity**: May overfit.
- **Runtime**: Training may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pymochi --help`
**Explanation:** Shows available options and usage instructions.

### Train model
**Args:** `pymochi train -i dms_data.txt -o model.pkl`
**Explanation:** Trains neural network model.

### With parameters
**Args:** `pymochi train -i dms_data.txt -p params.yaml -o model.pkl`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pymochi -v train -i dms_data.txt -o model.pkl`
**Explanation:** Runs with verbose output.

### Use GPU
**Args:** `pymochi --gpu train -i dms_data.txt -o model.pkl`
**Explanation:** Uses GPU for acceleration.

### Predict energies
**Args:** `pymochi predict -i model.pkl -d new_data.txt -o predictions.txt`
**Explanation:** Predicts energies for new mutations.

### Generate report
**Args:** `pymochi train -i dms_data.txt -o model.pkl --report report.html`
**Explanation:** Generates HTML report.