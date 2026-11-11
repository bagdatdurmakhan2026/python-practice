variable "service" {
  description = "Application deployment settings"
  type = object({
    name        = string
    environment = string
    region      = string
    replicas    = number
  })

  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{2,30}$", var.service.name))
    error_message = "The service name must be 3-31 lowercase letters, digits, or hyphens and start with a letter."
  }

  validation {
    condition     = contains(["development", "staging", "production"], var.service.environment)
    error_message = "Environment must be development, staging, or production."
  }

  validation {
    condition     = var.service.replicas >= 1 && var.service.replicas <= 10 && var.service.replicas == floor(var.service.replicas)
    error_message = "Replicas must be an integer between 1 and 10."
  }

  validation {
    condition     = length(trimspace(var.service.region)) > 0
    error_message = "Region must not be empty."
  }
}

locals {
  common_tags = {
    application = var.service.name
    environment = var.service.environment
    managed_by  = "terraform"
  }

  deployment_contract = {
    name     = "${var.service.name}-${var.service.environment}"
    region   = var.service.region
    replicas = var.service.replicas
    tags     = local.common_tags
  }
}

output "deployment_contract" {
  description = "Validated deployment settings; no cloud resources are created."
  value       = local.deployment_contract
}
