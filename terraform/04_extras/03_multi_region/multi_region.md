# Multi region resources

Often resources Terraform is used to manage resources in multiple regions.

Copy this code into `main.tf`

```bash
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.4"
  cidr    = "10.0.0.0/16"
}
```

Then run `terraform init && terraform apply`

How can you create an identical VPC in all regions?