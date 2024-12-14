terraform {
  backend "s3" {
    bucket = "terraformstatebucketparasupes"
    key    = "terraform/terraform.tfstate"
    region = "us-east-1"
  }
}
