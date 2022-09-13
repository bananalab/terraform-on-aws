# The Cloud Development Kit for Terraform
CDKTF is a variant of the CDK that uses Terraform as it's execution engine rather than CloudFormation.

Install
```bash
brew install cdktf
```

Create a project
```bash
mkdir cdktf-lab && cd cdktf-lab
cdktf init
```

Add the AWS provider
```bash
cdktf provider add "aws@~>4.0"
```

Edit cdktf.json
```json
{
  ...
  "terraformProviders": [
    "aws@~> 3.0"
  ],
  "terraformModules": [
    "terraform-aws-modules/vpc/aws@2.77.0"
  ],
  ...
}
```

Run `cdktf get` to download required modules and providers.