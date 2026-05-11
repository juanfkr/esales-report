from pathlib import Path

def get_directory(target: str) -> Path:
    path = Path(target)

    if type(target) is not str:
        raise(ValueError("Diretório deve ser uma string"))
        
    if not path.exists():
        raise(FileNotFoundError("Diretório não encontrado"))

    return path

def check_file_extension(file: Path):
    if file.suffix == ".csv":
        return "csv"
    elif file.suffix == ".xlsx":
        return "xlsx"
    
    raise(ValueError("Formato de arquivo não suportado"))