---
name: grz-common
category: bioinformatics
description: grz-common provides common utilities and shared components for GRZ applications and tools.
tags: [grz-common, library, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BfArM-MVH/grz-tools"
---

## Concepts

- **Shared Library**: grz-common provides reusable components for GRZ applications.

- **Configuration Management**: Manages configuration settings for GRZ tools.

- **Logging**: Provides standardized logging functionality.

- **Error Handling**: Implements common error handling patterns.

- **File I/O**: Offers utility functions for file operations.

- **Validation**: Contains validation logic shared across applications.

## Pitfalls

- **Version Compatibility**: Ensure compatibility with other GRZ components.

- **Dependency Management**: Manage dependencies carefully in complex workflows.

- **Configuration Conflicts**: Be aware of configuration conflicts between tools.

- **API Changes**: Monitor for breaking changes in API.

- **Testing**: Thoroughly test integration with dependent applications.

## Examples

### Import common module
**Args:** `from grz_common import config, logging`
**Explanation:** Imports common utilities from grz-common.

### Load configuration
**Args:** `config.load('config.yaml')`
**Explanation:** Loads configuration settings from file.

### Initialize logger
**Args:** `logger = logging.get_logger('my_app')`
**Explanation:** Creates a logger with standardized settings.

### Validate file
**Args:** `from grz_common.validation import validate_file`
**Explanation:** Uses shared validation functions.

### Read JSON
**Args:** `data = grz_common.io.read_json('data.json')`
**Explanation:** Reads JSON file using common utilities.

### Write log message
**Args:** `logger.info('Processing completed successfully')`
**Explanation:** Logs an informational message.

### Handle errors
**Args:** `from grz_common.exceptions import GrzError`
**Explanation:** Uses standardized exception classes.