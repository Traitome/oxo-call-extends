---
name: scop3p
category: structural-biology
description: Scop3P - The official Scop3P REST API Python client
tags: ["scop3p", "structural-biology", "protein-structure", "API-client"]
author: oxo-call-community
source_url: "https://iomics.ugent.be/scop3p/documentation"
---

## Concepts

- **Tool Overview**: Scop3P (v1.1.0) is the official Scop3P REST API Python client.
- **Core Function**: Provides access to the Scop3P web service for protein structure analysis.
- **Algorithm**: Interacts with REST API for protein structure prediction and analysis.
- **Input/Output**: Accepts protein sequences and produces structure predictions.
- **Web Service**: Accesses remote server for computational protein structure analysis.
- **Applications**: Protein structure prediction, structural bioinformatics, and protein analysis.

## Pitfalls

- **Network Dependency**: Requires internet connectivity.
- **API Rate Limits**: May be subject to API rate limits.
- **Server Availability**: Depends on remote server availability.
- **Data Privacy**: Requires sending data to remote server.
- **Computation Time**: May have long computation times for complex analyses.
- **API Key**: May require API key for full access.

## Examples

### Basic structure prediction
**Args:** `import scop3p; result = scop3p.predict(sequence)`
**Explanation:** Predicts protein structure from sequence.

### Multiple sequences
**Args:** `import scop3p; results = scop3p.predict_batch(sequences)`
**Explanation:** Processes multiple sequences in batch.

### Advanced options
**Args:** `import scop3p; result = scop3p.predict(sequence, model='alphafold')`
**Explanation:** Specifies prediction model.

### Fetch results
**Args:** `import scop3p; result = scop3p.get_result(job_id)`
**Explanation:** Retrieves results for submitted job.

### Set API key
**Args:** `import scop3p; scop3p.set_api_key('your_key')`
**Explanation:** Configures API authentication.

### Check status
**Args:** `import scop3p; status = scop3p.check_status(job_id)`
**Explanation:** Checks job status.

### Download structure
**Args:** `import scop3p; scop3p.download_pdb(job_id, 'structure.pdb')`
**Explanation:** Downloads predicted structure in PDB format.