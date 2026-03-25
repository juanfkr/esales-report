import pandas
from pandas import DataFrame

SHEETS_PATH: str = "src/data/"

df: DataFrame = pandas.read_csv(f"{SHEETS_PATH}/car_prices.csv")
