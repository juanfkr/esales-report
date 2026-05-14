from pathlib import Path

def get_directory(target: str) -> Path:
    """
    Retorna o caminho absoluto do diretório.
    
    Args:
        target: Caminho relativo ao raiz do projeto
        
    Returns:
        Path absoluto do diretório
        
    Raises:
        ValueError: Se target não é string
        FileNotFoundError: Se diretório não existe
    """
    if type(target) is not str:
        raise ValueError("Diretório deve ser uma string")
    
    # Obtém o diretório raiz do projeto (um nível acima de src/)
    project_root = Path(__file__).parent.parent
    path = project_root / target
    
    if not path.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {path}")

    return path
