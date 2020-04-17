import pandas as pd
from dateutil.parser import parse
import operator


NA_CHARACTERS = [
    "",
    "NA",
    "None"
]


BOOLEAN_CHARACTERS = [
    "true",
    "false",
    "t",
    "f"
]


def check_type(column_to_check):
    """
    Check the most common type in a column.
    @ input: column_to_check = a column to check.
    @ output: type of the column to check (the type is in string format).
    """

    count_types = {'int': 0, 'float': 0, 'bool': 0, 'datetime64': 0, 'object': 0}

    for value in column_to_check:
        try:
            _ = int(value)
            count_types['int'] += 1
            continue
        except ValueError:
            pass

        try:
            _ = float(value)
            count_types['float'] += 1
            continue
        except ValueError:
            pass

        if value.lower() in BOOLEAN_CHARACTERS:
            count_types['bool'] += 1
            continue

        try:
            _ = parse(value.lower())
            count_types['datetime64'] += 1
            continue
        except ValueError:
            pass

        count_types['object'] += 1

    return max(count_types.items(), key=operator.itemgetter(1))[0]


def check_type_of_object(column_to_check):
    """
    Check the most common type in an object column.
    @ input: column_to_check = a column to check with object values.
    @ output: type of the object column to check (the type is in string format).
    """

    count_types = {'bool': 0, 'datetime64': 0, 'object': 0}

    for value in column_to_check:
        if value.lower() in BOOLEAN_CHARACTERS:
            count_types['bool'] += 1
            continue

        try:
            _ = parse(value.lower())
            count_types['datetime64'] += 1
            continue
        except ValueError:
            pass

        count_types['object'] += 1

    return max(count_types.items(), key=operator.itemgetter(1))[0]


def determine_column_types(df):
    """
    Determine column types of a data frame
    @ input: df = data frame
    @ output: new data frame with new column types
    """

    change_of_column_types = {}

    for column, column_type in zip(df.columns, df.dtypes):
        if column_type == "object":
            change_of_column_types[column] = check_type_of_object(df[column].values)

    return df.astype(change_of_column_types)


def remove_na(df):
    for i, j in df.iteritems():
        print(i, j)


if __name__ == "__main__":
    df_1 = pd.read_csv('../../data/S&P500/all_stocks_5yr.csv', sep=',')

    df_1 = determine_column_types(df_1)
    print(df_1.head())
