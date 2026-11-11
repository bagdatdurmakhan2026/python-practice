variable "environment" {
  type    = string
  default = "development"
}

locals {
  app_name = "learning-api"
}

output "deployment_name" {
  value = "${local.app_name}-${var.environment}"
}
