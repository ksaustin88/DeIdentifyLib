from src.deidentify_data.io.base_reader import Reader
from typing import Callable, Tuple
import inspect
import tempfile
import pandas as pd
from pandas import (
    read_csv,
    read_parquet,
    read_excel,
    read_gbq,
    read_json
)




class FullReader(Reader):
    def __init__(self,
                 **kwargs):
        self.kwargs = kwargs
        # super().__init__(**kwargs)
    def _get_data(self, file_path):
        reader = self._get_reader(file_path=file_path)
        data = reader(file_path, **self.kwargs)
        return data