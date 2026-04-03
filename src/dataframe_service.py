import pandas as pd
from pandas import read_csv, DataFrame
from datetime import datetime

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
        self.sanitize()

    def sanitize(self) -> None:
        """Limpa e padroniza os dados"""
        if self.dataframe is None:
            raise ValueError("DataFrame não inicializado")
        
        # Converter OrderDate para datetime
        self.dataframe["OrderDate"] = pd.to_datetime(self.dataframe["OrderDate"])
        
        # Remover duplicatas
        self.dataframe = self.dataframe.drop_duplicates(subset=["OrderID"])
        
        # Preencher valores nulos com 0 (numéricos) ou "Unknown" (categóricos)
        numeric_cols = ["Quantity", "UnitPrice", "Discount", "Tax", "ShippingCost", "TotalAmount"]
        for col in numeric_cols:
            self.dataframe[col] = self.dataframe[col].fillna(0)
        
        self.dataframe["PaymentMethod"] = self.dataframe["PaymentMethod"].fillna("Unknown")
        self.dataframe["City"] = self.dataframe["City"].fillna("Unknown")
        
        # Padronizar OrderStatus
        self.dataframe["OrderStatus"] = self.dataframe["OrderStatus"].str.capitalize()
        
        # Resetar índice
        self.dataframe = self.dataframe.reset_index(drop=True)