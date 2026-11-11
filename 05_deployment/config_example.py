import os

environment = os.getenv("APP_ENV", "development")
allowed_environments = {"development", "staging", "production"}

if environment not in allowed_environments:
    raise ValueError(f"Неизвестная среда: {environment}")


if __name__ == "__main__":
    print({"environment": environment})
