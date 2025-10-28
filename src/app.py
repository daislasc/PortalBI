"""
Portal BI - Aplicación principal
Sistema de visualización de dashboards de Looker Studio
"""
import streamlit as st

from config import PAGE_CONFIG, UI_CONFIG
from services import DashboardService
from components import render_sidebar, render_dashboard_grid


def initialize_page() -> None:
    """Configura la página de Streamlit"""
    st.set_page_config(**PAGE_CONFIG)


def render_header() -> None:
    """Renderiza el encabezado de la aplicación"""
    st.image(UI_CONFIG["logo_path"], width=UI_CONFIG["logo_width"])
    st.title("BI Portal")


def main() -> None:
    """Función principal de la aplicación"""
    # Inicializar página
    initialize_page()
    
    # Renderizar encabezado
    render_header()
    
    # Inicializar servicio de dashboards
    dashboard_service = DashboardService()
    
    # Obtener secciones disponibles
    sections = dashboard_service.get_sections()
    
    # Renderizar sidebar y obtener sección seleccionada
    selected_section = render_sidebar(sections)
    
    # Mostrar sección seleccionada
    st.header(selected_section)
    
    # Obtener dashboards de la sección
    section_data = dashboard_service.get_section(selected_section)
    
    # Renderizar grid de dashboards
    render_dashboard_grid(
        section_data.dashboards,
        columns=UI_CONFIG["cards_per_row"]
    )


if __name__ == "__main__":
    main()

