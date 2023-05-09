from pydantic import BaseModel, Field


class InputData(BaseModel):
    degree: int = Field(ge=1)
    polynomial: str
    polynomial_gf2: str