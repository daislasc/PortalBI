"""
Modelo de datos para Dashboard
"""
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Dashboard:
    """
    Representa un dashboard individual en el portal
    """
    title: str
    url_dashboard: str
    url_docu: str
    color: str

    def to_dict(self) -> Dict[str, str]:
        """Convierte el dashboard a diccionario"""
        return {
            "title": self.title,
            "url_dashboard": self.url_dashboard,
            "url_docu": self.url_docu,
            "color": self.color
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'Dashboard':
        """Crea un Dashboard desde un diccionario"""
        return cls(
            title=data["title"],
            url_dashboard=data["url_dashboard"],
            url_docu=data["url_docu"],
            color=data["color"]
        )


@dataclass
class DashboardSection:
    """
    Representa una sección de dashboards
    """
    name: str
    dashboards: List[Dashboard]

    def __len__(self) -> int:
        """Retorna el número de dashboards en la sección"""
        return len(self.dashboards)

    def is_empty(self) -> bool:
        """Verifica si la sección está vacía"""
        return len(self.dashboards) == 0

