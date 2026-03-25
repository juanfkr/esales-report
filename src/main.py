import pandas
from pandas import DataFrame

SHEETS_PATH: str = "../shared/sheets"

df: DataFrame = pandas.read_csv(f"{SHEETS_PATH}/Amazon-sales.csv")
