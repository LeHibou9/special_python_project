import pandas as pd
from src import dataset


def join(datasets, args):
    dataset_1: dataset.Dataset = datasets['dataset_1']
    dataset_2: dataset.Dataset = datasets['dataset_2']
    df_1_join_key = args['df_1_join_key']
    df_2_join_key = args['df_2_join_key']
    type_of_join = args['type_of_join']

    new_df = dataset_1.df.merge(dataset_2.df, how=type_of_join, left_on=df_1_join_key, right_on=df_2_join_key)

    return dataset.Dataset(new_df, origin='function', function='join', dataset_1=dataset_1.filename,
                           dataset_2=dataset_2.filename)


existing_functions = {
    'join': join
}
