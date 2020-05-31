import pandas as pd
from src import dataset
from src.functions import existing_functions


class Project:
    def __init__(self, list_filenames):
        self.list_datasets = {}
        self.list_operations = []

        for filename in list_filenames:
            new_dataset = dataset.Dataset(filename)
            self.list_datasets[new_dataset.id] = new_dataset
            self.list_datasets.append(dataset.Dataset(filename))

    def run_operation(self, function_to_use, datasets: [dataset.Dataset], arguments: dict, testing: bool = False):
        if function_to_use in existing_functions:
            new_dataset = existing_functions[function_to_use(datasets, arguments)]

            self.list_datasets[new_dataset.id] = new_dataset
            self.list_operations.append([function_to_use, datasets])

    def get_list_datasets(self):
        return self.list_datasets

    def print_list_datasets(self):
        for index, filename in enumerate(self.list_datasets):
            print('Filename %d: %s' % (index, filename))


if __name__ == "__main__":
    project = Project(['data/S&P500/all_stocks_5yr.csv'])
