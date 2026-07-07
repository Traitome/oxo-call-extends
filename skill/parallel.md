---
name: parallel
category: hpc
description: GNU Parallel executes shell jobs in parallel across multiple computers.
tags: [parallel, hpc, gnu-parallel, job-scheduling]
author: oxo-call-community
source_url: "http://www.gnu.org/software/parallel/"
---

## Concepts

- **Tool Overview**: GNU Parallel parallelizes shell command execution.
- **Core Function**: Runs commands in parallel on single or multiple machines.
- **Algorithm**: Distributes jobs across available CPUs/nodes.
- **Input Format**: Accepts commands from file or stdin.
- **Output**: Produces combined output from parallel jobs.
- **Use Case**: Batch processing, parallel task execution.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Resource Contention**: Too many parallel jobs may affect performance.
- **Output Order**: Output may be interleaved from parallel jobs.
- **Error Handling**: Failed jobs need manual inspection.
- **SSH Requirements**: Remote execution needs SSH setup.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parallel --help`
**Explanation:** Shows available options and usage instructions.

### Parallel echo
**Args:** `parallel echo ::: A B C`
**Explanation:** Runs echo for each argument.

### Process files in parallel
**Args:** `parallel gzip ::: *.txt`
**Explanation:** Compresses all txt files in parallel.

### With command file
**Args:** `parallel -a commands.txt`
**Explanation:** Executes commands from file.

### Number of jobs
**Args:** `parallel -j 8 gzip ::: *.txt`
**Explanation:** Runs 8 parallel jobs.

### Remote execution
**Args:** `parallel --sshlogin server1,server2 echo ::: A B`
**Explanation:** Runs on multiple servers.

### Progress bar
**Args:** `parallel --bar gzip ::: *.txt`
**Explanation:** Shows progress bar during execution.