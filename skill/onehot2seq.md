---
name: onehot2seq
category: utility
description: onehot2seq decodes one-hot encoded numpy arrays back to biological sequences.
tags: [onehot2seq, utility, one-hot-encoding, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/akikuno/onehot2seq"
---

## Concepts

- **Tool Overview**: onehot2seq converts one-hot encoded arrays to biological sequences.
- **Core Function**: Decodes one-hot encoded numpy arrays.
- **Algorithm**: Uses argmax and mapping for sequence reconstruction.
- **Input Format**: Accepts numpy arrays with one-hot encoded sequences.
- **Output**: Produces FASTA sequences or sequence strings.
- **Use Case**: Machine learning output decoding, sequence analysis, and bioinformatics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Encoding Scheme**: Requires matching encoding scheme.
- **Input Shape**: Requires correct array shape.
- **Ambiguity**: May have issues with ambiguous bases.
- **Memory Usage**: Large arrays require memory.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `onehot2seq --help`
**Explanation:** Shows available options and usage instructions.

### Decode array
**Args:** `onehot2seq decode -i encoded.npy -o sequences.fasta`
**Explanation:** Decodes one-hot encoded array to FASTA.

### From stdin
**Args:** `python -c "import numpy as np; arr = np.load('encoded.npy'); print(onehot2seq.decode(arr))"`
**Explanation:** Decodes array in Python.

### Output format
**Args:** `onehot2seq decode -i encoded.npy -o sequences.txt --txt`
**Explanation:** Outputs sequences in text format.

### Verbose mode
**Args:** `onehot2seq decode -i encoded.npy -v -o sequences.fasta`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `onehot2seq batch -d encoded/ -o sequences/`
**Explanation:** Processes multiple encoded files.

### Custom alphabet
**Args:** `onehot2seq decode -i encoded.npy -a ACGTN -o sequences.fasta`
**Explanation:** Uses custom alphabet for decoding.