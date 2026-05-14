import pandas as pd
from pandas import read_csv, DataFrame
from pathlib import Path
from column_aliases import normalize_columns, validate_columns

class DataFrameService:
    def __init__(self):
        self.dataframe: DataFrame | None = None

    def load_dataframe(self, file_path: str) -> None:
        """
        Carrega um arquivo (CSV ou XLSX) automaticamente baseado na extensão.
        
        Args:
            file_path: Caminho do arquivo
            
        Raises:
            ValueError: Se a extensão não é suportada
        """
        path = Path(file_path)
        extension = path.suffix.lower()
        
        if extension == ".csv":
            self.csv_to_dataframe(file_path)
        elif extension in [".xlsx", ".xls"]:
            self.xlsx_to_dataframe(file_path)
        else:
            raise ValueError(f"Extensão de arquivo não suportada: {extension}")

    def csv_to_dataframe(self, csv: str) -> None:
        self.dataframe = read_csv(csv)
        # Normaliza nomes de colunas
        self.dataframe = normalize_columns(self.dataframe)
        # Seleciona e reordena colunas padrão
        self.dataframe = self.dataframe[[
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
        ]]
        self.sanitize()

    def xlsx_to_dataframe(self, xlsx: str) -> None:
        self.dataframe = pd.read_excel(xlsx)
        # Normaliza nomes de colunas
        self.dataframe = normalize_columns(self.dataframe)
        # Seleciona e reordena colunas padrão
        self.dataframe = self.dataframe[[
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
        ]]
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