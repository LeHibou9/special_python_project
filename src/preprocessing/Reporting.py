import pandas as pd


def compute_high_correlations(df):
    """
    Compute high correlations between two columns
    @ input: df = data frame
    @ output: list of tuples of highly correlated columns
    """

    correlations = df.corr()
    column_names = correlations.columns

    very_high_correlations = []

    for i in range(1, len(column_names)):
        for j in range(i):
            if correlations[column_names[i]][column_names[j]] >= 0.9:
                very_high_correlations.append([column_names[i], column_names[j]])

    return very_high_correlations


if __name__ == "__main__":
    df_1 = pd.read_csv('../../data/S&P500/all_stocks_5yr.csv', sep=',')
    df_2 = pd.read_csv('../../data/wine_quality/winequality_red.csv', sep=';')

    print(compute_high_correlations(df_2))
