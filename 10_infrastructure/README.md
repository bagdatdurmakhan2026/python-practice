# Infrastructure

This section introduces Infrastructure as Code through a safe Terraform example.

## Topics

- Declare input variables
- Derive configuration with local values
- Expose values as outputs

## Example: deployment name

[`main.example.tf`](main.example.tf) combines an application name with an environment name and outputs the result. It declares no cloud resources.

If Terraform is installed, inspect the configuration from the repository root:

```powershell
terraform -chdir=10_infrastructure plan -input=false
```

The plan contains no infrastructure changes because this example defines no resources.

## Intermediate example: validated deployment contract

[`environment_contract.example.tf`](environment_contract.example.tf) uses a typed object variable, input validations, and shared tags to produce a deployment configuration. It intentionally declares no cloud resources.

Terraform ignores files ending in `.example.tf`. To use the example, copy it into a separate temporary directory as a `.tf` file, provide a `terraform.tfvars` value for `service`, and run `terraform plan`. The plan describes values only and provisions nothing.
