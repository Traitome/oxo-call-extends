---
name: bamread
category: formatting
description: bamread - Read BAM files quickly into dataframes in Python
tags: [bamread, formatting, BAM, python, dataframe]
author: oxo-call-community
source_url: "https://github.com/endrebak/bamread"
---

## Concepts

- **Tool Overview**: bamread is a Python library that reads BAM files quickly into pandas DataFrames for efficient data analysis. Version 0.0.20.
- **Core Function**: Enables fast reading of BAM alignment data into pandas DataFrames for analysis.
- **Fast Reading**: Optimized for speed when reading large BAM files.
- **DataFrame Integration**: Seamlessly integrates with pandas for data manipulation and analysis.
- **Flexible Filtering**: Supports filtering reads during import.
- **Input/Output**: Accepts BAM files, outputs pandas DataFrames.
- **Installation**: `conda install -c bioconda bamread`.

## Pitfalls

- **Memory Usage**: Loading large BAM files into DataFrames can require significant memory.
- **DataFrame Size**: Very large datasets may not fit into memory.
- **Python Dependency**: Requires Python environment with pandas installed.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Basic BAM reading
**Args:** `python -c "import bamread; df = bamread.read_bam('alignments.bam'); print(df.head())"`
**Explanation:** Reads BAM file into pandas DataFrame and shows first 5 rows.

### Filter by mapping quality
**Args:** `python -c "import bamread; df = bamread.read_bam('alignments.bam', min_mapq=30)"`
**Explanation:** Reads only reads with mapping quality >= 30.

### Select specific columns
**Args:** `python -c "import bamread; df = bamread.read_bam('alignments.bam', columns=['qname', 'pos', 'mapq'])"`
**Explanation:** Reads only specified columns to reduce memory usage.

### Region-specific reading
**Args:** `python -c "import bamread; df = bamread.read_bam('alignments.bam', region='chr1:1000-2000')"`
**Explanation:** Reads only alignments in specified genomic region.

### Output to CSV
**Args:** `python -c "import bamread; df = bamread.read_bam('alignments.bam'); df.to_csv('bam_data.csv')"`
**Explanation:** Reads BAM and exports DataFrame to CSV file.

### Count reads by chromosome
**Args:** `python -c "import bamread; df = bamread.read_bam('alignments.bam'); print(df['rname'].value_counts())"`
**Explanation:** Reads BAM and counts reads per chromosome.

### Display help
**Args:** `python -c "import bamread; help(bamread.read_bam)"`
**Explanation:** Shows all available options for read_bam function.