def normalize_username(value: str) -> str:
    username = value.strip().lower()
    if len(username) < 3:
        raise ValueError("Имя должно содержать хотя бы 3 символа")
    return username


if __name__ == "__main__":
    print(normalize_username("  Alex  "))
