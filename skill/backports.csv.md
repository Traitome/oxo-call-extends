---
name: backports.csv
category: programming
description: backports.csv - Backport of Python 3 csv module for Python 2/3 compatibility
tags: [backports.csv, programming, csv, python2, compatibility]
author: oxo-call-community
source_url: "https://github.com/ryanhiebert/backports.csv"
---

## Concepts

- **Tool Overview**: backports.csv is a backport of Python 3's csv module to provide consistent CSV handling across Python 2 and Python 3 environments. Version 1.0.1.
- **Core Function**: Provides Python 3 csv module functionality to Python 2 environments, ensuring code compatibility.
- **CSV Handling**: Supports reading and writing CSV files with various dialects and formatting options.
- **Unicode Support**: Properly handles Unicode characters in CSV data.
- **Python 2/3 Compatibility**: Enables the same CSV code to run on both Python 2 and Python 3.
- **Drop-in Replacement**: Can be used as a drop-in replacement for the standard csv module.
- **Installation**: `conda install -c bioconda backports.csv` or `pip install backports.csv`.

## Pitfalls

- **Python 2 Deprecation**: Python 2 is no longer supported. Migrate to Python 3 if possible.
- **Version Compatibility**: Ensure compatibility with other dependencies in mixed Python environments.
- **Encoding Issues**: Be aware of encoding differences between Python 2 and Python 3 when handling CSV files.
- **Performance**: Slight performance overhead compared to native csv module.

## Examples

### Read CSV file
**Args:** `python -c "from backports.csv import reader; [print(row) for row in reader(open('data.csv'))]"`
**Explanation:** Reads CSV file and prints each row as a list.

### Write CSV file
**Args:** `python -c "from backports.csv import writer; w = writer(open('output.csv', 'w')); w.writerow(['Name', 'Value']); w.writerow(['Sample1', '100'])"`
**Explanation:** Writes data to CSV file.

### DictReader usage
**Args:** `python -c "from backports.csv import DictReader; [print(row['Name']) for row in DictReader(open('data.csv'))]"`
**Explanation:** Reads CSV file using dictionary-style access by column headers.

### DictWriter usage
**Args:** `python -c "from backports.csv import DictWriter; w = DictWriter(open('output.csv', 'w'), fieldnames=['Name', 'Value']); w.writeheader(); w.writerow({'Name': 'Sample1', 'Value': '200'})"`
**Explanation:** Writes CSV file with header using dictionary-style data.

### Custom dialect
**Args:** `python -c "import backports.csv; backports.csv.register_dialect('mydialect', delimiter='|', quotechar='\"'); [print(row) for row in backports.csv.reader(open('data.txt'), dialect='mydialect')]"`
**Explanation:** Uses custom dialect for non-standard CSV formats.

### Unicode handling
**Args:** `python -c "from backports.csv import reader; [print(row) for row in reader(open('unicode_data.csv', encoding='utf-8'))]"`
**Explanation:** Properly handles Unicode characters in CSV files.

### CSV with different delimiter
**Args:** `python -c "from backports.csv import reader; [print(row) for row in reader(open('tab_separated.txt'), delimiter='\t')]"`
**Explanation:** Reads tab-separated values file using custom delimiter.