from pydantic import BaseModel, Field


class InputData(BaseModel):
    rankA: int = Field(ge=1)
    rankB: int = Field(ge=1)
    polynomialA: str
    polynomialB: str
    polynomial_gf2A: str
    polynomial_gf2B: str

    rankS: int = Field(ge=1)
    i: int
    j: int