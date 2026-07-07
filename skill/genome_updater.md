---
name: genome_updater
category: data-management
description: genome_updater - Bash script to download/update snapshots of RefSeq/GenBank.
tags: [genome_updater, data-download, refseq, genbank]
author: oxo-call-community
source_url: "https://github.com/pirovc/genome_updater"
---

## Concepts
- **RefSeq Download**: Downloads RefSeq genome data.
- **GenBank Download**: Downloads GenBank genome data.
- **Data Synchronization**: Synchronizes local data with NCBI.
- **Batch Download**: Downloads multiple genomes.
- **Data Management**: Manages genomic data locally.

## Pitfalls
- **Network Dependency**: Requires stable network connection.
- **Storage Requirements**: Large datasets require significant storage.
- **Download Time**: May take time for large downloads.
- **Data Integrity**: Requires verification after download.
- **NCBI Rate Limits**: May hit NCBI rate limits.

## Examples
### Download RefSeq bacteria
**Args:** `genome_updater.sh -d "refseq" -g "bacteria" -o ./refseq_bacteria/`
**Explanation:** Downloads RefSeq bacterial genomes.

### Update existing data
**Args:** `genome_updater.sh -d "refseq" -g "bacteria" -o ./refseq_bacteria/ -u`
**Explanation:** Updates existing RefSeq data.

### Download GenBank
**Args:** `genome_updater.sh -d "genbank" -g "fungi" -o ./genbank_fungi/`
**Explanation:** Downloads GenBank fungal genomes.

### Custom filters
**Args:** `genome_updater.sh -d "refseq" -g "archaea" -f "complete" -o ./archaea/`
**Explanation:** Downloads complete archaeal genomes.

### Batch download
**Args:** `genome_updater.sh -d "refseq" -g "viral" -o ./viruses/`
**Explanation:** Downloads viral genomes from RefSeq.