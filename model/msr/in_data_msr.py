from pydantic import BaseModel, Field


class InputData(BaseModel):
    rankA: int = Field(ge=1)
    rankB: int = Field(ge=1)
    polynomialA: str
    polynomialB: str

    rankS: int = Field(ge=1)
    i: int
    j: int