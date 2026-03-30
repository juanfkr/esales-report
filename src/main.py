from path_handler import PathHandler
from dataframe_service import DataFrameService

# caminhos absolutos de pdfs e planilhas
PDFS_DIRECTORY = PathHandler.get_directory("shared/pdfs")
SHEETS_DIRECTORY = PathHandler.get_directory("shared/sheets")

df = DataFrameService()
df.csv_to_dataframe(f"{SHEETS_DIRECTORY}/Amazon-sales.csv")

local_df = df.dataframe

print(local_df)
