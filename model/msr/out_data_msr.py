from pydantic import BaseModel
from typing import List


class OutputData(BaseModel):
    matrA: List[str]
    matrB: List[str]
    periodA: int
    periodB: int
    stateMatrixS: List[List[str]]
    analS: int
    experimentalS: int
    hammingWeightPractice: int
    hammingWeightTheoretical: int
    polynomialA: str
    polynomialB: str
    prbs: str
    prbsIndexes: List[int]
    acf: List[float]