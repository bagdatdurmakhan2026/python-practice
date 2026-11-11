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
