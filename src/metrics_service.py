import pandas as pd

class MetricsService:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
        self.metrics = {}

    def calculate_all(self, month: int = None, year: int = None) -> dict:
        """Calcula todas as métricas. Se month/year, filtra período"""
        if month and year:
            self.df = self._filter_by_period(month, year)
        
        self.metrics = {
            "period": f"{month:02d}/{year}" if month and year else "All",
            "total_orders": len(self.df),
            "total_revenue": float(self.df["TotalAmount"].sum()),
            "average_order_value": float(self.df["TotalAmount"].mean()),
            "delivered_orders": int((self.df["OrderStatus"] == "Delivered").sum()),
            "cancelled_orders": int((self.df["OrderStatus"] == "Cancelled").sum()),
            "returned_orders": int((self.df["OrderStatus"] == "Returned").sum()),
            "delivery_rate": float((self.df["OrderStatus"] == "Delivered").sum() / len(self.df) * 100),
            "top_categories": self._top_categories(5),
            "top_brands": self._top_brands(5),
            "top_countries": self._top_countries(5),
            "revenue_by_payment": self._revenue_by_payment(),
            "total_discount": float(self.df["Discount"].sum()),
            "total_tax": float(self.df["Tax"].sum()),
            "total_shipping": float(self.df["ShippingCost"].sum()),
        }
        return self.metrics

    def _filter_by_period(self, month: int, year: int) -> pd.DataFrame:
        """Filtra dados por mês e ano"""
        return self.df[
            (self.df["OrderDate"].dt.month == month) & 
            (self.df["OrderDate"].dt.year == year)
        ]

    def _top_categories(self, limit: int) -> dict:
        top = self.df["Category"].value_counts().head(limit)
        return top.to_dict()

    def _top_brands(self, limit: int) -> dict:
        top = self.df["Brand"].value_counts().head(limit)
        return top.to_dict()

    def _top_countries(self, limit: int) -> dict:
        top = self.df.groupby("Country")["TotalAmount"].sum().nlargest(limit)
        return top.to_dict()

    def _revenue_by_payment(self) -> dict:
        revenue = self.df.groupby("PaymentMethod")["TotalAmount"].sum()
        return revenue.to_dict()