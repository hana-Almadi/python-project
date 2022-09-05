from typing import Dict, List

from pydantic import BaseModel


class SeedData(BaseModel):
    users: List[Dict] = [
        {"first_name": "hana", "username": "hana123", "password": "a123"},
        {"first_name": "saad", "username": "saad1", "password": "b123"}
    ]
    users_tokens: List[str] = []
