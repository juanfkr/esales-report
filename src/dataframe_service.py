from pandas import read_csv, DataFrame

class DataFrameService:
    def __init__(self):
        self.dataframe: DataFrame | None = None

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