import pandas as pd


class Convert:
    def df_to_json(self,
                   df: pd.core.frame.DataFrame,
                   sep: str = '.') -> list:
        return_data = []
        for index,row in df.iterrows():
            return_obj = {}
            for item in row:
                return_obj[item[0]] = item[1]
