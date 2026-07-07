---
name: awscli
category: utility
description: AWS Command Line Interface - Unified tool to manage AWS services
tags: [awscli, cloud, s3, aws, storage]
author: oxo-call-community
source_url: "https://aws.amazon.com/cli/"
---

## Concepts

- **Tool Overview**: AWS Command Line Interface (AWS CLI) is a unified tool to manage Amazon Web Services resources from the command line. Version 1.8.3.
- **Core Function**: Provides command-line access to AWS services including S3, EC2, IAM, Lambda, and more.
- **Unified Interface**: Single tool for managing multiple AWS services with consistent syntax.
- **Configuration**: Supports credential management via ~/.aws/credentials and ~/.aws/config files.
- **S3 Integration**: Enables file transfer to/from Amazon S3 storage.
- **EC2 Management**: Allows launching, managing, and terminating EC2 instances.
- **IAM Administration**: Manages users, roles, and permissions in AWS Identity and Access Management.
- **Installation**: `conda install -c bioconda awscli` or `pip install awscli`.

## Pitfalls

- **Credentials Management**: Improper credential handling can lead to security breaches. Use IAM roles when possible.
- **Region Configuration**: Must specify correct AWS region for resources to be created in the right location.
- **Rate Limiting**: AWS API calls have rate limits. Exceeding limits causes throttling.
- **Cost Awareness**: Some AWS services incur costs. Monitor usage to avoid unexpected charges.
- **Version Compatibility**: AWS CLI v1 and v2 have different syntax. Check version before use.
- **Network Access**: Requires internet connection and proper network configuration for AWS access.

## Examples

### Configure AWS credentials
**Args:** `aws configure`
**Explanation:** Interactive setup for AWS Access Key ID, Secret Access Key, default region, and output format.

### List S3 buckets
**Args:** `aws s3 ls`
**Explanation:** Lists all S3 buckets in the configured AWS account.

### Copy file to S3
**Args:** `aws s3 cp local_file.txt s3://my-bucket/path/to/destination/`
**Explanation:** Uploads local file to specified S3 bucket and path.

### Sync directory to S3
**Args:** `aws s3 sync ./local_dir/ s3://my-bucket/destination/ --delete`
**Explanation:** Syncs local directory to S3, deleting files in bucket that don't exist locally.

### Download file from S3
**Args:** `aws s3 cp s3://my-bucket/path/to/file.txt ./local_directory/`
**Explanation:** Downloads file from S3 to local directory.

### List EC2 instances
**Args:** `aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"`
**Explanation:** Lists all running EC2 instances in the current region.

### Create S3 bucket
**Args:** `aws s3 mb s3://my-unique-bucket-name --region us-east-1`
**Explanation:** Creates new S3 bucket in specified region.

### Delete S3 object
**Args:** `aws s3 rm s3://my-bucket/path/to/file.txt`
**Explanation:** Deletes specified object from S3 bucket.

### Get S3 object metadata
**Args:** `aws s3api head-object --bucket my-bucket --key path/to/file.txt`
**Explanation:** Retrieves metadata for S3 object without downloading it.

### Upload with encryption
**Args:** `aws s3 cp local_file.txt s3://my-bucket/ --server-side-encryption AES256`
**Explanation:** Uploads file with server-side encryption enabled.

### List IAM users
**Args:** `aws iam list-users`
**Explanation:** Lists all IAM users in the AWS account.

### Run Lambda function
**Args:** `aws lambda invoke --function-name my-function --payload '{"key": "value"}' output.json`
**Explanation:** Invokes Lambda function with specified payload and saves output.

### Check AWS CLI version
**Args:** `aws --version`
**Explanation:** Displays current AWS CLI version and Python version.