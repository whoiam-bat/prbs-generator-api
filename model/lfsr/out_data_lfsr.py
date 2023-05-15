from pydantic import BaseModel
from typing import List


class OutputData(BaseModel):
    prbs: str
    rang_formula: int
    rang_experimental: int
    polynomial_type: str
    hamming_weight: int = 0
    register_states: List[str]
    accompanying_matrix: List[str] = []
    prbs_indexes: List[int] = []
    acf: List[float] = []
