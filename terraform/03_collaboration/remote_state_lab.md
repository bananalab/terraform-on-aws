# Backend for state

In this exercise, you will create a remote backend for Terraform state of your project. This will allow:

* cooperation with the team
* safe location for Terraform state
* locking the state for Terraform apply operation

## Project pre-state: Create resources for state

1. Create the directory for the project that will create resources necessary for the main project's state:

    ```bash
    mkdir pre-state && cd pre-state
    ```

1. Create files for the project:

    * `main.tf`
    * `outputs.tf`
    * `variables.tf`
    * `providers.tf`

1. In the `main.tf` file, create an S3 bucket:

    ```bash
    resource "aws_s3_bucket" "bucket" {
        bucket = "${var.project}-terraform-state-bucket"
        versioning {
            enabled = true
        }
        server_side_encryption_configuration {
            rule {
                apply_server_side_encryption_by_default {
                    sse_algorithm = "AES256"
                }
            }
        }
        object_lock_configuration {
            object_lock_enabled = "Enabled"
        }
        tags = {
            Name = "S3 Remote Terraform State Store"
        }
    }
    ```

1. In the `main.tf` file, create a DynamoDB table:

    ```bash
    resource "aws_dynamodb_table" "terraform_lock" {
        name           = "${var.project}-terraform-lock-table"
        read_capacity  = 5
        write_capacity = 5
        hash_key       = "LockID"
        attribute {
            name = "LockID"
            type = "S"
        }
        tags = {
            "Name" = "State Lock Table for ${var.project}"
        }
    }

1. Declare variables "project", "aws_region" and "aws_profile" in `variables.tf` file.
1. Configure the AWS provider in `providers.tf` file.
1. Set up outputs:

    ```bash
    output "state_backend" {
        value = {
            "bucket"  = aws_s3_bucket.bucket.id
            "table"   = aws_dynamodb_table.terraform_lock.id
            "region"  = var.aws_region
            "profile" = var.aws_profile
        }
    }
    ```

1. Create a `project.auto.tfvars` file and define variables` values.
1. Write down the code for the **backend** of the project:

    ```
    terraform {
      backend "s3" {
        bucket         = <state_backend.bucket>
        key            = "terraform.tfstate"
        region         = <state_backend.region>
        dynamodb_table = <state_backend.table>
        profile        = <state_backend.profile>
      }
    }
    ```

    NOTE: This is something you will copy in the project below.

## Project main: Create resources shared in backend

1. Create the directory for the main project:

    ```bash
    mkdir main && cd main
    ```

1. Create files for the project:

    * `main.tf`
    * `outputs.tf`
    * `variables.tf`
    * `providers.tf`

1. In the `providers.tf` file, set up the AWS provider as usual.

1. In the `providers.tf` file also **paste the *backend* code - result from pre-state-project**.

1. In the `main.tf` file, create a resource:

    ```tf
    resource "aws_iam_policy" "policy" {
      name        = "terraformed_test_policy_my_username"
      path        = "/"
      description = "Terraformed test policy"

      policy = <<EOF
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": [
            "ec2:Describe*"
          ],
          "Effect": "Allow",
          "Resource": "*"
        }
      ]
    }
    EOF
    }
    ```

1. Apply the code to create a resource in AWS. Notice that the `terraform.tfstate` is no longer in the local directory.
1. Visit AWS console and:
    1. View the policy in IAM.
    1. Go to S3 and see the `terraform.tfstate` object.


## Challenge

1. Create `development` and `production` workspaces.
1. Modify the policy code so that the workspace name is the part of policy name.
1. Apply both workspaces.
1. Analyze the contents of the S3 state bucket. How are workspaces organized?