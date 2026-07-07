---
name: pronto
category: programming
description: pronto is a Python library for working with ontologies.
tags: [pronto, programming, ontology, python]
author: oxo-call-community
source_url: "https://pronto.readthedocs.io/en/stable"
---

## Concepts

- **Tool Overview**: pronto interacts with ontologies.
- **Core Function**: Ontology parsing and querying.
- **Algorithm**: Uses OBO/OWL parsing methods.
- **Input Format**: Accepts OBO/OWL files.
- **Output**: Produces ontology objects.
- **Use Case**: Bioinformatics data integration.

## Pitfalls

- **Version Differences**: API may change between versions.
- **Memory Usage**: Large ontologies require memory.
- **Ontology Quality**: Results depend on input quality.
- **Parsing Errors**: May fail on malformed files.
- **Runtime**: Loading may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -m pronto --help`
**Explanation:** Shows available options and usage instructions.

### Load ontology
**Args:** `python -c "from pronto import Ontology; o = Ontology('go.obo')"`
**Explanation:** Loads an ontology file.

### With parameters
**Args:** `python -c "from pronto import Ontology; o = Ontology('go.obo', timeout=300)"`
**Explanation:** Uses custom parameters.

### Query terms
**Args:** `python -c "from pronto import Ontology; o = Ontology('go.obo'); print(o['GO:0005886'])"`
**Explanation:** Queries ontology terms.

### Save ontology
**Args:** `python -c "from pronto import Ontology; o = Ontology('go.obo'); o.dump('output.obo')"`
**Explanation:** Saves ontology to file.

### List terms
**Args:** `python -c "from pronto import Ontology; o = Ontology('go.obo'); [print(t) for t in o.terms()]"`
**Explanation:** Lists all ontology terms.

### Search terms
**Args:** `python -c "from pronto import Ontology; o = Ontology('go.obo'); [print(t) for t in o.search('apoptosis')]"`
**Explanation:** Searches for ontology terms.