import pandas as pd
from dateutil.parser import parse
import operator

pd.options.mode.use_inf_as_na = True


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


def remove_rows_based_on_na(df):
    """
    Remove rows if it contains too many (> 50%) NA values
    @ input: df = data frame
    @ output: new data frame with rows removed if they contained too many NA values
    """


def predict_categorical_features(df):
    """
    Try to predict categorical features
    Example:
        - feature with values of 1-5 letters
        - feature with "category" or "cat" in their name
        - feature with 2 - 10 unique values
    @ input: df = data frame
    @ output:
    """


def define_categorical_features(df):
    """
    Define categorical features in the data frame
    @ input: df = data frame
    @ output: new data frame with categorical features
    """

    new_df = df.copy()

    feature_name_index = {}
    feature_unique_counts = {}

    for index, feature_name in enumerate(df.columns):
        feature_name_index[feature_name] = index
        feature_unique_values = df[feature_name].unique()
        feature_unique_counts[feature_name] = len(feature_unique_values)

        print("The feature name '%s' has %d unique values (examples of values: %s, %s or %s)."
              % (feature_name, feature_unique_counts[feature_name], feature_unique_values[0], feature_unique_values[1],
                 feature_unique_values[2]))

    wrong_value = True
    input_feature_name = 'q'
    while wrong_value:
        print("Which feature do you want to categorize? Write down its full name (press 'q' to stop this function).")

        input_feature_name = input()
        if input_feature_name in df.columns or input_feature_name == 'q':
            wrong_value = False
        else:
            print("Oops, it seems that this value is not accepted.")

    if input_feature_name == 'q':
        print("Exiting the categorization function ...")
        return new_df

    
def remove_na(df):
    for i, j in df.iteritems():
        print(i, j)


if __name__ == "__main__":
    df_1 = pd.read_csv('../../data/S&P500/all_stocks_5yr.csv', sep=',')
    df_2 = pd.read_csv('../../data/wine_quality/winequality_red_with_na.csv', sep=';')

    define_categorical_features(df_2)
