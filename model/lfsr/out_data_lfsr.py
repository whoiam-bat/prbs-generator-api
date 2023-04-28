from pydantic import BaseModel
from typing import List


class OutputData(BaseModel):
    degree: int
    polynomial: str
    seed: str
    prbs: str
    rang_formula: int
    rang_experimental: int
    polynomial_type: str
    hamming_weight: int = 0
    register_states: List[str]
    accompanying_matrix: List[str] = []

