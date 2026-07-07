---
name: firecloud
category: programming
description: "Firecloud (FISS - FireCloud API in Python) provides a Python API and CLI for managing Broad Institute's Firecloud/Terra workspaces, uploading data, and executing WDL workflows on Google Cloud Platform."
tags: [firecloud, programming, api, cli, workflow, genomics, cloud, terra, broad-institute, google-cloud, wdl]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/fiss"
---

## Concepts
- **Tool Overview**: Firecloud (also known as FISS - FireCloud API in Python) is a Python library and command-line interface for interacting with Broad Institute's Firecloud (now part of Terra) cloud platform. It enables workspace management, data transfer, and workflow execution for genomic analyses.
- **Core Function**: Provides programmatic access to FireCloud REST API for managing workspaces, uploading/downloading data to Google Cloud Storage, configuring method inputs, and submitting/monitoring WDL workflow executions.
- **Command Structure**: The primary CLI command is `fiss` (not `firecloud`). Commands follow the pattern `fiss <resource> <action>` such as `fiss ws list` or `fiss method list`.
- **Workspace Management**: Workspaces organize cloud resources including Google Cloud Storage buckets, compute instances, and workflow data. Each workspace is associated with a billing project and has access control lists (ACLs).
- **Method Registry**: Firecloud uses WDL (Workflow Description Language) for defining analytical workflows. Methods are registered in workspace-specific method repositories with version control.
- **Data Transfer**: Supports uploading local files to workspace Google Cloud Storage buckets and downloading results. Handles large genomic files (BAM, VCF) with multipart upload support for reliability.
- **Installation**: `pip install firecloud` or `conda install -c bioconda firecloud`. Requires Python 2.7+/3.x, Google Cloud SDK, and authentication via `gcloud auth login`.

## Pitfalls
- **Authentication Requirements**: Firecloud requires Google Cloud authentication via `gcloud auth login`. The underlying Firecloud API uses OAuth2 tokens that expire periodically. Automated pipelines must handle token refresh.
- **Command Name Mismatch**: The CLI tool is `fiss`, not `firecloud`. Using `firecloud` as a command will fail. Always use `fiss <subcommand>` syntax.
- **Billing Project Permissions**: Users need proper permissions on both the billing project and target workspace to run workflows or upload data. Insufficient permissions result in API 403 errors.
- **Workspace Naming**: Workspace names must be unique within a billing project. Creating a workspace with an existing name returns an HTTP 409 Conflict error.
- **Large File Upload Timeouts**: Files larger than 10GB require segmented uploads or pre-signed URLs to avoid timeout. Use Google Cloud Storage native tools for very large file transfers.
- **WDL Input JSON Formatting**: WDL workflow inputs must be precisely formatted JSON. Incorrect types (string vs file path, array syntax) are the most common cause of workflow submission failures.

## Examples
### Authenticate with Google Cloud
**Args:** `gcloud auth login`
**Explanation:** Initiates Google Cloud authentication. Required before using Firecloud CLI or API. Opens browser for Google account login or accepts token-based authentication.

### List accessible workspaces
**Args:** `fiss ws list`
**Explanation:** Displays all workspaces accessible to the authenticated user. Shows workspace name, billing project, creation date, and owner information.

### Create a new workspace
**Args:** `fiss ws create --workspace my_project --billing-project my-billing-project`
**Explanation:** Creates a new workspace under the specified billing project. Initializes empty storage bucket and sets owner ACLs for the creator.

### Upload data to workspace
**Args:** `fiss fc upload --workspace my_project --bucket gs://my-bucket/data --file variants.vcf`
**Explanation:** Uploads a local VCF file to the workspace Google Cloud Storage bucket. Creates necessary directory structure if paths don't exist.

### List available WDL methods
**Args:** `fiss method list --workspace my_project`
**Explanation:** Shows all WDL workflows available in the workspace method registry. Includes method name, namespace, and version information.

### Get method input template
**Args:** `fiss method inputs --workspace my_project --method MyWorkflow --yaml > inputs.yaml`
**Explanation:** Generates a template YAML showing all required and optional inputs for a workflow method. Use this as a starting point for configuring workflow runs.

### Submit a workflow
**Args:** `fiss ws run_workflow --workspace my_project --method MyWorkflow --wdl inputs.json`
**Explanation:** Submits a WDL workflow for execution with specified input parameters. Returns a job ID for tracking. Monitor status with `fiss job status`.

### Check job status
**Args:** `fiss job status --job-id abc123`
**Explanation:** Returns current status of a submitted job including queued time, start time, completion time (if finished), and any error messages if failed.

### Download workflow outputs
**Args:** `fiss fc download --workspace my_project --pattern "*.vcf" --output-dir ./results`
**Explanation:** Downloads output files matching the pattern from workspace bucket to local directory. Supports wildcard patterns for batch downloading.

### Set workspace permissions
**Args:** `fiss ws acl --workspace my_project --user researcher@example.com --role WRITER`
**Explanation:** Modifies workspace access control list to grant a user read, write, or owner permissions. Essential for collaborative project management.

### Get workspace information
**Args:** `fiss ws describe --workspace my_project`
**Explanation:** Shows detailed information about a workspace including storage bucket URL, billing project, creation date, owners, and total storage used.
