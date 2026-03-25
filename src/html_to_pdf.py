from weasyprint import HTML

import pandas
from pandas import DataFrame

SHEETS_PATH: str = "../shared/sheets"

df: DataFrame = pandas.read_csv(f"{SHEETS_PATH}/Amazon-sales.csv")

HTML(string=f"<p>{df}</p>").write_pdf("document.pdf", pdf_variant="pdf/a-3u")

