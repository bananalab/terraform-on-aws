# Import resources

When adopting Terraform resources often already exist.  To import resources you can use the command `terraform import` however the terraform code that defines the infrastructure must already exist.

Challenge:
  Create an RDS database cluster using the AWS console.  Can you import it into Terraform?

Explore:
  Importing infrastructure is very tedious.  Tolls exists to assist with the process. See if you can import your infrastructure with [Terraformer](https://github.com/GoogleCloudPlatform/terraformer).
