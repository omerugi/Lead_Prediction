import uvicorn
from fastapi import FastAPI, Request, Response, status, Depends
from sqlalchemy.orm import Session

from database.db_setup import engine, get_db
from database import db_models
from ipynb.fs.full.LeadPrediction import *
from repos.lead_repo import lead_repo
import pandas as pd

app = FastAPI()
db_models.Base.metadata.create_all(engine)


@app.post("/predict")
async def predict_new_df_sample(request: Request, db: Session = Depends(get_db)):
    '''
    Post method to predict if the samples will converge + save results to the DB
    :param request:
    :param db:
    :return:
    '''
    try:
        js = await request.json()
        df = pd.DataFrame(js)
        lead = lead_repo(df)
        lead.preprocess_data().predict_and_save(db)
        return {"The prob of converting by ID: ": lead.predictions_dict()}
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_400_BAD_REQUEST)


def run():
    uvicorn.run(app)


if __name__ == "__main__":
    run()
    # n = get_data().head(2).drop("Converted", axis = 1)
    # print(n.to_json())
    # n = step_1_pipline(n)
    # n = step_2_pipline(n)
    # n = step_3_pipline(n)
    # print(will_convert_prod_lr_model(n))
