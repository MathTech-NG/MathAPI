def create_account(email: str, _password: str) -> dict:
    return {"message": f"Account created for {email}"}


def login_account(email: str, _password: str) -> dict:
    return {"message": f"Authenticated {email}"}
