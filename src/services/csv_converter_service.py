from pandas import read_csv, DataFrame

class CsvConverterService:
    def __init__(self):
        self.dataframe = None

    def get_dataframe(self) -> DataFrame:
        return self.dataframe

    def csv_to_dataframe(self, target: str) -> None:
        self.dataframe = read_csv(target)