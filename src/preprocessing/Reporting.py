import pandas as pd


def compute_correlation(df):
    return 0


if __name__ == "__main__":
    df_1 = pd.read_csv('../../data/S&P500/all_stocks_5yr.csv', sep=',')
    df_2 = pd.read_csv('../../data/wine_quality/winequality_red_with_na.csv', sep=';')

    print(df_2.corr())
    corr = df_2.corr()
    print(corr > 0.95)
