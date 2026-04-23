---
name: ananse
category: epigenomics
description: ANANSE - Predict key transcription factors in cell fate determination using enhancer-based gene regulatory networks
tags: [enhancer, gene-regulatory-network, transcription-factor, cell-fate, binding]
author: oxo-call-community
source_url: "https://github.com/vanheeringen-lab/ANANSE"
---

## Concepts

- **Tool Overview**: ANANSE (ANalysis Algorithm for Networks Specified by Enhancers) infers enhancer-based gene regulatory networks and predicts key transcription factors controlling cell fate transitions. Version 0.5.1.
- **Three-Step Workflow**: `ananse binding` (enhancer-TF binding) → `ananse network` (GRN inference) → `ananse influence` (TF importance for cell fate change).
- **Enhancer Integration**: Uses enhancer regions (ATAC-seq/ChIP-seq peaks) combined with motif scanning to connect TFs to target genes via enhancers.
- **Network Inference**: Integrates binding evidence, gene expression, and enhancer-gene links to construct comprehensive gene regulatory networks.
- **Influence Analysis**: Compares GRNs between two cell types to identify TFs with highest influence on cell fate transition.
- **Data Requirements**: ATAC-seq/ChIP-seq peaks, RNA-seq expression data, genome annotation, and motif database.
- **scANANSE Extension**: Single-cell version available for GRN analysis of individual cell clusters.

## Pitfalls

- **Genome Version**: All input files must use the same genome version (e.g., hg38). Mismatched genome versions cause incorrect enhancer-gene assignments.
- **Motif Database**: Requires motif database (e.g., JASPAR) for TF binding prediction. Download appropriate version before running.
- **Memory Usage**: Large enhancer collections and genomes require substantial memory for network inference. 32GB+ recommended.
- **Enhancer-Gene Linking**: Quality of GRN depends on accurate enhancer-gene linking. Use appropriate distance thresholds or Hi-C data when available.
- **Expression Input**: Requires proper normalization of RNA-seq data. TPM or FPKM values recommended.
- **Cell Type Comparison**: Influence analysis requires GRNs from two distinct cell types. Ensure proper sample selection.

## Examples

### Step 1: Predict TF binding at enhancers
**Args:** `ananse binding -a enhancer.bed -g hg38 -m JASPAR2022.pwm -o binding.h5`
**Explanation:** Scans enhancer regions for TF binding motifs using JASPAR database. Outputs binding probability matrix. First step in ANANSE workflow.

### Step 2: Infer gene regulatory network
**Args:** `ananse network -b binding.h5 -e expression.tsv -g hg38 -o network.h5`
**Explanation:** Constructs GRN by integrating binding predictions with gene expression data. Expression file should have gene IDs and TPM/FPKM values. Core GRN inference step.

### Step 3: Identify key TFs for cell fate transition
**Args:** `ananse influence -n source_network.h5 target_network.h5 -g hg38 -o influence_results/`
**Explanation:** Compares source and target cell type GRNs to identify TFs with highest influence on cell fate transition. Outputs ranked TF list and influence scores.

### Complete workflow
**Args:** `ananse binding -a peaks.bed -g hg38 -m motifs.pwm -o bind.h5 && ananse network -b bind.h5 -e expr.tsv -g hg38 -o net.h5 && ananse influence -n source_net.h5 net.h5 -g hg38 -o results/`
**Explanation:** Full three-step workflow: binding prediction, network inference, and influence analysis. Chain commands with && for automated processing.

### Use ATAC-seq peaks as enhancers
**Args:** `ananse binding -a ATAC_peaks.narrowPeak -g hg38 -m JASPAR2022.pwm -o atac_binding.h5`
**Explanation:** Uses ATAC-seq peak regions as enhancer input. NarrowPeak format supported. Common approach when ChIP-seq data is unavailable.

### Custom enhancer-gene distance
**Args:** `ananse network -b binding.h5 -e expression.tsv -g hg38 -o network.h5 --enhancer-to-gene-distance 100000`
**Explanation:** Sets maximum enhancer-gene linking distance to 100kb. Default may be too permissive for compact genomes or too restrictive for large genomes.

### Single-cell ANANSE (scANANSE)
**Args:** `ananse binding -a sc_peaks.bed -g hg38 -m motifs.pwm -o sc_binding.h5`
**Explanation:** Same workflow applied to single-cell cluster-specific peaks. Use with scanpy/anndata for single-cell GRN analysis per cell cluster.