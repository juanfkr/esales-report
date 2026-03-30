from pathlib import Path
from pdf_generator_service import PdfGeneratorService
from dataframe_service import DataFrameService
from path_handler import PathHandler

path_handler = PathHandler()

PDFS_DIRECTORY: Path = path_handler.get_directory("shared/pdfs")
SHEETS_DIRECTORY: Path = path_handler.get_directory("shared/sheets")

pdf_generator = PdfGeneratorService(f"{PDFS_DIRECTORY}/teste.pdf")

pdf_generator.generate_pdf("teste")

df = DataFrameService()
df.csv_to_dataframe(f"{SHEETS_DIRECTORY}/Amazon-sales.csv")

local_df = df.get_dataframe()

print(local_df)
