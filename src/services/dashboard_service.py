"""
Servicio para gestión de dashboards
"""
from pathlib import Path
from typing import Dict, List
import yaml

from models import Dashboard, DashboardSection
from config import CONFIG_DIR


class DashboardService:
    """
    Servicio para cargar y gestionar dashboards
    """
    
    def __init__(self, config_file: str = "dashboards.yaml"):
        """
        Inicializa el servicio de dashboards
        
        Args:
            config_file: Nombre del archivo de configuración YAML
        """
        self.config_path = CONFIG_DIR / config_file
        self._dashboards_data: Dict[str, List[Dashboard]] = {}
        self._load_dashboards()
    
    def _load_dashboards(self) -> None:
        """Carga los dashboards desde el archivo YAML"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            # Convertir los datos YAML a objetos Dashboard
            self._dashboards_data = {}
            for section_name, dashboards_list in data.get('dashboards', {}).items():
                self._dashboards_data[section_name] = [
                    Dashboard.from_dict(dash_data)
                    for dash_data in dashboards_list
                ]
        except Exception as e:
            raise RuntimeError(f"Error al cargar dashboards: {str(e)}")
    
    def get_sections(self) -> List[str]:
        """
        Obtiene la lista de secciones disponibles
        
        Returns:
            Lista de nombres de secciones
        """
        return list(self._dashboards_data.keys())
    
    def get_section(self, section_name: str) -> DashboardSection:
        """
        Obtiene una sección específica con sus dashboards
        
        Args:
            section_name: Nombre de la sección
            
        Returns:
            DashboardSection con los dashboards de la sección
        """
        dashboards = self._dashboards_data.get(section_name, [])
        return DashboardSection(name=section_name, dashboards=dashboards)
    
    def get_all_dashboards(self) -> Dict[str, List[Dashboard]]:
        """
        Obtiene todos los dashboards organizados por sección
        
        Returns:
            Diccionario con secciones y sus dashboards
        """
        return self._dashboards_data.copy()
    
    def reload_dashboards(self) -> None:
        """Recarga los dashboards desde el archivo de configuración"""
        self._load_dashboards()

