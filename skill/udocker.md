---
name: udocker
category: container
description: udocker - A user-friendly tool to run docker containers without root privileges.
tags: [udocker, docker, container, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/indigo-dc/udocker"
---

## Concepts

- **Tool Overview**: udocker - A tool to run docker containers without requiring root privileges.
- **Core Function**: Enables container execution for non-privileged users.
- **Input**: Docker image or container specification.
- **Output**: Container execution environment.
- **Installation**: Install via pip or source
- **Use Case**: Containerization, reproducible research, bioinformatics.

## Pitfalls

- **Performance**: May have performance overhead compared to native docker.
- **Network**: Container networking may be limited.

## Examples

### Run container
**Args:** `udocker run ubuntu:latest echo "Hello"`
**Explanation:** Run a simple command in container.

### Pull and run
**Args:** `udocker pull ubuntu:latest && udocker run ubuntu:latest`
**Explanation:** Pull image and run container.
