from pathlib import Path
from services.pdf_generator_service import PdfGeneratorService
from core.path_handler import PathHandler
from services.csv_converter_service import CsvConverterService

path_handler = PathHandler()

PDFS_DIRECTORY: Path = path_handler.get_directory("shared/pdfs")
SHEETS_DIRECTORY: Path = path_handler.get_directory("shared/sheets")

pdf_generator = PdfGeneratorService(f"{PDFS_DIRECTORY}/teste.pdf")

pdf_generator.generate_pdf("teste")

csv_converter = CsvConverterService()

csv_converter.csv_to_dataframe(f"{SHEETS_DIRECTORY}/Amazon-sales.csv")
df = csv_converter.get_dataframe()

print(df)