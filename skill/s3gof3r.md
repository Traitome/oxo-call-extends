---
name: s3gof3r
category: utility
description: Fast, concurrent, streaming access to Amazon S3.
tags: ["s3gof3r", "AWS", "S3", "cloud storage", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/rlmcpherson/s3gof3r"
---

## Concepts

- **Tool Overview**: s3gof3r (v0.5.0) is a high-performance command-line tool for interacting with Amazon S3 storage. It provides fast, concurrent, streaming access for uploading and downloading files.
- **Core Function**: Enables efficient transfer of large bioinformatics files to/from Amazon S3, supporting parallel transfers and streaming operations.
- **Algorithm**: Uses concurrent goroutines for parallel file transfers, supports multipart uploads for large files, and implements streaming for efficient memory usage.
- **Input Format**: Local files or standard input for upload; S3 object paths for download.
- **Output Format**: Downloaded files to local filesystem or streamed output.
- **Use Case**: Transferring sequencing data to/from cloud storage, backup of large bioinformatics datasets, distributed computing workflows.

## Pitfalls

- **AWS credentials**: Requires proper AWS credential configuration.
- **Network dependency**: Performance depends on network bandwidth and latency.
- **Region configuration**: Must specify correct AWS region for S3 buckets.
- **Large file handling**: Very large files require multipart upload configuration.
- **Cost considerations**: Data transfer and storage costs may apply.
- **Error handling**: Network interruptions may require restarting transfers.

## Examples

### Upload file to S3
**Args:** `gof3r put -b my-bucket -k path/to/s3/object -f local_file.fastq`
**Explanation:** `-b` bucket name; `-k` S3 key/path; `-f` local file to upload.

### Download file from S3
**Args:** `gof3r get -b my-bucket -k path/to/s3/object -f local_file.fastq`
**Explanation:** `-b` bucket name; `-k` S3 key/path; `-f` local destination file.

### Stream to S3
**Args:** `cat input.fastq | gof3r put -b my-bucket -k path/to/s3/object -s`
**Explanation:** `-s` stream mode for uploading from stdin.

### Stream from S3
**Args:** `gof3r get -b my-bucket -k path/to/s3/object -s | gunzip > output.fastq`
**Explanation:** `-s` stream mode for downloading to stdout.

### List bucket contents
**Args:** `gof3r ls -b my-bucket`
**Explanation:** Lists objects in the specified S3 bucket.

### Multipart upload
**Args:** `gof3r put -b my-bucket -k path/to/s3/object -f large_file.bam --part-size 64MB`
**Explanation:** `--part-size` specifies multipart chunk size.

### Set AWS region
**Args:** `gof3r put -b my-bucket -k path/to/s3/object -f file.fastq --region us-east-1`
**Explanation:** `--region` specifies AWS region for the bucket.
