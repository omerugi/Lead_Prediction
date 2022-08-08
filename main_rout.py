import uvicorn
from fastapi import FastAPI, Response, status

from database.db_setup import engine, get_db
from database import db_models
from ipynb.fs.full.LeadPrediction import *
import pandas as pd

app = FastAPI()
db_models.Base.metadata.create_all(engine)


@app.post("/predict_new_df_sample")
def predict_new_df_sample(df_in: str):
    try:
        df = pd.DataFrame.read_json(df_in)

    except Exception as e:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)


def run():
    uvicorn.run(app)


if __name__ == "__main__":
    run(app)
    n = get_data()
    n = step_1_pipline(n)
    n = step_2_pipline(n)
    n = step_3_pipline(n)
