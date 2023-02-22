import os

db = {
    "lukasscholz": {
        "username": "lukasscholz",
        "full_name": "Lukas Scholz",
        "email": str(os.getenv("email")),
        "hashed_password": str(os.getenv("password_api")),
        "disabled": False,
    },
}

SECRET_KEY = str(os.getenv("SECRET_KEY"))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
