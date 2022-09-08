
provider "null" {
  alias = "null_1"
}

provider "null" {
  alias = "null_2"
}

module "example_1" {
  providers = {
    null = null.null_1
  }
  source    = "../01_minimal"
  parameter = 1
}

module "example_2" {
  providers = {
    null = null.null_2
  }
  source    = "../01_minimal"
  parameter = 2
}
