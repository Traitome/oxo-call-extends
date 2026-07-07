---
name: mykatlas
category: annotation
description: MykAtlas - Assists in antibiotic-resistance discovery with Mykrobe
tags: [mykatlas, annotation, antibiotic-resistance, mykrobe, bacteria, tuberculosis]
author: oxo-call-community
source_url: "https://github.com/phelimb/atlas"
---

## Concepts

- **Tool Overview**: MykAtlas v0.6.1 is a companion database and utilities package for the Mykrobe antibiotic resistance prediction tool. It provides curated reference data for predicting antibiotic resistance in bacterial pathogens.
- **Core Function**: Supplies validated mutation catalogs and resistance gene databases that Mykrobe uses to predict antibiotic resistance from genomic data. Includes known resistance-associated mutations for supported species.
- **Database Content**: Contains curated catalogs of mutations known to confer resistance to various antibiotics, compiled from published research and clinical validation studies.
- **Species Support**: Primary focus on Mycobacterium tuberculosis complex, providing resistance prediction for first-line and second-line anti-tuberculosis drugs.
- **Output**: When used with Mykrobe, produces JSON-formatted resistance predictions including detected mutations and predicted phenotype (resistant/susceptible).
- **Use Case**: Tuberculosis diagnostics, drug resistance surveillance, clinical microbiology labs, and epidemiological studies of antibiotic resistance.

## Pitfalls

- **Mykrobe Dependency**: MykAtlas is designed to work with Mykrobe. Cannot be used standalone without Mykrobe installation.
- **Database Updates**: Resistance mutations are continuously discovered. Ensure using current database versions for accurate predictions.
- **Species Limitations**: Database is optimized for specific pathogens. Using with non-supported species may give unreliable results.
- **Interpretation Challenges**: Some mutations may have uncertain clinical significance. Expert interpretation may be needed for complex cases.
- **Version Matching**: Database version should match Mykrobe version. Mismatched versions may cause errors or incorrect predictions.
- **Complex Resistance**: Some forms of resistance involve multiple mutations or compensatory mechanisms not captured by single-mutation catalogs.

## Examples

### Update MykAtlas database
**Args:** `mykatlas update`
**Explanation:** Downloads and installs the latest resistance mutation catalog database.

### Check database version
**Args:** `mykatlas version`
**Explanation:** Displays current MykAtlas database version and publication information.

### Display help
**Args:** `mykatlas --help`
**Explanation:** Shows available commands and usage information for MykAtlas.

### List supported drugs
**Args:** `mykatlas list-drugs`
**Explanation:** Lists all antibiotics covered in the current resistance database.

### Verify database integrity
**Args:** `mykatlas check`
**Explanation:** Validates database integrity and reports any corruption or missing data.
