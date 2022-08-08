import pandas as pd
from sqlalchemy.orm import Session
from var import data_file_prefix,data_file_name

class lead_repo():

    def __init__(self, df):
        self.df = pd.DataFrame()

