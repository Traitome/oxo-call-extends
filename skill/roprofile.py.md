---
name: roprofile.py
category: utility
description: Python module for generating pan-genome profile files from Roary output; the same functionality as the `roProfile` CLI but callable from Python pipelines.
tags: ["roprofile", "roary", "pangenome", "profile", "presence-absence", "python-api"]
author: oxo-call-community
source_url: "https://github.com/cimendes/roProfile"
---

## Concepts

- **Tool Overview**: roprofile.py (v1.4.5, cimendes) is the Python module underlying the `roProfile` CLI. It provides a class-based interface for reading Roary's `gene_presence_absence.csv`, computing per-gene statistics, and writing a tidy profile TSV — without spawning a subprocess.
- **Core Function**: The `RoaryProfile` class is the main entry point. It accepts a path to the Roary CSV, computes the gene-level statistics (presence count, frequency, group category, mean identity, paralog count), and exposes the result as a pandas DataFrame. The DataFrame is the canonical data structure for downstream analysis in Python.
- **Algorithm**: A pandas-based implementation that mirrors the CLI. The class is a thin wrapper around `pandas.read_csv` plus a small set of aggregation methods. The class is intended to be imported into a larger analysis pipeline (e.g., a Jupyter notebook, a Snakemake rule).
- **Input Format**: A path to a Roary `gene_presence_absence.csv` (passed to the constructor). The class reads the file once and stores the data; subsequent access is in-memory. The CSV must be the post-Roary version with the standard Roary column header.
- **Output Format**: A pandas DataFrame with one row per gene group and the columns `Gene, Annotation, Presence_count, Frequency, Group_category, Mean_identity, Num_paralogs, Isolate_names`. The DataFrame is the "profile" object and can be written to a file via `profile.to_csv()`.
- **Use Case**: Embedding Roary-profile generation in a Snakemake or Nextflow pipeline (no subprocess overhead), using the profile in a Jupyter notebook for interactive exploration, computing custom statistics on top of the standard profile (e.g., per-gene correlation with a phenotype), and integrating the profile with scikit-learn for ML-based pan-genome analyses.

## Pitfalls

- **CRITICAL — The module is installed as `roprofile`, not `roprofile.py`**: The Bioconda package name is `roprofile`; the module is imported as `import roprofile` (or `from roprofile import RoaryProfile`). A common mistake is `import roprofile.py` which fails on Python's import machinery.
- **CRITICAL — Pandas version must be ≥ 1.0**: The module uses `pandas.DataFrame.itertuples()` and other modern APIs. Older pandas (< 0.25) may produce deprecation warnings or runtime errors.
- **The class does NOT validate the Roary CSV schema**: A malformed or hand-edited CSV produces a silently-broken DataFrame (e.g., missing `Gene` column). Always verify with `pandas.read_csv` first if the CSV provenance is unclear.
- **The classification (core/accessory/unique) is hard-coded to 99%**: To change the threshold, subclass `RoaryProfile` and override `_classify_gene`. The CLI accepts `--core-threshold`; the Python API does not.
- **Paralog counts are integer counts, not flags**: The `Num_paralogs` column is the count (0 if no paralog). For a binary flag, use `df['Has_paralog'] = (df['Num_paralogs'] > 0).astype(int)`.
- **The DataFrame is not memory-optimized**: For very large pan-genomes (10,000+ gene groups), the in-memory DataFrame can be 100+ MB. Use `pandas.read_csv(chunksize=1000)` for streaming access.

## Examples

### Load a Roary profile into a DataFrame
**Args:** `python -c "from roprofile import RoaryProfile; p = RoaryProfile('gene_presence_absence.csv'); print(p.profile.head())"`
**Explanation:** Imports the `RoaryProfile` class, loads the Roary CSV, and prints the first few rows. The `.profile` attribute is the pandas DataFrame. Useful for a quick sanity check in a notebook.

### Compute per-gene statistics
**Args:** `python -c "from roprofile import RoaryProfile; p = RoaryProfile('gene_presence_absence.csv'); print(p.profile.groupby('Group_category').size())"`
**Explanation:** Groups the profile by `Group_category` (core / accessory / unique) and prints the count per category. Useful for a quick pan-genome summary.

### Write the profile to a TSV
**Args:** `python -c "from roprofile import RoaryProfile; p = RoaryProfile('gene_presence_absence.csv'); p.profile.to_csv('profile.tsv', sep='\t', index=False)"`
**Explanation:** Writes the profile DataFrame to a TSV file. Equivalent to the CLI's `roProfile -i ... -o profile.tsv`, but without spawning a subprocess.

### Filter to accessory genes
**Args:** `python -c "from roprofile import RoaryProfile; p = RoaryProfile('gene_presence_absence.csv'); accessory = p.profile[p.profile['Group_category'] == 'accessory']; print(len(accessory))"`
**Explanation:** Filters the profile to rows where `Group_category == 'accessory'` and prints the count. Useful for downstream accessory-gene analyses.

### Add a phenotype column via merge
**Args:** `python -c "from roprofile import RoaryProfile; import pandas as pd; p = RoaryProfile('gene_presence_absence.csv'); traits = pd.read_csv('traits.csv'); p.profile['Mean_trait'] = p.profile['Isolate_names'].apply(lambda x: traits.loc[traits['isolate'].isin(x.split(';')), 'trait'].mean())"`
**Explanation:** Composite: load the profile, load a traits table, and add a per-gene mean trait column. The mean trait is computed across the isolates in which the gene is present. Useful for a quick gene-phenotype correlation analysis.

### Use the profile with scikit-learn
**Args:** `python -c "from roprofile import RoaryProfile; from sklearn.cluster import KMeans; import pandas as pd; p = RoaryProfile('gene_presence_absence.csv'); X = pd.get_dummies(p.profile['Isolate_names'].str.get_dummies(';')).values; km = KMeans(n_clusters=5).fit(X); print(km.labels_[:10])"`
**Explanation:** Composite: load the profile, build a per-gene × per-isolate binary matrix from the `Isolate_names` column, and run K-means clustering. Useful for a quick pan-genome clustering.

### Stream a large CSV
**Args:** `python -c "from roprofile import RoaryProfile; p = RoaryProfile('large_gene_presence_absence.csv'); print(p.profile.shape)"`
**Explanation:** The constructor reads the entire CSV into memory; for very large CSVs (> 1 GB), use `pandas.read_csv(chunksize=1000)` and call `RoaryProfile.from_chunks` (if available) for streaming access.
