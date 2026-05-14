from pathlib import Path

from path_handler import get_directory
from dataframe_service import DataFrameService
from metrics_service import MetricsService
from report_generator import ReportGenerator

# caminhos absolutos de pdfs e planilhas
PDFS_DIRECTORY = get_directory("shared/pdfs")
SHEETS_DIRECTORY = get_directory("shared/sheets")

def main(csv_file: str = None, month: int = None, year: int = None):
    if not csv_file:
        csv_file = str(SHEETS_DIRECTORY / "Amazon-sales.csv")
    

    df_service = DataFrameService()

    df_service.load_dataframe(csv_file)
    print(f"✓ {len(df_service.dataframe)} registros carregados")
    
    metrics_service = MetricsService(df_service.dataframe)
    metrics = metrics_service.calculate_all(month, year)
    print("✓ Métricas calculadas")
    
    report_gen = ReportGenerator(metrics)
    if month and year:
        output_file = str(PDFS_DIRECTORY / f"relatorio_{month:02d}_{year}.pdf")
    else:
        output_file = str(PDFS_DIRECTORY / "relatorio_all.pdf")
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
