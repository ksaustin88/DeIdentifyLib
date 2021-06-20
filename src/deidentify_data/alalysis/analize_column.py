import pandas as pd
import numpy as np

class Analyze_Column:
    # Do we want a base analyze colmun class?
    def __init__(self):
        self.df = None
        self.col = None
        self.nulls = [None, np.nan]

    def _separate_nulls_and_non_nulls(self, df, col):
        # Separate column into nulls and non nulls
        return df[col][df[col].isin(self.nulls)], df[col][~df[col].isin(self.nulls)]

    def _analyze(self, df, col):
        self.df = df
        self.col = col

        df_null, df_valid = self._separate_nulls_and_non_nulls(self.df, self.col)