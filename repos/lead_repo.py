import pandas as pd
from sqlalchemy.orm import Session
from var import data_features, data_features_can_nan
from numpy import nan
from ipynb.fs.full.LeadPrediction import *
from database.db_models import Lead

'''
This class will do all the data processing and the predictions.
It will the connection both to the DB, the preprocessing, and to the model.
A data layer between the API and the functionality. 
'''


class lead_repo():

    def __init__(self, df):
        '''
        Will init the object with a df (as a json) from the user with valid columns,
        drop the "Converted" feature as it's not relevant and also empty,
        and keep a dict for the prdictions later + the id's of the leads (as they will be dropped).
        :param df: a df from the user
        '''
        dict_to_df = pd.DataFrame(columns=data_features)
        for feature in data_features:
            try:
                dict_to_df[feature] = df[feature]
            except Exception as e:
                if feature not in data_features_can_nan: raise e
        dict_to_df.drop("Converted", axis=1)
        self.df = df
        self.pred = {}
        self.did_preproc = False
        self.lead_id = self.df["Lead Number"]

    def preprocess_data(self):
        '''
        Will preprocess the data the object stores according to the pipeline steps.
        But, if the data is already been preprocessed it won't do it again.
        '''
        if not self.did_preproc:
            df = step_1_pipline(self.df)
            # d = step_1_pipline(get_data().head(1))
            # print(df.columns)
            # print(d.columns)
            # for f in df.columns:
            #     try:
            #         if not d[f].equals(df[f]):
            #             print(f,": ")
            #             print(d[f].value_counts(dropna=False))
            #             print(df[f].value_counts(dropna=False))
            #             print("*********")
            #     except Exception as e:
            #         print(e)
            #         print(f)
            #         print(d[f])
            #         print(df[f])
            df = step_2_pipline(df)
            # d = step_2_pipline(d)
            # print(df.columns)
            # print(d.columns)
            # for f in df.columns:
            #
            #     try:
            #         if not d[f].equals(df[f]):
            #             print(f, ": ")
            #             print(d[f].value_counts(dropna=False))
            #             print(df[f].value_counts(dropna=False))
            #             print("*********")
            #     except Exception as e:
            #         print(e)
            #         print(f)
            #         print(d[f])
            #         print(df[f])
            df = step_3_pipline(df)
            # d = step_3_pipline(d)
            # print(df.columns)
            # print(d.columns)
            # for f in df.columns:
            #     try:
            #         if not d[f].equals(df[f]):
            #             print(f, ": ")
            #             print(d[f].value_counts(dropna=False))
            #             print(df[f].value_counts(dropna=False))
            #             print("*********")
            #     except Exception as e:
            #         print(e)
            #         print(f)
            #         print(d[f])
            #         print(df[f])
            #
            self.df = df
            self.did_preproc = True
            # print(self.df["Asymmetrique Activity Index"].value_counts(dropna=False))
            # print(self.df["Asymmetrique Activity Score"].value_counts(dropna=False))
            # print(self.df["Asymmetrique Profile Index"].value_counts(dropna=False))
            # print(self.df["Asymmetrique Profile Score"].value_counts(dropna=False))
        return self

    def predict_and_save(self, db: Session):
        '''
        The function will run the model on our preprocessed samples and return a probability of converging +
        will save the samples in the db.
        Also, will keep the prob in a dict to return as a response to the user.
        :param db: db session
        '''
        will_convert = will_convert_prod_lr_model(self.df)
        for i, id in enumerate(self.lead_id.unique()):
            self.pred[int(id)] = will_convert[i]
            new_lead = Lead(lead_id=int(id), prob_convert=will_convert[i])
            db.add(new_lead)
        db.commit()
        return self

    def predictions_dict(self):
        '''
        Return a dict to send as a response to the user.
        '''
        return self.pred

    def get_all_ids(self, db: Session):
        return [id[0] for id in db.query(Lead.lead_id).all()]
