from typing import Callable, Tuple
import inspect
import tempfile
import pandas as pd
# TODO for testing let's work with csv's and json only -- We can work on other file sources later
from pandas import (
    read_csv,
    # read_parquet,
    read_excel,
    # read_gbq,
    read_json
)

# TODO once base reader is pretty ready, add shmexy doc string

class Reader:
    def __init__(self,
                 encoding:str = 'utf-8'):
        self.encoding = encoding

    def _get_reader(self,
                    file_path: str
                    ) -> Callable[[str],pd.core.frame.DataFrame]:

        if file_path.endswith('.csv'):
            return read_csv
        if file_path.endswith('.xlsx'):
            return read_excel
        if file_path.endswith('.json'):
            return read_json

