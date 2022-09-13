
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.4"
  cidr    = "10.0.0.0/16"
}
