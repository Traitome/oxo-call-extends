---
name: assemblytics
category: variant-calling
description: Assemblytics - Detect and analyze structural variants from genome assembly alignments
tags: [structural-variant, assembly, nucmer, delta, variant-calling]
author: oxo-call-community
source_url: "https://github.com/MariaNattestad/Assemblytics"
---

## Concepts

- **Tool Overview**: Assemblytics detects and analyzes structural variants from de novo genome assembly aligned to a reference genome. Uses unique anchor filtering for robustness to repeats. Version 1.2.1.
- **Assembly-Based SVs**: Identifies variants by comparing assembled genome to reference, detecting insertions, deletions, tandem expansions, contractions, and other SVs.
- **Anchor Filtering**: Unique anchor filtering approach increases robustness to repetitive elements. Reduces false positives from misassemblies in repetitive regions.
- **Six Variant Classes**: Identifies six classes of variants based on alignment signatures: insertions, deletions, tandem expansions, tandem contractions, repeat expansions, and novel insertions.
- **Input Format**: Requires MUMmer nucmer delta file from assembly-to-reference alignment. Standard whole-genome alignment output.
- **Web Interface**: Available as web tool at assemblytics.com for quick analysis without installation. Upload delta file and get results.
- **Visualization**: Generates publication-quality plots showing variant size distributions and genomic locations.

## Pitfalls

- **Assembly Quality**: Poor quality assemblies with misassemblies produce false variant calls. QC assembly before running Assemblytics.
- **Reference Quality**: Gaps or errors in reference genome may appear as variants. Use high-quality reference genomes.
- **Repetitive Regions**: Highly repetitive regions may still produce false positives despite anchor filtering. Verify variants in repeats manually.
- **Alignment Parameters**: Nucmer alignment parameters affect variant detection. Use appropriate parameters for assembly-to-reference comparison.
- **Size Range**: Most sensitive for variants 50bp-10kb. Very large SVs (>100kb) may be missed or misclassified.
- **Strand Orientation**: Inversions not detected by standard Assemblytics. Requires separate analysis for inversions.

## Examples

### Basic Assemblytics analysis
**Args:** `Assemblytics -delta assembly.delta -out output_prefix -unique_anchor_length 10000 -min_variant_size 50 -max_variant_size 10000000`
**Explanation:** Standard analysis: processes delta file from nucmer alignment. Unique anchor length 10kb, variant size range 50bp-10Mb. Outputs variant calls and plots.

### Run via web interface
**Args:** Upload delta file at assemblytics.com, set unique anchor length to 10000, click "Run Assemblytics"
**Explanation:** Web-based analysis without installation. Maximum delta file size limits apply. Good for quick analysis of small assemblies.

### Generate nucmer alignment for Assemblytics
**Args:** `nucmer --maxmatch -c 100 -p assembly reference.fa query_assembly.fa`
**Explanation:** Creates MUMmer alignment required by Assemblytics. --maxmatch finds all matches. -c 100 sets minimum cluster length. Output: assembly.delta.

### Adjust unique anchor length
**Args:** `Assemblytics -delta assembly.delta -out output -unique_anchor_length 20000 -min_variant_size 50 -max_variant_size 10000000`
**Explanation:** Longer unique anchor length (20kb) increases stringency. Reduces false positives in repetitive genomes but may miss real variants.

### Focus on small variants
**Args:** `Assemblytics -delta assembly.delta -out output -unique_anchor_length 10000 -min_variant_size 10 -max_variant_size 1000`
**Explanation:** Detects only small variants (10bp-1kb). Useful for detailed analysis of small indels. May miss larger structural variants.

### Filter for high-confidence variants
**Args:** `Assemblytics -delta assembly.delta -out output -unique_anchor_length 15000 -min_variant_size 100 -max_variant_size 1000000`
**Explanation:** Conservative settings: longer anchors (15kb), larger minimum size (100bp). Higher confidence calls but may miss true small variants.

### Generate only variant summary
**Args:** `Assemblytics -delta assembly.delta -out output -unique_anchor_length 10000 -min_variant_size 50 -max_variant_size 10000000 --skip_plots`
**Explanation:** Skips plot generation for faster runtime. Outputs variant table only. Useful for automated pipelines.