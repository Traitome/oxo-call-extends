---
name: parafly
category: hpc
description: ParaFly executes multiple commands in parallel on a single server.
tags: [parafly, hpc, parallel, job-scheduling]
author: oxo-call-community
source_url: "http://parafly.sourceforge.net/"
---

## Concepts

- **Tool Overview**: ParaFly parallelizes command execution on single server.
- **Core Function**: Runs multiple commands concurrently using multithreading.
- **Algorithm**: Uses thread pool for parallel execution.
- **Input Format**: Accepts text file with list of commands.
- **Output**: Produces success/failure reports for each command.
- **Use Case**: Parallel task execution, batch processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Resource Contention**: Too many parallel jobs may affect performance.
- **Error Handling**: Failed commands need manual inspection.
- **Dependency Issues**: Commands must be available in PATH.
- **Output Management**: Output from parallel jobs may interleave.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ParaFly --help`
**Explanation:** Shows available options and usage instructions.

### Run commands in parallel
**Args:** `ParaFly -c commands.txt -CPU 8 -outfile results.txt`
**Explanation:** Runs commands with 8 parallel threads.

### With error file
**Args:** `ParaFly -c commands.txt -CPU 4 -outfile results.txt -failed_cmds failed.txt`
**Explanation:** Saves failed commands to separate file.

### Resume mode
**Args:** `ParaFly -c commands.txt -CPU 8 -resume`
**Explanation:** Resumes from previous execution.

### Verbose mode
**Args:** `ParaFly -v -c commands.txt -CPU 8`
**Explanation:** Runs with verbose output.

### Completion report
**Args:** `ParaFly -c commands.txt -CPU 8 -print_completed`
**Explanation:** Prints completed commands.

### Timeout per job
**Args:** `ParaFly -c commands.txt -CPU 8 -timeout 300`
**Explanation:** Sets 5-minute timeout per command.