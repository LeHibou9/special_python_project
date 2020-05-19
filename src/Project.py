import pandas as pd
from src import dataset


class Project:
    def __init__(self, list_filenames=[]):
        self.list_datasets = []
        self.list_operations = []

        for filename in list_filenames:
            self.list_datasets.append(dataset.Dataset(filename))

    # def modify_dataset(self, function_to_use, arguments, testing=False):

    def get_list_datasets(self):
        return self.list_datasets

    def print_list_datasets(self):
        for index, filename in enumerate(self.list_datasets):
            print('Filename %d: %s' % (index, filename))


if __name__ == "__main__":
    project = Project(['data/S&P500/all_stocks_5yr.csv'])
