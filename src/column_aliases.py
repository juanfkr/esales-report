"""
Definição de aliases e normalização de nomes de colunas.
Mapeamento para tratar diferentes nomes de colunas que possam vir de diferentes fontes.
"""

# Mapeamento de possíveis nomes para o nome padrão
COLUMN_ALIASES = {
    # Order ID
    "OrderID": ["orderid", "order_id", "id", "pedido", "pedido_id", "order number"],
    
    # Order Date
    "OrderDate": ["orderdate", "order_date", "data_pedido", "data do pedido", "date"],
    
    # Product ID
    "ProductID": ["productid", "product_id", "produto_id", "product number"],
    
    # Product Name
    "ProductName": ["productname", "product_name", "nome_produto", "product"],
    
    # Category
    "Category": ["category", "categoria", "cat"],
    
    # Brand
    "Brand": ["brand", "marca"],
    
    # Quantity
    "Quantity": ["quantity", "qty", "quantidade", "qtd"],
    
    # Unit Price
    "UnitPrice": ["unitprice", "unit_price", "preço_unitário", "price", "valor_unitario"],
    
    # Discount
    "Discount": ["discount", "desconto", "disc"],
    
    # Tax
    "Tax": ["tax", "imposto", "taxa"],
    
    # Shipping Cost
    "ShippingCost": ["shippingcost", "shipping_cost", "frete", "custo_frete"],
    
    # Total Amount
    "TotalAmount": ["totalamount", "total_amount", "total", "valor_total"],
    
    # Payment Method
    "PaymentMethod": ["paymentmethod", "payment_method", "método_pagamento", "payment"],
    
    # Order Status
    "OrderStatus": ["orderstatus", "order_status", "status", "status_pedido"],
    
    # City
    "City": ["city", "cidade"],
    
    # State
    "State": ["state", "estado", "uf"],
    
    # Country
    "Country": ["country", "país", "pais"],
}

# Colunas obrigatórias
REQUIRED_COLUMNS = [
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
]


def normalize_columns(dataframe):
    """
    Normaliza os nomes das colunas do DataFrame para os nomes padrão.
    
    Args:
        dataframe: DataFrame com colunas a serem normalizadas
        
    Returns:
        DataFrame com colunas renomeadas para nomes padrão
    """
    rename_mapping = {}
    
    for col in dataframe.columns:
        col_lower = col.lower().strip()
        
        # Procura correspondência nos aliases
        for standard_name, aliases in COLUMN_ALIASES.items():
            if col_lower == standard_name.lower() or col_lower in aliases:
                rename_mapping[col] = standard_name
                break
    
    # Aplica renomeação
    if rename_mapping:
        dataframe = dataframe.rename(columns=rename_mapping)
    
    return dataframe


def validate_columns(dataframe):
    """
    Valida se todas as colunas obrigatórias estão presentes.
    
    Args:
        dataframe: DataFrame a validar
        
    Raises:
        ValueError: Se colunas obrigatórias estão faltando
    """
    missing_columns = set(REQUIRED_COLUMNS) - set(dataframe.columns)
    
    if missing_columns:
        raise ValueError(
            f"Colunas obrigatórias faltando: {', '.join(sorted(missing_columns))}"
        )
