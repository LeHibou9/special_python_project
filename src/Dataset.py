import pandas as pd


class Dataset:
    def __init__(self, list_files):
        self.list_files = list_files
        self.list_df = []  # possibility to transform into dictionary so that people can give titles to dataframe.

        for file in list_files:
            df = pd.DataFrame(file)
            self.list_df.append(df)

    def get_list_datasets(self):
        return self.list_files

    def print_list_datasets(self):
        for index, filename in enumerate(self.list_files):
            print('Filename %d: %s' % (index, filename))
