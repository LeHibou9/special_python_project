import pandas as pd
from uuid import uuid4


class Dataset:
    def __init__(self, *args, **kwds):
        self.id = uuid4()

        if 'origin' in kwds and kwds['origin'] == 'filename':
            filename = args[0]
            self.origin = 'original'
            self.path = filename
            self.filename = filename.split('/')[-1]
            self.df = pd.read_csv(filename)

        elif 'origin' in kwds and kwds['origin'] == 'function':
            self.origin = 'function'
            self.path = kwds['function']
            self.filename = kwds['function'] + '_' + kwds['dataset_1'] + '_&_' + kwds['dataset_2']
            self.df = pd.read_csv(args[0])

        else:
            raise AttributeError()
