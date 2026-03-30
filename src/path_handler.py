from pathlib import Path

class PathHandler:    
    @staticmethod
    def get_directory(target: str) -> Path:
        """retorna o diretório especificado"""
        path = Path(target)

        if not type(target) is str:
            raise(ValueError("Diretório deve ser uma string"))
        
        if not path.exists():
            raise(FileNotFoundError("Diretório não encontrado"))

        return path