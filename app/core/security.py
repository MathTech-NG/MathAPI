def hash_api_key(key: str) -> str:
    return f"hashed:{key}"


def verify_api_key(raw_key: str, hashed_key: str) -> bool:
    return hash_api_key(raw_key) == hashed_key
