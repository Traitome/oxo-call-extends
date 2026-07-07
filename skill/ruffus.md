---
name: ruffus
category: workflow_management
description: Light-weight Python Computational Pipeline Management
tags: ["ruffus", "python", "pipeline", "workflow", "bioinformatics"]
author: oxo-call-community
source_url: "http://www.ruffus.org.uk/"
---

## Concepts

- **Tool Overview**: ruffus (v2.8.4) is a lightweight Python library for managing computational pipelines. It provides a simple decorator-based approach to define tasks and their dependencies.
- **Core Function**: Orchestrates multi-step computational workflows with automatic dependency tracking, parallel execution, and incremental updates.
- **Design Pattern**: Uses Python decorators to mark functions as pipeline tasks, with built-in support for file-based dependencies and task parallelization.
- **Features**: Automatic re-run of modified tasks, job parallelization, logging, and progress tracking.
- **Integration**: Works seamlessly with Python bioinformatics libraries like Biopython, pandas, and numpy.
- **Use Case**: Building bioinformatics analysis pipelines, managing multi-step data processing workflows, automating repetitive computational tasks.

## Pitfalls

- **Python dependency**: Requires Python; not suitable for non-Python workflows.
- **Learning curve**: Requires understanding of decorators and pipeline concepts.
- **Error handling**: Debugging pipeline failures can be challenging.
- **Scalability**: May struggle with very large workflows or distributed computing.
- **Documentation**: Some advanced features have limited documentation.
- **Version compatibility**: API changes between versions may break existing pipelines.

## Examples

### Define a simple pipeline
**Args:** `python my_pipeline.py`
**Explanation:** Runs a Python script containing a ruffus pipeline definition.

### Pipeline decorator
**Args:** `@transform(input_files, suffix('.fastq'), '.fastqc.html', fastqc)`
**Explanation:** Applies fastqc to all .fastq files, producing .fastqc.html outputs.

### Parallel execution
**Args:** `pipeline_run(verbose=3, multiprocess=4)`
**Explanation:** Runs pipeline with 4 parallel processes.

### Print pipeline flowchart
**Args:** `pipeline_printout_graph('pipeline.png', 'png')`
**Explanation:** Generates a visual flowchart of the pipeline.

### Specify task dependencies
**Args:** `@follows(previous_task)`
**Explanation:** Marks task as dependent on previous_task completing first.

### Parameterized tasks
**Args:** `@jobs_limit(10)`
**Explanation:** Limits concurrent execution of a task to 10 jobs.

### Pipeline status
**Args:** `pipeline_run(verbose=2)`
**Explanation:** Runs pipeline with detailed progress reporting.
