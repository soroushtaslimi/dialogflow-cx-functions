import pandas as pd

class DataManager():
    def __init__(self, raw_data):
        columns = raw_data[0]
        rows = raw_data[1:]

        self.df = pd.DataFrame(rows, columns=columns)
        print(self.df)

    