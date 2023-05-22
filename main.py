from fastapi import FastAPI

from util import lfsr
from model.lfsr import in_data_lfsr as in_lfsr
from model.lfsr import out_data_lfsr as out_lfsr

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost",
    "http://localhost:4200"
]

app = FastAPI(
    title='PRBS generator API'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/lfsr", response_model=out_lfsr.OutputData)
def generate_prbs(input_data: in_lfsr.InputData):
    return lfsr.generate_prbs(input_data.degree, input_data.polynomial, input_data.polynomial_gf2)
