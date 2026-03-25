#import pandas
#from pandas import DataFrame
from pathlib import Path
from services.pdf_generator_service import PdfGeneratorService

#df: DataFrame = pandas.read_csv(f"{SHEETS_PATH}/Amazon-sales.csv")

BASE_DIR = Path(__file__).resolve().parent.parent

SHEETS_PATH = BASE_DIR / "shared" / "sheets"
GENERATED_PDF_PATH = BASE_DIR / "shared" / "pdfs"

GENERATED_PDF_PATH.mkdir(parents=True, exist_ok=True)

target_path = str(GENERATED_PDF_PATH / "document.pdf")
pdf_generator = PdfGeneratorService(target_path)

pdf_generator.generate_pdf("teste")

pdf_generator = PdfGeneratorService(f"{GENERATED_PDF_PATH}/document.pdf");

pdf_generator.generate_pdf("teste")