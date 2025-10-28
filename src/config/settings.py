"""
Configuración general del portal BI
"""
from pathlib import Path
from typing import Dict, Any

# Rutas del proyecto
PROJECT_ROOT = Path(__file__).parent.parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
STYLES_DIR = ASSETS_DIR / "styles"
DOCS_DIR = PROJECT_ROOT / "docs"
CONFIG_DIR = PROJECT_ROOT / "src" / "config"

# Configuración de la página
PAGE_CONFIG: Dict[str, Any] = {
    "page_title": "Portal BI - Ingetek",
    "layout": "wide",
    "page_icon": str(IMAGES_DIR / "ingetek-logo.png")
}

# Configuración de UI
UI_CONFIG = {
    "logo_path": str(IMAGES_DIR / "ingetek-logo-completo.png"),
    "logo_width": 300,
    "cards_per_row": 3,
    "instructivo_path": str(DOCS_DIR / "instructivo_dashboards.md")
}

# Configuración de colores corporativos
BRAND_COLORS = {
    "primary": "#18515F",
    "secondary": "#2A7C8F",
    "accent": "#4A9FB0",
    "background": "#FFFFFF",
    "border": "#DDDDDD"
}

