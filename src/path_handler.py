from pathlib import Path

class PathHandler:
    CURRENT_DIRECTORY = Path(__file__).resolve().parent
    
    @staticmethod
    def get_directory(target: str) -> Path:
        """retorna o diretório especificado"""
        path = Path(target)

        if not type(target) is str:
            raise(ValueError("Diretório inválido"))
        
        if not path.exists():
            raise(FileNotFoundError("Diretório não encontrado"))

        return path