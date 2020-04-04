import pandas as pd


NA_CHARACTERS = [
    "",
    "NA",
    "None"
]


def check_type(column_to_check):
    type_of_column = "int"

    for value in column_to_check:
        if type_of_column == "int":
            try:
                _ = int(value)
            except ValueError:
                type_of_column = "float"

        if type_of_column == "float":
            try:
                _ = float(value)
            except ValueError:
                type_of_column = "str"

        if type_of_column == "str":
            return "str"

    return type_of_column


def remove_na(df):
    return None


if __name__ == "__main__":
    # df_1 = pd.read_csv('../../data/wine_quality/winequality_red_with_na.csv', sep=';')

    print('[3, 2, 3, 1, 0, -1]', check_type(['3', '2', '3', '1', '0', '-1']))
    print('[3, 2.0, 3, 1, 0, -1]', check_type(['3', '2.0', '3', '1', '0', '-1']))
    print('[3, 2.0, a, 1, 0, -1]', check_type(['3', '2.0', 'a', '1', '0', '-1']))
