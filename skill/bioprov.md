---
name: bioprov
category: workflow
description: BioProv - Provenance capture for bioinformatics workflows
tags: [provenance, workflow, reproducibility, tracking]
author: oxo-call-community
source_url: "https://bioprov.readthedocs.io/"
---

## Concepts

- **Tool Overview**: BioProv is a Python library for capturing provenance information from bioinformatics workflows, enabling reproducibility and tracking of computational experiments.
- **Provenance Tracking**: Automatically records inputs, outputs, parameters, and execution details for each step in a workflow.
- **Workflow Integration**: Works with common workflow engines and script-based pipelines.
- **Reproducibility**: Enables exact reproduction of bioinformatics analyses by capturing complete provenance.
- **Output Formats**: Generates provenance reports in multiple formats including JSON and HTML.

## Pitfalls

- **Performance Overhead**: Provenance capture adds some overhead to workflow execution.
- **Storage Requirements**: Detailed provenance data can be substantial.

## Examples

### Initialize provenance tracker
**Args:** `from bioprov import Prov; p = Prov("my_workflow")`
**Explanation:** Creates a new provenance tracker for a workflow.

### Track command execution
**Args:** `p.run("bwa mem ref.fasta reads.fq > aligned.sam")`
**Explanation:** Executes a command and captures its provenance.

### Export provenance report
**Args:** `p.export("provenance_report.json")`
**Explanation:** Exports provenance information to JSON file.

### Generate HTML report
**Args:** `p.html_report("provenance_report.html")`
**Explanation:** Generates an HTML visualization of provenance data.