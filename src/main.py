import sys
from pathlib import Path
from path_handler import PathHandler
from dataframe_service import DataFrameService
from metrics_service import MetricsService
from report_generator import ReportGenerator

# caminhos absolutos de pdfs e planilhas
PDFS_DIRECTORY = PathHandler.get_directory("shared/pdfs")
SHEETS_DIRECTORY = PathHandler.get_directory("shared/sheets")

def main(csv_file: str = None, month: int = None, year: int = None):
    """Executa pipeline: CSV → Métricas → PDF"""
    
    if not csv_file:
        csv_file = f"{SHEETS_DIRECTORY}/Amazon-sales.csv"
    
    # 1. Carregar e sanitizar dados
    df_service = DataFrameService()
    df_service.csv_to_dataframe(csv_file)
    print(f"✓ {len(df_service.dataframe)} registros carregados")
    
    # 2. Calcular métricas
    metrics_service = MetricsService(df_service.dataframe)
    metrics = metrics_service.calculate_all(month, year)
    print(f"✓ Métricas calculadas")
    
    # 3. Gerar PDF
    report_gen = ReportGenerator(metrics)
    if month and year:
        output_file = f"{PDFS_DIRECTORY}/relatorio_{month:02d}_{year}.pdf"
    else:
        output_file = f"{PDFS_DIRECTORY}/relatorio_all.pdf"
    report_gen.generate_pdf(output_file)
    print(f"✓ PDF gerado: {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Gera relatório de vendas em PDF")
    parser.add_argument("--csv", help="Caminho do CSV", default=None)
    parser.add_argument("--month", type=int, help="Mês (1-12)", default=None)
    parser.add_argument("--year", type=int, help="Ano", default=None)
    
    args = parser.parse_args()
    main(args.csv, args.month, args.year)
