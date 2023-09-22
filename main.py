from fastapi import FastAPI

from util import lfsr
from util import msr
from model.lfsr import in_data_lfsr as in_lfsr
from model.lfsr import out_data_lfsr as out_lfsr
from model.msr import in_data_msr as in_msr
from model.msr import out_data_msr as out_msr

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:4200",
    "https://prbs-generator.netlify.app",
    "https://oleksii-drabchak-prbs.azurewebsites.net"
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
def generate_prbs_lfsr(input_data: in_lfsr.InputData):
    return lfsr.generate_prbs(input_data.degree, input_data.polynomial, input_data.polynomial_gf2)


@app.post("/msr", response_model=out_msr.OutputData)
def generate_prbs_msr(input_data: in_msr.InputData):
    return msr.generate_prbs(input_data.rankA, input_data.rankB,
                             input_data.polynomialA, input_data.polynomialB,
                             input_data.rankS, input_data.i, input_data.j)
