import pandas as pd
from uuid import uuid4


class Dataset:
    def __init__(self, filename):
        self.id = uuid4()
        self.path = filename
        self.filename = filename.split('/')[-1]
        self.df = pd.read_csv(filename)

    # def modify_dataset(self, function_to_use, arguments, testing=False):
