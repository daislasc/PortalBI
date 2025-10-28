"""
Funciones auxiliares para el Portal BI
"""
from pathlib import Path
from typing import Optional


def load_markdown_file(file_path: Path) -> Optional[str]:
    """
    Carga el contenido de un archivo markdown
    
    Args:
        file_path: Ruta al archivo markdown
        
    Returns:
        Contenido del archivo o None si hay error
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error al cargar archivo markdown: {str(e)}")
        return None


def ensure_path_exists(path: Path) -> bool:
    """
    Verifica que una ruta existe
    
    Args:
        path: Ruta a verificar
        
    Returns:
        True si la ruta existe, False en caso contrario
    """
    return path.exists()

