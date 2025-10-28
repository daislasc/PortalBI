"""
Script de ejecución del Portal BI
Ejecuta: python run.py
"""
import sys
import subprocess
from pathlib import Path

# Añadir src al path para imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

if __name__ == "__main__":
    # Ejecutar streamlit
    app_path = src_path / "app.py"
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", str(app_path)
    ])

