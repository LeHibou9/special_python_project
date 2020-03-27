import pandas as pd


class Join:
    def __init__(self, type_join='inner'):
        self.type_join = type_join
        self.dict_join = {
            'inner': self.inner_join,
            'left': self.left_join,
            'right': self.right_join
        }

    @staticmethod
    def inner_join(df_1, df_2):
        inner_join_df = df_1.copy()
        return inner_join_df.join(df_2, how='inner')

    @staticmethod
    def left_join(df_1, df_2):
        left_join_df = df_1.copy()
        return left_join_df.join(df_2, how='left')

    @staticmethod
    def right_join(df_1, df_2):
        right_join_df = df_1.copy()
        return right_join_df.join(df_2, how='right')

    def join(self, df_1, df_2):
        return self.dict_join[self.type_join](df_1, df_2)


if __name__ == "__main__":
    df_1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                         'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
    df_1.set_index('key')
    print(df_1.keys())

    df_2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                         'B': ['B0', 'B1', 'B2']})
    df_2.set_index('key')
    print(df_2.keys())

    join_instance = Join(type_join='inner')
    new_df = join_instance.join(df_1, df_2)
    print(new_df.head())
