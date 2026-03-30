from datetime import datetime

from pandas import read_csv, DataFrame

class DataFrameService:
    def __init__(self):
        self.dataframe = None

    def get_dataframe(self) -> DataFrame:
        return self.dataframe

    def csv_to_dataframe(self, csv: str) -> None:
        self.dataframe = read_csv(csv, usecols=[
            "OrderID",
            "OrderDate",
            "ProductID",
            "ProductName",
            "Category",
            "Brand",
            "Quantity",
            "UnitPrice",
            "Discount",
            "Tax",
            "ShippingCost",
            "TotalAmount",
            "PaymentMethod",
            "OrderStatus",
            "City",
            "State",
            "Country"
        ])