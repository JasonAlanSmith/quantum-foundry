import os


def get_user_from_env(username_env: str | None):
    une = f"Could not read username from environment {username_env}."
    if username_env is not None:
        username = os.environ.get(username_env)
        if not username:
            raise ValueError(une)
        else:
            return username
    else:
        raise ValueError("username_env=None")


def get_password_from_env(password_env: str | None):
    pe = f"Could not read password from environment {password_env}."
    if password_env is not None:
        password = os.environ.get(password_env)
        if not password:
            raise ValueError(pe)
        else:
            return password
    else:
        raise ValueError("password_env=None")
